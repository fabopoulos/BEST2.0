from django.conf.urls import url,re_path

from .views import ProjectList, OutputList, ProjectDetail, ProjectUpdate, OutputDetail, OutputUpdate
from . import views

urlpatterns = [
           url(r'^projects$',ProjectList.as_view(),name='projects_list'),
           url(r'^projects/(?P<project_pk>[0-9]+)$', ProjectDetail.as_view(),name='project_detail'),

           url(r'^outputs$', OutputList.as_view(), name='outputs_list'),
           url(r'^outputs/(?P<output_pk>[0-9]+)$', OutputDetail.as_view(), name='output_detail'),
           url(r'^$', views.index, name='index'),
           #path('', index, name='index'),
]