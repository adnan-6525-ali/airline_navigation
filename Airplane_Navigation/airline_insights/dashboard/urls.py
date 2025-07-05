from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('autocomplete-airport/', views.autocomplete_airport, name='autocomplete-airport'),
]