# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.gis.measure import D
import json
from django.http import HttpResponse

#from django.http import Http404
from django.shortcuts import get_object_or_404, render, render_to_response
#import folium
#import pandas as pd
from django.contrib.gis.geos import GEOSGeometry, Point
from .models import *

from django.template.loader import render_to_string


from pyproj import Proj, transform

# TODO faire le ménage

# Create your views here.

# index view : la page index affiche les différents projets. Par un click les projets sont visibles

def index(request):

    projects = Project.objects.order_by('code')[:100]


    context = {
        'projects': projects,
        'content': render_to_string('BestApp/projects_list.html', {'projects': projects}),
    }
    return render_to_response ('BestApp/index.html',context)


def project_detail(request, id):

    project = get_object_or_404(Project, pk=id)
    #outputs = get_object_or_404(Output, project_id=project_id)
    outputs = Output.objects.filter(project_id = id)
    #outputs = get_object_or_404(Output, project_id=id)

    #nb_outputs = outputs.count()
    #tab_activities = [nb_outputs]
    #i=0
    #for output in outputs:
        #tab_activities[i]= list(Activity.objects.filter( output_id = output.id))
        #i = i + 1
    context = {
        'project': project,
        'outputs_html' : render_to_string('BestApp/outputs_list.html',{
            'outputs':outputs,
            #'activities_html' : render_to_string('BestApp/activities_list.html',{'tab_activities':tab_activities}),
            #'tab_activities' : tab_activities,
            }),
        }
    return render_to_response('BestApp/project_detail.html',context)


def outputs_list(request, project_id):
    outputs = Output.objects.filter(project_id= project_id)
    context = {'outputs': outputs}
    return render_to_response('BestApp/outputs_list.html', context)


def activities_list(request, output_id):
    activities = Activity.objects.filter(output_id=output_id)
    context = {'activities': activities}
    return render_to_response('BestApp/activities_list.html', context)

    #try :
    #project = Project.objects.get(pk=project_id)

    #except Project.DoesNotExist:
    #    raise Http404("the project does no exist")
    #project = get_object_or_404(Project, pk=project_id)
    #name_map = {'latitude': 'x', 'longitude': 'y'}
    #sql = "SELECT st_x(geom) as x,st_y(geom) as y FROM \"BestApp_project\""
    #sql = 'le mot "magique" '



    #project = Project.objects.filter(Project.geom__dwithin=(Project.geom, D(m=100)))
    #point = Column(Geometry('Point'))
    #project = get_object_or_404(Project, pk=project_id)
    #point = GEOSGeometry(project.geom)
    #coordinates = json.loads(point.json)
    #if coordinates['coordinates']:
    #    inProj = Proj(init='epsg:3857')
    #    outProj = Proj(init='epsg:4326')
    #    x1, y1 = coordinates['coordinates'][1], coordinates['coordinates'][0]
    #    latitude, longitude = transform(inProj, outProj, x1, y1)
    #latitude = coordinates['coordinates'][1]
    #longitude = coordinates['coordinates'][0]
    #else:
    #    latitude, longitude = None, None

    #return [coordinates[1], coordinates[0]]
    #projectPoint = Project.objects.raw(sql, name_map)
    #point = projectPoint.
    #project = Project.objects.raw('SELECT * FROM BestApp_project')
    #point = project.objects.__str__()
    #doc = GEOSGeometry(project.geom.__str__())

    #point = doc.coord_seq
    #point = doc.kml.__str__()

    #point = doc.json

    #map_osm = folium.Map(location=point.tuple)
    #map_osm.save("BestApp//templates/BestApp/map.html")
    #display(map)
    #return render(request, 'BestApp/project_detail.html',{'project': project,'latitude': latitude, 'longitude': longitude, 'coordinates':coordinates, })