import random
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
#from django.utils.http import url_has_allowed_host_and_scheme


ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def tasks_view(request, *args, **kwargs):
    return render(request, "pages/tasks.html")

def tasks_list_view(request, *args, **kwargs):
    return render(request, "tweets/tasks.html")

def tasks_detail_view(request, tweet_id, *args, **kwargs):
    return render(request, "tweets/tasks_detail.html", context={"tweet_id": tweet_id})
#from django.shortcuts import render

# Create your views here.
