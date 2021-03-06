"""captains_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.generic import RedirectView
mapbox_access_token = settings.MAPBOX_KEY
from django.conf.urls.static import static
from .views import download_file




urlpatterns = [
    path('maps/', include('sitemaps.urls', namespace='sitemaps')),
    path('admin/', admin.site.urls),
    path('triplog/', include('triplog.urls')),
    re_path('media/routes', download_file, name='download_file')
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]


urlpatterns += [
    path('', RedirectView.as_view(url='/accounts/login/', permanent=True)),
]

#if 'rosetta' in settings.INSTALLED_APPS:
urlpatterns += [
    path('rosetta/', include('rosetta.urls'))
]

