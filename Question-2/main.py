#main program that runs all analyses for question-2
from reader import load_temperature_data
from seasonal_average import calculate_seasonal_average, save_seasonal_average
from temperature_range import find_largest_temp_range, save_largest_temp_range
from temperature_stability import find_temperature_stability, save_temperature_stability

def main():
    station_temps, season_temps = load_temperature_data("temperatures")

    averages = calculate_seasonal_average(season_temps)
    save_seasonal_average(averages)

    ranges = find_largest_temp_range(station_temps)
    save_largest_temp_range(ranges)

    stable, variable = find_temperature_stability(station_temps)
    save_temperature_stability(stable, variable)

    print("Analysis complete. Output files generated.")

if __name__ == "__main__":
    main()