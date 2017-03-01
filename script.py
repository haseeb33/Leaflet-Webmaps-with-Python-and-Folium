import folium

map = folium.Map(location = [31.471132, 74.260050], zoom_start = 3, tiles = "Stamen Terrain")
# .Map() creates a folium map object 
# location is cordinates
# zoom_start is zoom level min is 1
# tiles shows the map style

map.simple_marker(location = [31.469935, 74.260096], popup = "Zam Zam Tower", marker_color = "red", popup_width = 500)
#Adding marker for a location

map.create_map(path = "test.html")

# .create_map() create a html file from map object
