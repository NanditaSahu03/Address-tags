from geopy.geocoders import Nominatim
import folium
nom = Nominatim()

a = input("enter a region:")
n = nom.geocode(a)
lat = n.latitude
lon = n.longitude
map = folium.Map(location=[lat,lon])
map.add_child(folium.Marker(location=[22.0506,88.0722],popup="The place(HALDIA INSTITUTE OF TECHNOLOGY) where i met you first time(clg) and got u as my friend",icon=folium.Icon(color="blue")))
map.add_child(folium.Marker(location=[22.051193,88.064319],popup="The place(KHUDIRAM MARKET) where i usually go.. praying to god that by conincident i can see u there eating golgappas and give company to u",icon=folium.Icon(color="red")))
map.add_child(folium.Marker(location=[22.051868,88.071250],popup="The place(CLG LIBRARY) where i taught u to hack fb account and where i have seen ur ex..s  pics.....the place where u told me that me to get out of ur life because u are frustrated of me ",icon=folium.Icon(color="red")))
map.add_child(folium.Marker(location=[22.049240,88.069605],popup="The place(CLG ROAD)where i use to go with u in cc for movie ...great memories i have in this road...the place where i always stare sitting beside some thek when u return to your home or go to clg",icon=folium.Icon(color="red")))
map.add_child(folium.Marker(location=[22.049966,88.067202],popup="The place(THEK)where i drank tea with u first time when u came near balaji to take BABA...s cake",icon=folium.Icon(color="blue")))
map.add_child(folium.Marker(location=[22.050631,88.073382],popup="The place (GARDEN) where after riveria we went together having dinner just because you were angry with ur roomies ",icon=folium.Icon(color="blue")))
map.add_child(folium.Marker(location=[22.048106,88.065592],popup="The place (BR) where u called me up once and told me to come near the gate as u are near BR for dhurwa club and i was waiting for u for 15 min ",icon=folium.Icon(color="red")))
map.add_child(folium.Marker(location=[22.059653,88.075432],popup="The place (CC) where i requested DIYANK,BISWAJEET,NAVEEN to hide somewhere in cc so that u come comforatbly in theatre ....the place where u were feeling very shy when MOHIT, u, ABHINAV and I met for dinner DURING DIWALI ",icon=folium.Icon(color="red")))
map.save("newss.html")

  


