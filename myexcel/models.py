from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    project_name = models.CharField('项目名称', max_length=50)
    project_text = models.TextField('项目描述', null=True)
    project_charge = models.CharField('项目负责人', max_length=50, default='赵旻')
    pub_date = models.DateTimeField('date published', auto_now=True)

    def __str__(self):
        return self.project_name

class Table(models.Model):
    table_name = models.CharField('excel表名', max_length=50)
    table_en_name =  models.CharField('英文名', max_length=50, null=True)
    table_row = models.IntegerField('行数', default=10)
    pub_date = models.DateTimeField('date published', auto_now=True)

    def __str__(self):
        return self.table_name

class ProjectTable(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, db_index=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, db_index=True)

class Column(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, db_index=True)
    column_name = models.CharField('列名', max_length=50)
    column_en_name = models.CharField('英文名', max_length=50)
    parameter = models.CharField('参数名', max_length=10, null=True)
    formula = models.CharField('公式', max_length=100, null=True)
    dropdown = models.ForeignKey(Value, on_delete=models.CASCADE, null=True)
    default = models.CharField('默认值', max_length=10, null=True)
    prompt = models.CharField('提示', max_length=100, null=True)
    must = models.BooleanField('是否必填', default=True)
    pub_date = models.DateTimeField('date published', auto_now=True)

    def __str__(self):
        return self.column_name

class Value(models.Model):
    project_table = models.ForeignKey(ProjectTable, on_delete=models.CASCADE, db_index=True)
    value =  models.TextField('值', null=True)
    pub_date = models.DateTimeField('date published', auto_now=True)

    def __str__(self):
        return self.value