def format_city_country(city, country, population = ''):
    """Generate a formated statement with city and country and population"""
    if population:
        city_country = f'{city}, {country} Population {population}'
    else:
        city_country = f'{city}, {country}'        
    return city_country.title()