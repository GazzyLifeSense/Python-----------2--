a = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

for key in a.keys():
    print(f"a's {key} is {a[key]}")

# ---
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
}
for river in rivers.keys():
    print(f"The {river} runs through {rivers[river]}")
print(set(rivers.values()))

# ---
city_dict = {
    "a": {
        "country": "USA",
        "population": "1M"
    },
    "b": {
        "country": "US",
        "population": "2M"
    }
}

for city in city_dict:
    for key in city_dict[city]:
        print(f"{city}'s {key} is {city_dict[city][key]}")