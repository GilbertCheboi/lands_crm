"""tweetme2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include # url()
from django.views.generic import TemplateView

# from accounts.views import RegisterAPI
# from knox import views as knox_views
# from accounts.views import LoginAPI
# from django.urls import path



from bookings.views import (
    bookings_view,
    bookings_list_view,
    bookings_detail_view,
)

from clients.views import (
    clients_view,
    clients_list_view,
    clients_detail_view,
)
from clients_documents.views import (
    clients_documents_view,
    clients_documents_list_view,
    clients_documents_detail_view,
)
from leads.views import (
    leads_view,
    leads_list_view,
    leads_detail_view,
)
from meetings.views import (
    meetings_view,
    meetings_list_view,
    meetings_detail_view,
)
from schedules.views import (
    schedules_view,
    schedules_list_view,
    schedules_detail_view,
)
from tasks.views import (
    tasks_view,
    tasks_list_view,
    tasks_detail_view,
)
from transactions.views import (
    transactions_view,
    transactions_list_view,
    transactions_detail_view,
)





urlpatterns = [
    #path('api/', include('accounts.urls')),
    
    path('bookings/', bookings_view),
    path('clients/', clients_view),
    path('clients_documents/', clients_documents_view),
    path('leads/', leads_view),
    path('meetings/', meetings_view),
    path('schedules/', schedules_view),
    path('transactions/', transactions_view),
    path('tasks/', tasks_view),
    path('admin/', admin.site.urls),
    path('react/', TemplateView.as_view(template_name='react.html')),
    path('bookings/<int:tweet_id>/', bookings_detail_view),
    path('clients/<int:tweet_id>/', clients_detail_view),
    path('clients_documents/<int:tweet_id>/', clients_documents_detail_view),
    path('leads/<int:tweet_id>/', leads_detail_view),
    path('meetings/<int:tweet_id>/', meetings_detail_view),
    path('schedules/<int:tweet_id>/', schedules_detail_view),
    path('tasks/<int:tweet_id>/', tasks_detail_view),
    path('transactions/<int:tweet_id>/', transactions_detail_view),
    re_path(r'profiles?/', include('profiles.urls')),
    path('api/bookings/', include('bookings.api.urls')),
    path('api/clients/', include('clients.api.urls')),
    path('api/clients_documents/', include('clients_documents.api.urls')),
    path('api/leads/', include('leads.api.urls')),
    path('api/meetings/', include('meetings.api.urls')),
    path('api/schedules/', include('schedules.api.urls')),
    path('api/accounts/', include('accounts.api.urls')),
    path('api/tasks/', include('tasks.api.urls')),
    path('api/transactions/', include('transactions.api.urls')),
    re_path(r'api/profiles?/', include('profiles.api.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, 
                document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, 
                document_root=settings.MEDIA_ROOT)