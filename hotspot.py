import streamlit as st
import pandas as pd
import numpy as np
import pickle
import torch
import urllib.request
from PIL import Image
from transformers import pipeline
import requests
import geemap
from streamlit_folium import st_folium
from streamlit_geolocation import streamlit_geolocation
import geemap.foliumap as geemap
import geopandas as gpd
from shapely.geometry import Point
import ipywidgets as widgets


url = f"https://api.ebird.org/v2/ref/hotspot/geo?lat={lat}&lng={lng}"

payload = {}
headers = {
    'X-eBirdApiToken': 'aqf69iukjcqs'  # Replace 'YOUR_API_KEY' with your actual eBird API key
}

response = requests.request("GET", url, headers=headers, data=payload)

# Example data

data = response.text
# Split the data into lines
lines = data.strip().split('\n')

# Extract coordinates from each line
coordinates = []
for line in lines:
    parts = line.split(',')
    latitude = float(parts[4])
    longitude = float(parts[5])
    coordinates.append((latitude, longitude))

# Create a GeoDataFrame
gdf = gpd.GeoDataFrame(geometry=gpd.points_from_xy([lon for lat, lon in coordinates], [lat for lat, lon in coordinates]))

center = (lat, lon)

center_point = Point(center)

gdf['distance'] = gdf.distance(center_point)

# Set the CRS to WGS84 (EPSG:4326) before transforming
gdf.set_crs(epsg=4326, inplace=True)
gdf.to_crs(epsg=4326, inplace=True)

gdf['distance'] = gdf.distance(center_point)

# Find the nearest points
nearest_points = gdf.nsmallest(5, 'distance')  # Adjust the number of nearest points as needed

# Print the nearest points
print(nearest_points)

Map = geemap.Map(center=(lon,lat), zoom=12)
popup = widgets.HTML(value="Your Location")
Map.add_marker(location=(lon,lat), popup=popup, name="Current Location")
Map.add_gdf(nearest_points, "Nearest Hotspots")

Map.to_streamlit(width=800, height=600)