from django.shortcuts import render
from django.http import JsonResponse
from .utils.airport_loader import load_airports
from .utils.api_client import fetch_flight_data  # Assuming this is already present
from .utils.data_processor import get_insights   # Assuming this is already present

def home(request):
    selected_airport = request.GET.get("airport")
    insights = []

    if selected_airport:
        arrival_code = selected_airport.split(" - ")[0]
        data = fetch_flight_data(arrival_code)
        insights = get_insights(data)

    return render(request, "home.html", {"insights": insights})

def autocomplete_airport(request):
    query = request.GET.get('q', '').lower()
    airport_data = load_airports()

    filtered = [
        {
            'label': f"{airport['name']} - {airport['iata']}",
            'value': f"{airport['iata']} - {airport['name']}"
        }
        for airport in airport_data
        if query in airport['name'].lower() or query in airport['iata'].lower()
    ][:20]  # Limit to 20 results

    return JsonResponse(filtered, safe=False)
