from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('maps', views.maps, name='maps'),
    path('maps_detail/<str:name>', views.maps_detail, name='maps_detail'),
    path('npc', views.npc, name='npc'),
    path('npc_detail/<str:name>', views.npc_detail, name='npc_detail'),
]
