from django.urls import path
from . import views

urlpatterns = [
    path('', views.katalog, name='katalog'),
    path('kniha/<int:kniha_id>/', views.detail_knihy, name='detail_knihy'),
    path('vypujcky/', views.seznam_vypujcek, name='seznam_vypujcek'),
]