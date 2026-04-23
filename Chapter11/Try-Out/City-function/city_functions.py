def city_country(city, country):
    """Return a string formatted as 'City, Country'."""
    return f"{city.title()}, {country.title()}"

def city_country(city, country, population):
    """Return a string including population."""
    return f"{city.title()}, {country.title()} - population {population}"
