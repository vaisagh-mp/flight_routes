from django.shortcuts import render, redirect
from django.db.models import Max, Min
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .models import Airport, AirportRoute
from .forms import AirportForm, AirportRouteForm, SearchRouteForm


def home(request):
    # Airports pagination
    airports = Airport.objects.order_by('-created_at')
    airport_paginator = Paginator(airports, 5)
    airport_page_number = request.GET.get('airport_page')
    airport_page_obj = airport_paginator.get_page(airport_page_number)

    latest_airports = airports[:4]

    # Routes pagination
    routes = AirportRoute.objects.select_related(
        'parent', 'child'
    ).order_by('-created_at')

    route_paginator = Paginator(routes, 5)
    route_page_number = request.GET.get('route_page')
    route_page_obj = route_paginator.get_page(route_page_number)

    return render(request, 'routes/home.html', {
        'latest_airports': latest_airports,
        'page_obj': airport_page_obj,      # airports
        'route_page_obj': route_page_obj,  # routes
    })

# CREATE Airport
def add_airport(request):
    form = AirportForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('add_airport')

    return render(request, 'routes/add_airport.html', {
        'form': form
    })


# EDIT AIRPORT
def edit_airport(request, pk):
    airport = get_object_or_404(Airport, pk=pk)
    form = AirportForm(request.POST or None, instance=airport)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'routes/edit_airport.html', {
        'form': form,
        'airport': airport
    })

# DELETE AIRPORT
def delete_airport(request, pk):
    airport = get_object_or_404(Airport, pk=pk)

    if request.method == "POST":
        airport.delete()
        return redirect('home')

    return redirect('home')


# Add Airport Route
def add_route(request):
    form = AirportRouteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('add_route')
    return render(request, 'routes/add_route.html', {'form': form})


# Edit Airport Route
def edit_route(request, pk):
    route = get_object_or_404(AirportRoute, pk=pk)
    form = AirportRouteForm(request.POST or None, instance=route)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'routes/edit_route.html', {
        'form': form,
        'route': route
    })


# Delete Airport Route
def delete_route(request, pk):
    route = get_object_or_404(AirportRoute, pk=pk)

    if request.method == "POST":
        route.delete()
        return redirect('home')

    return redirect('home')


# Find Last Reachable Airport
def find_last_airport(request):
    form = SearchRouteForm(request.POST or None)
    last_airport = None

    if form.is_valid():
        current_airport = form.cleaned_data['start_airport']
        direction = form.cleaned_data['direction']

        while True:
            route = AirportRoute.objects.filter(
                parent=current_airport,
                position=direction
            ).first()

            if not route:
                break

            current_airport = route.child

        last_airport = current_airport

    return render(request, 'routes/search_last_node.html', {
        'form': form,
        'last_airport': last_airport
    })


# Longest & Shortest Duration
def route_statistics(request):
    longest = AirportRoute.objects.order_by('-duration').first()
    shortest = AirportRoute.objects.order_by('duration').first()

    return render(request, 'routes/stats.html', {
        'longest': longest,
        'shortest': shortest
    })
