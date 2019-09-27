from django.contrib import admin

# Register your models here.
from .models import Project, Table, Column, ProjectTable

class TableAdmin(admin.ModelAdmin):
    list_display = ('table_name', 'table_row', 'pub_date')  # list

class TagInline(admin.TabularInline):
    model = ProjectTable

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'user', 'pub_date')  # list
    inlines = [TagInline]

class ColumnAdmin(admin.ModelAdmin):
    list_display = ('column_name', 'table', 'column_index', 'must', 'pub_date')  # list

class ProjectTableAdmin(admin.ModelAdmin):
    list_display = ('project', 'table')  # list

admin.site.register(Table, TableAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(ProjectTable, ProjectTableAdmin)
admin.site.site_header = '我的管理系统'
admin.site.site_title = '站点管理'