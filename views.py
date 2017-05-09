from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
# your views here
from . import APP_NAME


def index(request):
        return render(request, template_name="%s/index.html" % APP_NAME, context={'message':'Hello from %s'% APP_NAME,'app_name':APP_NAME})
