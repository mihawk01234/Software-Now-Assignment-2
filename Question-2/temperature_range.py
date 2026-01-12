#finds station with the largest temp range
def find_largest_temp_range(station_temps):
    results = []

    for station, temps in station_temps.items():
        max_t = max(temps)
        min_t = min(temps)
        rng = max_t - min_t
        results.append((station, rng, max_t, min_t))

    max_range = max(r[1] for r in results)
    #return all stations with same largest range
    return [r for r in results if r[1] == max_range]


def save_largest_temp_range(winners, filename="largest_temp_range_station.txt"):
    with open(filename, "w") as f:
        for st, rng, mx, mn in winners:
            f.write(f"{st}: Range {rng:.1f}°C (Max: {mx:.1f}°C, Min: {mn:.1f}°C)\n")