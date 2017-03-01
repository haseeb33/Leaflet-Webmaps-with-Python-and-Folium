import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt")
# Reading all the valcanoes info and saving it a df

map = folium.Map(location = [df["LAT"].mean(), df["LON"].mean()], zoom_start = 4, tiles = "Stamen Terrain")
# .Map() creates a folium map object 
# location is cordinates
# zoom_start is zoom level min is 1
# tiles shows the map style

for lat, lon, name, elev in zip(df["LAT"], df["LON"], df["NAME"], df["ELEV"]):
    #Adding all the markers
    color = "blue"
    mini = int(min(df["ELEV"]))
    step = int((max(df["ELEV"]) - min(df["ELEV"]))/3)
    
    if elev in range(mini, mini + step):
        color = "green"
    elif elev in range(mini + step, mini + step*2):
        color = "orange"
    else:
        color = "red"
        
    map.simple_marker(location = [lat, lon], popup = name, marker_color = color)


map.create_map(path = "test.html")
# .create_map() create a html file from map object
