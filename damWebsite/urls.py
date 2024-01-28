from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('SearchAsset',views.SearchAsset, name='SearchAsset'),
    path('Assets',views.SearchAsset,name='Assets')
    ]