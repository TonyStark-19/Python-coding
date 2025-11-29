# This program create a Python dictionary of 3 cities and their populations.

# import json module
import json

# Create a dictionary and save it to cities.json
cities = {
    "Delhi": 19000000,
    "Mumbai": 21000000,
    "Bangalore": 12000000
}

# Save dictionary to JSON file
with open("Working with Json/cities.json", "w") as f:
    json.dump(cities, f, indent=4)

# Load JSON and print each city with population
with open("Working with Json/cities.json", "r") as f:
    data = json.load(f)

print("\nCurrent Cities and Populations:")
for city, population in data.items():
    print(f"{city}: {population}")

# Ask user for new city & its population
new_city = input("\nEnter a new city name: ")
new_population = int(input("Enter its population: "))

# Update dictionary
data[new_city] = new_population

# Save updated data back to JSON
with open("Working with Json/cities.json", "w") as f:
    json.dump(data, f, indent=4)

print("\nCity added successfully!")
print("Updated cities data saved to cities.json")