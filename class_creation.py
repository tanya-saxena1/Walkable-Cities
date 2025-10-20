import json
import googlemaps
import random
import pandas as pd

api_key = ""
googlemapsSession = googlemaps.Client(api_key)

class City:
    def __init__(self, nameofcity):
        self.nameofcity = nameofcity
        self.outer_bounds = []

    def get_geocoding_data(self):
        geocoding_result = googlemapsSession.geocode(self.nameofcity)

        if geocoding_result:
            location = geocoding_result[0]['location']['geometry']
            viewport = geocoding_result[0]['viewport']['geometry']

            self.central_coordinates = (location['lat'], location['lng'])
            self.outer_bounds = [
                viewport['southwest']['lat'],
                viewport['southwest']['lng'],
                viewport['northeast']['lat'],
                viewport['northeast']['lng']
            ]

    def get_random_coordinates(self):
        lat = random.uniform(self.outer_bounds[0], self.outer_bounds[2])
        lng = random.uniform(self.outer_bounds[1], self.outer_bounds[3])
        return lat, lng

    def get_outer_bounds(self):
        places_result = googlemapsSession.places(self.nameofcity)
        city_bound_coords = places_result["geometry"]["viewport"]
        self.outer_bounds = [
            city_bound_coords["southwest"]["lat"],
            city_bound_coords["southwest"]["lng"],
            city_bound_coords["northeast"]["lat"],
            city_bound_coords["northeast"]["lng"]
        ]

class blocks_1km:
    def __init__(self, outer_coords):
        self.central_lat = random.uniform(outer_coords[1][0], outer_coords[0][0])
        self.central_lng = random.uniform(outer_coords[1][1], outer_coords[0][1])
        self.params: list = None
    def parameterize(self, something):
        pass

class WorldCitiesLine:
    def __init__(self, line):
        pre_list = line.strip().split(',')
        try:
            self.country = pre_list[0]
            self.capital = pre_list[1]
            self.latitude = float(pre_list[2])
            self.longitude = float(pre_list[3])
        except IndexError:
            pass

def save_to_dataframe(city_list):
    data = [{"name": city.nameofcity, "coordinates": city.get_random_coordinates()} for city in city_list]
    df = pd.DataFrame(data)
    return df

def main():
    list_of_cities = []
    with open("cities.csv") as file:
        for line in file:
            city = WorldCitiesLine(line)
            if hasattr(city, 'latitude') and hasattr(city, 'longitude'):
                city_instance = City(city.capital)
                city_instance.get_geocoding_data()
                list_of_cities.append(city_instance)

    for city in list_of_cities:
        city.get_outer_bounds()

    df = save_to_dataframe(list_of_cities)
    df.to_json("training_data.json", orient="records", lines=True)

if __name__ == "__main__":

    main()
