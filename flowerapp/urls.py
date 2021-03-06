"""flowerapp URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from flowerapp import views as rootviews
from flowerapp.moviesapp import views as moviesviews
from flowerapp.airbnbapp import views as airbnbviews

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', rootviews.main),
    url(r'^browsemovies', moviesviews.browse),
    url(r'^browseproperties', airbnbviews.browse),
    url(r'^moviesflower', moviesviews.flower),
    url(r'^loadairbnbflower', airbnbviews.flower),
    url(r'^loadbarchart', airbnbviews.barchart),
    url(r'^regenerate', airbnbviews.regenerate)
]
