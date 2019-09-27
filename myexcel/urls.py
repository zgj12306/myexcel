from django.urls import path
from . import views, admin_views

app_name = 'myexcel'
urlpatterns = [
    # path('', admin_views.login, name='login'),
    # path('admin/myexcel/project/', admin_views.change_list, name='project'),
    path('', views.project, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/excel/', views.excel, name='excel'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]