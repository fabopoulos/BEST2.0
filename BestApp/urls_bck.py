from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project_detail/<int:id>/', views.project_detail, name='project_detail'),
    path('outputs_list/<int:project_id>/', views.outputs_list, name='outputs_list'),
    path('activities_list/<int:output_id>/', views.activities_list, name='activities_list'),
]
