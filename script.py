import folium

map = folium.Map(location = [45.372, -121.697], zoom_start = 3, tiles = "Stamen Terrain")
# .Map() creates a folium map object 
# location is cordinates
# zoom_start is zoom level min is 1
# tiles shows the map style

map.create_map(path = "test.html")

# .create_map() create a html file from map object
