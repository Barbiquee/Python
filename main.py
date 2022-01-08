def random_country():
    countries = {}
    continents = []
    capitals = []
    with open('text.txt', 'r') as file:
        content = file.readlines()
    for line in content:
        country, capital, continent = line.lower().split()
        try:
            countries[continent].append(country)
        except KeyError:
            countries[continent] = []
            countries[continent].append(country)
    return countries

print(random_country())