#finds the most stable and variable stations
import math

def std_dev(values):
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return math.sqrt(variance)


def find_temperature_stability(station_temps):
    stds = [(s, std_dev(t)) for s, t in station_temps.items()]

    min_sd = min(x[1] for x in stds)
    max_sd = max(x[1] for x in stds)

    most_stable = [x for x in stds if x[1] == min_sd]
    most_variable = [x for x in stds if x[1] == max_sd]

    return most_stable, most_variable


def save_temperature_stability(stable, variable, filename="temperature_stability_stations.txt"):
    with open(filename, "w") as f:
        for s, sd in stable:
            f.write(f"Most Stable: {s}: StdDev {sd:.1f}°C\n")
        for s, sd in variable:
            f.write(f"Most Variable: {s}: StdDev {sd:.1f}°C\n")