from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
# your views here
from . import APP_NAME


@login_required(login_url=reverse_lazy('account_login'))
def index(request):
    if request.user.group_list_all():
        return HttpResponseRedirect(
            reverse_lazy('group_detail', kwargs={'slug': request.user.group_list_all().first().slug}))
    else:
        return HttpResponseRedirect(reverse_lazy('group_list'))
