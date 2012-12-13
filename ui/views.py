# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext, Template
from django.shortcuts import render_to_response

from models import *

import datetime
import json, yaml

def getInp(request, fld, default=None):
    if request.method == 'GET':
        qd = request.GET
    elif request.method == 'POST':
        qd = request.POST
    return qd.get(fld, default)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "It is now %s" % now
    return HttpResponse(html)

######### Static pages ###########################

def getRobots(request):
    robots = ["User-agent: *","Disallow: "]
    return HttpResponse("\r\n".join(robots))


def getHome(request):
    context = {}
    return render_to_response("index.html", \
                               context, \
                               context_instance=RequestContext(request))

