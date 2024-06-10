from geopy.geocoders import Nominatim

def get_states_from_cities(cities):
    geolocator = Nominatim(user_agent="city_to_state")
    states = []
    for city in cities:
        location = geolocator.geocode(city, addressdetails=True)
        if location:
            address = location.raw.get('address')
            if address:
                state = address.get('state')
                if state:
                    states.append(state)
                else:
                    states.append("State information not found")
            else:
                states.append("Address information not found")
        else:
            states.append("City not found or error occurred")
    return states

# Example usage:
cities = ["New York", "Los Angeles", "Chicago", "Houston"]
states = get_states_from_cities(cities)
for city, state in zip(cities, states):
    print(f"The state for {city} is {state}")
