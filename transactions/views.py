import random
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
#from django.utils.http import is_safe_url


ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def transactions_view(request, *args, **kwargs):
    return render(request, "pages/transactions.html")

def transactions_list_view(request, *args, **kwargs):
    return render(request, "tweets/transacions_list.html")

def transactions_detail_view(request, tweet_id, *args, **kwargs):
    return render(request, "tweets/transactions_detail.html", context={"tweet_id": tweet_id})
