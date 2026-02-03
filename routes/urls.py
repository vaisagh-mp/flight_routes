from django.urls import path
from .views import (
    home,
    add_airport,
    edit_airport,
    delete_airport,
    add_route,
    edit_route,
    delete_route,
    find_last_airport,
    route_statistics,
    
)

urlpatterns = [
    path('', home, name='home'),

    # Airports
    path('airport/add/', add_airport, name='add_airport'),
    path('airport/<int:pk>/edit/', edit_airport, name='edit_airport'),
    path('airport/<int:pk>/delete/', delete_airport, name='delete_airport'),

    # Routes
    path('route/add/', add_route, name='add_route'),
    path('route/<int:pk>/edit/', edit_route, name='edit_route'),
    path('route/<int:pk>/delete/', delete_route, name='delete_route'),

    path('search/', find_last_airport, name='search'),
    path('stats/', route_statistics, name='stats'),
]