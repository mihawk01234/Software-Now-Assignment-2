#calculate average temperature for each season
def calculate_seasonal_average(season_temps):
    averages = {}
    for season in ["Summer", "Autumn", "Winter", "Spring"]:
        temps = season_temps.get(season, [])
        averages[season] = sum(temps) / len(temps) if temps else None
    return averages


def save_seasonal_average(averages, filename="average_temp.txt"):
   #save seasonal averages to a text file
    with open(filename, "w") as f:
        for season in ["Summer", "Autumn", "Winter", "Spring"]:
            f.write(f"{season}: {averages[season]:.1f}°C\n")