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

st.title("Welcome to Bird Identification and Bird Observation Hotspot Finder")
st.write("This page will help you identify bird species and find the best nearest bird ovbservation hotspots")
st.write("please upload the image file of bird to identify the species")

# Create a file image uploader
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Open the image using PIL
    img = Image.open(uploaded_file)

    # Display the uploaded image
    st.image(img, caption='Uploaded Image.',  use_container_width=False, width=500)
    st.write("")
    st.write("⌛ Classifying......")

    # Loading the model and preprocessor using Pipeline
    pipe = pipeline("image-classification", model="dennisjooo/Birds-Classifier-EfficientNetB2")

    # Running the inference
    result = pipe(img)[0]

    # Displaying the result label
    st.write(f"**Prediction: {result['label']}**")

# import pipeline model
# Load model directly
# Load model directly
# Use a pipeline as a high-level helper
#from transformers import pipeline

label = result['label']


def convert_label(label):
    return label.replace(" ", " ").lower()

import requests

# Define the endpoint
endpoint = "https://en.wikipedia.org/w/api.php"

# Define the parameters
params = {
    "action": "query",
    "format": "json",
    "titles": f"{convert_label(label)}",
    "prop": "extracts|pageimages",
    "exintro": True,
    "explaintext": True,
    "pithumbsize": 500
}

# Make the request
response = requests.get(endpoint, params=params)

# Parse the response
data = response.json()

# Extract the page content
page = next(iter(data['query']['pages'].values()))
extract = page.get('extract', 'No extract available')
thumbnail = page.get('thumbnail', {}).get('source', None)
# Display the image if available
if thumbnail:
    st.image(thumbnail)

st.write(f"🐤 **Discription:** {extract}")


st.write("⬇️ please press the button to get your current location")
st.write("⬇️ please press button few time if the map does not show up")

location = streamlit_geolocation()

# # lon = location["latitude"]   #= -43.5053818
# # lat = location["longitude"] #=:172.5837443
lon,lat = location["longitude"], location["latitude"]
st.write(lat,lon)


st.markdown(
    """
    The following map shows the 5 nearest bird hotspots your location. 
    
    **What is an eBird Hotspot?**
    
    **Hotspots** are public birding locations created by eBird users where is the best place to go birding. 
    
    The app will automatic calculate the 5 nearest hotspots to your location based on the recent uploaded hotspot coordinates. 
 
"""
)

# #lon = -43.5053818
# #lat = 172.5837443
# Map = geemap.Map(center=(lat,lon), zoom=15)
# Map.add_marker(location=(lat, lon), popup="You are here")

# Map.to_streamlit(width=800, height=300)

url = f"https://api.ebird.org/v2/ref/hotspot/geo?lat={lat}&lng={lon}"

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

center = (lon,lat)

center_point = Point(center)

gdf['distance'] = gdf.distance(center_point)

# Set the CRS to WGS84 (EPSG:4326) before transforming

gdf.set_crs(epsg=4326, inplace=True)
gdf.to_crs(epsg=4326, inplace=True)

gdf['distance'] = gdf.distance(center_point)

# Find the nearest points
nearest_points = gdf.nsmallest(5, 'distance')  # Adjust the number of nearest points as needed

# # Print the nearest points
# print(nearest_points)

Map = geemap.Map(center=(lon,lat), zoom=12)
popup = widgets.HTML(value="Your Location")
Map.add_marker(location=(lat,lon), popup=popup, name="Current Location")
Map.add_gdf(nearest_points, "Nearest Hotspots")

Map.to_streamlit(width=800, height=600)
