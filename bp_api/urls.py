"""
bp_api URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path
from rest_framework import serializers, viewsets, routers

urlpatterns = [
    path('admin/', admin.site.urls),
]
