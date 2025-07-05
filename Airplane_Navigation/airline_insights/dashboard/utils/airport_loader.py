import csv
import os

def load_airports():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '..', 'data', 'airports.dat')

    airports = []
    with open(file_path, encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 5:
                iata_code = row[4].strip('"')
                name = row[1].strip('"')
                city = row[2].strip('"')
                country = row[3].strip('"')

                # Skip entries with no IATA code
                if iata_code and iata_code != "\\N":
                    airports.append({
                        "name": name,
                        "city": city,
                        "country": country,
                        "iata": iata_code,
                        "label": f"{iata_code} - {name} ({city}, {country})"
                    })

    return airports
