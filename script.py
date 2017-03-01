import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt")
# Reading all the valcanoes info and saving it a df

map = folium.Map(location = [df["LAT"].mean(), df["LON"].mean()], zoom_start = 4, tiles = "Mapbox bright")
map.add_child(folium.TileLayer(tiles = "OpenStreetMap"))
map.add_child(folium.TileLayer(tiles = "mapquestopen"))
# .Map() creates a folium map object 
# location is cordinates
# zoom_start is zoom level min is 1
# tiles shows the map style
feature_group = folium.FeatureGroup("Volcano Locations")
#Creating a feature group to add it in layer control

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
        
    feature_group.add_child(folium.Marker(location = [lat, lon], popup = name, icon = folium.Icon(color = color)))
    
map.add_child(feature_group)

map.add_child(folium.GeoJson(data = open("World-population.geojson"),
     name = "World Population",
     style_function = lambda x: {"fillColor": "green" if x["properties"]["POP2005"] <= 10000000 else "orange" if 10000000 < x["properties"]["POP2005"] < 20000000 else "red"}))
#Adding a Choropleth Map from GeoJson

map.add_child(folium.LayerControl())
map.save(outfile = "test.html")
# .create_map() create a html file from map object
