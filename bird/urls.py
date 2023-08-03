from django.urls import path
from .views import *


urlpatterns = [
    path('add/', add_bird, name='add_bird'),
    path('birds/', bird_list, name='bird_list'),
    path('bird/<int:id>/', one_bird, name='one_bird'),
    path('bird/<int:id>/increment/', increment_sightings, name='increment_sightings'),
    path('', main)
]