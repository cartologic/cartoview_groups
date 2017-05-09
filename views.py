from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
# your views here
from . import APP_NAME


@login_required(login_url=reverse('account_login'))
def index(request):
    return HttpResponseRedirect(reverse('group_detail', kwargs={'slug': request.user.group_list_all().first().slug}))
