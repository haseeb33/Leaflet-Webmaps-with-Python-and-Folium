import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt")
# Reading all the valcanoes info and saving it a df

map = folium.Map(location = [42.879902, -113.221001], zoom_start = 2.5, tiles = "Stamen Terrain")
# .Map() creates a folium map object 
# location is cordinates
# zoom_start is zoom level min is 1
# tiles shows the map style

for lat, lon, name in zip(df["LAT"], df["LON"], df["NAME"]):
    #Adding all the markers
    map.simple_marker(location = [lat, lon], popup = name, marker_color = "red")


map.create_map(path = "test.html")
# .create_map() create a html file from map object
