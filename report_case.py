from matplotlib.pylab import f
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


st.title("Reporting the suspicious HPAI case")
st.write("This page will help you identify dead bird and help you report the suspicious HPAI case to Authority")
st.write("please upload the image of dead bird")

# Create a file image uploader
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Open the image using PIL
    img = Image.open(uploaded_file)

    # Display the uploaded image
    st.image(img, caption='Uploaded Image.',  use_container_width=True)

    # Loading the model and preprocessor using Pipeline
    pipe = pipeline("image-classification", model="chriamue/bird-species-classifier")

    # Running the inference
    result = pipe(img)[0]

    # Displaying the result label
    #st.write(f"Prediction: {result['label']}")

# import pipeline model
# Load model directly
# Load model directly
# Use a pipeline as a high-level helper
#from transformers import pipeline

label = result['label']
st.write(f"**Prediction: {result['label']}**")

def convert_label(label):
    return st.write(label.replace(" ", " ").lower())



# import requests

# # Define the parameters
# params = {
#     "action": "query",
#     "format": "json",
#     "titles": f"{convert_label(label)}",
#     "prop": "extracts|pageimages",
#     "exintro": True,
#     "explaintext": True,
#     "pithumbsize": 500  # Set the thumbnail size
# }

# # Define the endpoint
# endpoint = "https://en.wikipedia.org/w/api.php"

# # Make the request
# response = requests.get(endpoint, params=params)

# # Parse the response
# data = response.json()

# # Extract the page content
# page = next(iter(data['query']['pages'].values()))
# extract = page.get('extract', 'No extract available')
# thumbnail = page.get('thumbnail', {}).get('source', None)

# Display the result
# print(f"Description: {extract}")
# if thumbnail:
#     print(f"Thumbnail URL: {thumbnail}")




location = streamlit_geolocation()

# lon = location["latitude"]   #= -43.5053818
# lat = location["longitude"] #=:172.5837443
lat,lon = location["longitude"], location["latitude"]
#lon = -43.5053818
#lat = 172.5837443
st.write(f"Your location is: {lon}, {lat}")

# #lon = -43.5053818
# #lat = 172.5837443
# Map = geemap.Map(center=(lon,lat), zoom=15)
# Map.add_marker(location=(lon, lat), popup="You are here")

# Map.to_streamlit(width=800, height=300)

st.write(f"The suspicious HPAI case:  **{label}**  at location: {lon}, {lat}")

st.write("Please press the button to report the suspicious HPAI case")

# Create a button to report the label and location
if st.button("Report"):
    
    st.write("Thank you for report. The Authority will review your report shortly.")