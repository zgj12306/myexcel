from django.shortcuts import render, get_object_or_404, get_list_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .models import Project,ProjectTable, Table, Column, Value
from django.contrib.auth.models import User
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from mysite.common.response import json_response
import json

@login_required(redirect_field_name='', login_url='/admin/login/')
def project(request):
    project_list = Project.objects.filter(user=request.user)
    context = {'list': project_list}
    return render(request, 'myexcel/index.html', context)

@login_required(redirect_field_name='', login_url='/admin/login/')
def detail(request, pk):
    tables = ProjectTable.objects.filter(project=pk).all()
    return render(request, 'myexcel/tables.html', {'list': tables})

@login_required(redirect_field_name='', login_url='/admin/login/')
def excel(request, pk):
    context = {}
    project_table = ProjectTable.objects.get(pk=pk)
    if request.POST:
        data = request.POST['data']
        value = Value(value=json.dumps(data), project_table=project_table)
        value.save()
        return json_response('保存成功！')
    else:
        data = Value.objects.filter(project_table=project_table)
        if data:
            data = data[0].value
        else:
            data = json.dumps("[[]]")
    c = []

    columns = Column.objects.filter(table=project_table.table)
    for column in columns:
        c.append({'title': column.column_name, 'width': column.width})
    context['columns'] = json.dumps(c)
    context['minDimensions'] = json.dumps([len(c),project_table.table.table_row])
    context['data'] = data
    return render(request, 'myexcel/excel.html', context)