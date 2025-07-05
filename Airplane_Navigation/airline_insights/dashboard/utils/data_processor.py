import pandas as pd

def get_insights(flight_data):
    flat_data = []

    for item in flight_data:
        try:
            flat_data.append({
                'from': item['departure']['iata'],
                'to': item['arrival']['iata'],
                'airline': item['airline']['name'],
                'flight_no': item['flight']['iata']
            })
        except:
            continue

    df = pd.DataFrame(flat_data)

    if df.empty:
        return []

    popular_routes = df.groupby(['from', 'to']).size().reset_index(name='count')
    popular_routes = popular_routes.sort_values(by='count', ascending=False)

    return popular_routes.to_records(index=False)
