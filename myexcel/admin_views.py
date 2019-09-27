from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Project

@login_required(redirect_field_name='', login_url='/admin/login/')
def change_list(request):
    return render(
        request,
        template_name="admin/myexcel/project/change_list.html",
        context={'projects': Project.objects.all()}
    )