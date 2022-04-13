def city_country(city, country):
    return f"{city.title()}, {country.title()}"


city_to_visit_1 = city_country("tokyo", "japan")
city_to_visit_2 = city_country("st. andrews", "scotland")
city_to_visit_3 = city_country("munich", "germany")

print(city_to_visit_1)
print(city_to_visit_2)
print(city_to_visit_3)
