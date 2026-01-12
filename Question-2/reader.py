#reads CSV files from temperature folder
import os
import csv
import math
from collections import defaultdict
#mapping months to australian seasons
MONTH_TO_SEASON = {
    "December": "Summer", "January": "Summer", "February": "Summer",
    "March": "Autumn", "April": "Autumn", "May": "Autumn",
    "June": "Winter", "July": "Winter", "August": "Winter",
    "September": "Spring", "October": "Spring", "November": "Spring"
}

MONTHS = list(MONTH_TO_SEASON.keys())

def load_temperature_data(folder="temperatures"):
    station_temps = defaultdict(list)
    season_temps = defaultdict(list)

    for filename in os.listdir(folder):
        if not filename.lower().endswith(".csv"):
            continue

        path = os.path.join(folder, filename)

        with open(path, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)

            for row in reader:
                station = row["STATION_NAME"].strip()

                for month in MONTHS:
                    value = row.get(month, "").strip()

                    if value == "" or value.lower() == "nan":
                        continue

                    temp = float(value)

                    station_temps[station].append(temp)

                    season = MONTH_TO_SEASON[month]
                    season_temps[season].append(temp)

    return station_temps, season_temps