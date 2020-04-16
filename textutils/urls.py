"""textutils URL Configuration

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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # indexs this is function name created inside views.py
    path('', views.indexs, name='index1'),
    path('about1', views.abouts, name='about'),
    # if your path length is large then you can use name to access web
    path('contact1/', views.contacts, name='contact'),
    path('read1/', views.readFile, name='read'),
    path('read2/', views.readFile2, name='read22'),
    path('personalNavigator1', views.personalNavigator, name='pesonalNavigator'),
    path('removepunch', views.removePunch, name='removePunch'),
    path('capitalize', views.capitalize, name='capitalize'),
    path('newlineremove', views.newLineRemove, name='newlineremove'),
    path('spaceremove', views.spaceRemove, name='spaceremove'),
    path('charcounts', views.charCounts, name='charcounts'),
    path('templateload', views.templateLoad, name='templateload'),
    path('templateload2', views.templateLoad2, name='templateload2'),
    path('analyze', views.analyze, name='analyze'),
    path('textanalyzerhome', views.textAnalyzerHome, name='textanalyzerhome'),

]
