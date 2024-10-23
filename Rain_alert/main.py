import geocoder
from geopy.geocoders import Nominatim

def get_current_gps_coordinates():
    g = geocoder.ip('me')#this function is used to find the current information using our IP Add
    if g.latlng is not None: #g.latlng tells if the coordiates are found or not
        return g.latlng
    else:
        return None

def process_coordinates(coordinates, latitude, longitude):
        geo_location = Nominatim(user_agent="GetLoc")
        print(geo_location)
        location_name =  geo_location.reverse(f"{latitude}, {longitude}")
        print(location_name)


if __name__ == "__main__":
    coordinates = get_current_gps_coordinates()
    if coordinates is not None:
        latitude, longitude = coordinates
        print(f"Your current GPS coordinates are:")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
        process_coordinates(coordinates, latitude, longitude) 
    else:
        print("Unable to retrieve your GPS coordinates.")
    