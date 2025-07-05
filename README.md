# airline_navigation
This Project is to get the popular routes from that airport

Features :-
Autocomplete Search: Start typing an airport code (e.g., BLR), and the app suggests matching airports like Kempegowda International Airport - BLR.

Popular Routes View: On selecting an airport, view the most popular routes from that airport.

Extendable Airport Data: If a specific airport is missing, you can add it to the data source.



# Missing an Airport?
If the airport name/code is not appearing in the suggestion:

Open the file:
- Airplane_Navigation/airline_insights/dashboard/data/airports.dat
- Append your new airport data in the same format as existing entries.



#  How to Use
Start the server:

python manage.py runserver
Open in browser:

http://127.0.0.1:8000/
Search by airport code (e.g., BLR, BOM) in the input field.



# -----> API Usage
This project uses a third-party API to retrieve popular route data for airports. You can use the existing API provided in the project, or register for your own if needed.

API Provider: AviationStack (or other open/free APIs depending on your implementation)

Endpoint Example:
https://api.aviationstack.com/v1/routes?access_key=YOUR_API_KEY&iata_code=BLR

# Get Your Own API Key
If you'd like to use your own API key:

Go to the API provider's website. Example:

AviationStack

Sign up for a free account.

Create a new app or subscribe to the API plan (free or paid).

Get your API key from your dashboard.

