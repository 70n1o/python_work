def get_city_country(city, country, population=''):
    """Return formatted city, country pair."""
    if population:
        city_country = f"{city}, {country} - population {population}"
    else:
        city_country = f"{city}, {country}"

    return city_country.title()