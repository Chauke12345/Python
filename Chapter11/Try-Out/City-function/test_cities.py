from city_functions import city_country

def test_city_country():
    """Test that city_country() returns the correct string."""
    formatted = city_country('santiago', 'chile')
    assert formatted == 'Santiago, Chile'

def city_country(city, country, population=None):
    """Return a string formatted as 'City, Country', optionally with population."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"
    

def test_city_country_population():
    """Test city, country, and population."""
    formatted = city_country('santiago', 'chile', population=5000000)
    assert formatted == 'Santiago, Chile - population 5000000'