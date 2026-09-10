from django.urls import path
from . import views

urlpatterns = [
    path('npcs/', views.get_npcs, name='get_npcs'),
    path('all_locations/', views.get_all_locations, name='get_all_locations'),
]


