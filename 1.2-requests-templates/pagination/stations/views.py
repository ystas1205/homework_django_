from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def reading_file(request):
    with open(BUS_STATION_CSV, 'r', encoding='utf-8', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        list_stations = [row for row in reader]
        return list_stations


def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    pagination = Paginator(reading_file(request), 10)
    page = pagination.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
