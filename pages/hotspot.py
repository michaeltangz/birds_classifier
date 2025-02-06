# import streamlit as st
# import pandas as pd
# import numpy as np
# import pickle
# import torch
# import urllib.request
# from PIL import Image
# from transformers import pipeline
# import requests
# import geemap
# from streamlit_folium import st_folium
# from streamlit_geolocation import streamlit_geolocation
# import geemap.foliumap as geemap
# import geopandas as gpd
# from shapely.geometry import Point
# import ipywidgets as widgets

# lat = 172.5837443
# lon = -43.5053818
# url = f"https://api.ebird.org/v2/ref/hotspot/geo?lat={lat}&lng={lon}"

# payload = {}
# headers = {
#     'X-eBirdApiToken': 'aqf69iukjcqs'  # Replace 'YOUR_API_KEY' with your actual eBird API key
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# # Example data

# # data = response.text
# # # Split the data into lines
# # lines = data.strip().split('\n')



# # # Extract coordinates from each line
# # coordinates = []
# # for line in lines:
# #     parts = line.split(',')
# #     latitude = float(parts[4])
# #     longitude = float(parts[5])
# #     coordinates.append((latitude, longitude))

# # # Create a GeoDataFrame
# # gdf = gpd.GeoDataFrame(geometry=gpd.points_from_xy([lon for lat, lon in coordinates], [lat for lat, lon in coordinates]))



# # center = (lat, lon)

# # center_point = Point(center)

# # gdf['distance'] = gdf.distance(center_point)

# # # Set the CRS to WGS84 (EPSG:4326) before transforming
# # gdf.set_crs(epsg=4326, inplace=True)
# # gdf.to_crs(epsg=4326, inplace=True)

# # gdf['distance'] = gdf.distance(center_point)

# # # Find the nearest points
# # nearest_points = gdf.nsmallest(5, 'distance')  # Adjust the number of nearest points as needed

# # # Print the nearest points
# # import folium

# # m = folium.Map(location=[lon, lat], zoom_start=12)

# # folium.Marker(
# #     [lon, lat], 
# #     popup="Current Location", 
# #     icon=folium.Icon(color='red')  # Set marker color
# # ).add_to(m)


# # m.to_streamlit(width=800, height=600)

# url = f"https://api.ebird.org/v2/ref/hotspot/geo?lat={lon}&lng={lat}"

# payload = {}
# headers = {
#     'X-eBirdApiToken': 'aqf69iukjcqs'  # Replace 'YOUR_API_KEY' with your actual eBird API key
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# # Example data
# data = response.text

# # Split the data into lines
# lines = data.strip().split('\n')

# # Extract coordinates from each line
# coordinates = []
# for line in lines:
#     try:
#         parts = line.split(',')
#         latitude = float(parts[4])
#         longitude = float(parts[5])
#         coordinates.append((latitude, longitude))
#     except (IndexError, ValueError) as e:
#         print(f"Error processing line: {line}")
#         print(f"Error: {e}")

# try:
#     # Create a GeoDataFrame
#     gdf = gpd.GeoDataFrame(geometry=gpd.points_from_xy([lon for lat, lon in coordinates], [lat for lat, lon in coordinates]))

#     center = (lat, lon)
#     center_point = Point(center)

#     gdf['distance'] = gdf.distance(center_point)

#     # Set the CRS to WGS84 (EPSG:4326) before transforming
#     gdf.set_crs(epsg=4326, inplace=True)
#     gdf.to_crs(epsg=4326, inplace=True)

#     gdf['distance'] = gdf.distance(center_point)

#     # Find the nearest points
#     nearest_points = gdf.nsmallest(5, 'distance')  # Adjust the number of nearest points as needed

#     # Print the nearest points
#     print(nearest_points)

#     # Create a map centered at the current locationm = folium.Map(location=[lon, lat], zoom_start=12)

#     # Add markers for the nearest points

# st.write(lines)


# # Print the nearest points
# # Print the nearest points
# import folium
# import streamlit as st
# from streamlit_folium import st_folium

# m = folium.Map(location=[lon, lat], zoom_start=12)

# folium.Marker(
#     [lon, lat], 
#     popup="Current Location", 
#     icon=folium.Icon(color='red')  # Set marker color
# ).add_to(m)

# # Display the map in Streamlit
# st_folium(m, width=800, height=600)


import requests
import geopandas as gpd
from shapely.geometry import Point
import folium
import streamlit as st
from streamlit_folium import st_folium
from streamlit_geolocation import streamlit_geolocation



st.title("Bird Observation Hotspot Finder")
st.write("This page will find the best 5 bird ovbservation hotspots near you")

# Get the current location
location = streamlit_geolocation()

lat, lon = location["latitude"], location["longitude"]

# lon = 172.5837443
# lat = -43.5053818
url = f"https://api.ebird.org/v2/ref/hotspot/geo?lat={lat}&lng={lon}"



payload = {}
headers = {
    'X-eBirdApiToken': 'aqf69iukjcqs'  # Replace 'YOUR_API_KEY' with your actual eBird API key
}

response = requests.request("GET", url, headers=headers, data=payload)
#st.write(response.text)

data = response.text
# Split the data into lines
lines = data.strip().split('\n')

# Extract coordinates from each line
coordinates = []
locations = []
for line in lines:
    parts = line.split(',')
    latitude = float(parts[4])
    longitude = float(parts[5])
    coordinates.append((latitude, longitude))
    locations.append(parts[6])

#st.write(coordinates)
#st.write(locations)

# Create a GeoDataFrame
gdf = gpd.GeoDataFrame(geometry=gpd.points_from_xy([lon for lat, lon in coordinates], [lat for lat, lon in coordinates]))

# add the location name into gdf
gdf['location'] = locations

center = (lon,lat)

center_point = Point(center)

gdf['distance'] = gdf.distance(center_point)

# Set the CRS to WGS84 (EPSG:4326) before transforming

gdf.set_crs(epsg=4326, inplace=True)
gdf.to_crs(epsg=4326, inplace=True)

gdf['distance'] = gdf.distance(center_point)

# Find the nearest points
nearest_points = gdf.nsmallest(5, 'distance')  # Adjust the number of nearest points as needed

#st.write(nearest_points)

m = folium.Map(location=[lat, lon], zoom_start=12)

folium.Marker(
    [lat, lon], 
    popup="Current Location", 
    icon=folium.Icon(color='red')  # Set marker color
).add_to(m)

# plot the nearest points
for idx, row in nearest_points.iterrows():
    folium.Marker(
        location=[row.geometry.y, row.geometry.x],
        popup=f"{row['location'].split('-')[-1]}",
        icon=folium.Icon(color='blue')
    ).add_to(m)

# Display the map in Streamlit
st_folium(m, width=600, height=400)


