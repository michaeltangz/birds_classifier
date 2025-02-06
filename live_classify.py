import streamlit as st
import pandas as pd
import numpy as np
import pickle
import torch
import urllib.request
from PIL import Image
from transformers import pipeline
import requests
#import geemap
from streamlit_folium import st_folium
from streamlit_geolocation import streamlit_geolocation
import geemap.foliumap as geemap
import geopandas as gpd
from shapely.geometry import Point
import ipywidgets as widgets
import os
import folium
import requests

# #os.environ["EARTHENGINE_TOKEN"] == st.secrets["EARTHENGINE_TOKEN"]

# st.markdown("## Welcome to Bird Identification Page") 
# #st.write("This page will help you identify bird species")
# st.write("please upload the image file of bird to identify the species")

# #pipe = pipeline("image-classification", model="dennisjooo/Birds-Classifier-EfficientNetB2")
# # Create a file image uploader
# uploaded_file = st.file_uploader("Choose an image...", type="jpg")

# if uploaded_file is not None:
#     # Open the image using PIL
#     img = Image.open(uploaded_file)

#     # Display the uploaded image
#     st.image(img, caption='Uploaded Image.',  use_container_width=False, width=500)
#     st.write("")
#     st.write("⌛ Classifying......")

#     # Loading the model and preprocessor using Pipeline
#     pipe = pipeline("image-classification", model="dennisjooo/Birds-Classifier-EfficientNetB2")
#     result = pipe(img)[0]
#     st.write(f"**Prediction: {result['label']}**")
#     label = result['label']

    
# def convert_label(label):
#     return label.replace(" ", "_").lower()


# # Define the endpoint
# endpoint = "https://en.wikipedia.org/w/api.php"

# # # Define the parameters
# params = {
#     "action": "query",
#     "format": "json",
#     "titles": f"{convert_label(label)}",
#     # extract the taxonomy information  
#     "prop": 'extracts|pageimages',
#     #"prop": "extracts",
#     "exintro": True,
#     "explaintext": True,
#     "pithumbsize": 400

# }

# # # Make the request
# response = requests.get(endpoint, params=params)

# # # Parse the response
# data = response.json()
# #st.write(data)

# # # Extract the page content
# page = next(iter(data['query']['pages'].values()))
# extract = page.get('extract', 'No extract available')


# thumbnail = page.get('thumbnail', {}).get('source', None)

# # # Display the image if available
# if thumbnail:
#     st.image(thumbnail)

# st.write(f"🐤 **Description:** {' '.join(extract.split('.')[:3])}.")

# st.markdown("⬇️ Please press the button to get your current location, press button few times if the map does not show up")

# lon = 172.5837443
# lat = -43.5053818

# location = streamlit_geolocation()
# lat = location["latitude"]
# lon = location["longitude"]

# st.write(lat,lon)
# # Create a map centered at the current location
# m = folium.Map(location=[lat, lon], zoom_start=12)

# folium.Marker(
#     [lat, lon], 
#     popup="Current Location", 
#     icon=folium.Icon(color='red')  # Set marker color
# ).add_to(m)

# st_folium(m, width=600, height=400)

# import streamlit as st
# import requests
# from PIL import Image
# from transformers import pipeline

# st.markdown("<h1 style='font-size: 20px;'>Welcome to Bird Identification Page</h1>", unsafe_allow_html=True)
# st.write("This page will help you identify bird species and find the best nearest bird observation hotspots")
# st.write("Please upload the image file of bird to identify the species")

# # Create a file image uploader
# uploaded_file = st.file_uploader("Choose an image...", type="jpg")

# if uploaded_file is not None:
#     # Open the image using PIL
#     img = Image.open(uploaded_file)

#     # Display the uploaded image
#     st.image(img, caption='Uploaded Image.', use_container_width=False, width=500)
#     st.write("")
#     st.write("⌛ Classifying......")

#     # Loading the model and preprocessor using Pipeline
#     pipe = pipeline("image-classification", model="dennisjooo/Birds-Classifier-EfficientNetB2")
#     result = pipe(img)[0]
#     st.write(f"**Prediction: {result['label']}**")
#     label = result['label']

#     def convert_label(label):
#         return label.replace(" ", "_").lower()

#     # Define the endpoint
#     endpoint = "https://en.wikipedia.org/w/api.php"

#     # Define the parameters
#     params = {
#         "action": "query",
#         "format": "json",
#         "titles": f"{convert_label(label)}",
#         "prop": "extracts|pageimages",
#         "exintro": True,
#         "explaintext": True,
#         "pithumbsize": 400
#     }

#     # Make the request
#     response = requests.get(endpoint, params=params)

#     # Check if the response is empty
#     if response.text.strip() == "":
#         st.write("Received empty response from Wikipedia API")
#     else:
#         try:
#             # Parse the response
#             data = response.json()

#             # Extract the page content
#             page = next(iter(data['query']['pages'].values()))
#             extract = page.get('extract', 'No extract available')
#             thumbnail = page.get('thumbnail', {}).get('source', None)

#             # Display the image if available
#             if thumbnail:
#                 st.image(thumbnail)

#             # Display the description
#             st.write(f"🐤 **Description:** {' '.join(extract.split('.')[:3])}.")

#         except requests.exceptions.RequestException as e:
#             st.write("Failed to retrieve data from Wikipedia API")
#             st.write(f"Error: {e}")
#         except ValueError as e:
#             st.write("Failed to parse JSON response from Wikipedia API")
#             st.write(f"Error: {e}")

#     st.write("⬇️ Please press the button to get your current location")

#     location = streamlit_geolocation()

#     if location:
#         lat, lon = location["latitude"], location["longitude"]
#         st.write(f"Your location is: {lat}, {lon}")
#     else:
#         st.write("Please enable location services and press the button to get your current location.")

# #st.write(lat,lon)
# # Create a map centered at the current location
# location = streamlit_geolocation()
# lat, lon = location["latitude"], location["longitude"]
# m = folium.Map(location=[lat, lon], zoom_start=12)

# folium.Marker(
#     [lat, lon], 
#     popup="Current Location", 
#     icon=folium.Icon(color='red')  # Set marker color
# ).add_to(m)

# st_folium(m, width=600, height=400)
##############################################################
# import streamlit as st
# import requests
# from PIL import Image
# from transformers import pipeline
# import folium
# from streamlit_folium import st_folium
# from streamlit_geolocation import streamlit_geolocation

# st.markdown("<h1 style='font-size: 20px;'>Welcome to Bird Identification Page</h1>", unsafe_allow_html=True)
# st.write("This page will help you identify bird species and find the best nearest bird observation hotspots")
# st.write("Please upload the image file of bird to identify the species")

# # Create a file image uploader
# uploaded_file = st.file_uploader("Choose an image...", type="jpg")

# if uploaded_file is not None:
#     # Open the image using PIL
#     img = Image.open(uploaded_file)

#     # Display the uploaded image
#     st.image(img, caption='Uploaded Image.', use_container_width=False, width=500)
#     st.write("")
#     st.write("⌛ Classifying......")

#     # Loading the model and preprocessor using Pipeline
#     pipe = pipeline("image-classification", model="dennisjooo/Birds-Classifier-EfficientNetB2")
#     result = pipe(img)[0]
#     st.write(f"**Prediction: {result['label']}**")
#     label = result['label']

#     def convert_label(label):
#         return label.replace(" ", "_").lower()

#     # Define the endpoint
#     endpoint = "https://en.wikipedia.org/w/api.php"

#     # Define the parameters
#     params = {
#         "action": "query",
#         "format": "json",
#         "titles": f"{convert_label(label)}",
#         "prop": "extracts|pageimages",
#         "exintro": True,
#         "explaintext": True,
#         "pithumbsize": 400
#     }

#     # Make the request
#     response = requests.get(endpoint, params=params)

#     # Check if the response is empty
#     if response.text.strip() == "":
#         st.write("Received empty response from Wikipedia API")
#     else:
#         try:
#             # Parse the response
#             data = response.json()

#             # Extract the page content
#             page = next(iter(data['query']['pages'].values()))
#             extract = page.get('extract', 'No extract available')
#             thumbnail = page.get('thumbnail', {}).get('source', None)

#             # Display the image if available
#             if thumbnail:
#                 st.image(thumbnail)

#             # Display the description
#             st.write(f"🐤 **Description:** {' '.join(extract.split('.')[:3])}.")

#         except requests.exceptions.RequestException as e:
#             st.write("Failed to retrieve data from Wikipedia API")
#             st.write(f"Error: {e}")
#         except ValueError as e:
#             st.write("Failed to parse JSON response from Wikipedia API")
#             st.write(f"Error: {e}")

#     st.write("⬇️ Please press the button to get your current location")
   

#     location = streamlit_geolocation()

#     if location:
#         lat, lon = location["latitude"], location["longitude"]
#         st.write(f"Your location is: {lat}, {lon}")

#         # Create a map centered at the current location
#         m = folium.Map(location=[lat, lon], zoom_start=12)

#         folium.Marker(
#             [lat, lon], 
#             popup="Current Location", 
#             icon=folium.Icon(color='red')  # Set marker color
#         ).add_to(m)

#         st_folium(m, width=600, height=400)
#     else:
#         st.write("Please enable location services and press the button to get your current location.")
##############################################################

# import streamlit as st
# import requests
# from PIL import Image
# from transformers import pipeline
# import folium
# from streamlit_folium import st_folium
# from streamlit_geolocation import streamlit_geolocation

# st.markdown("<h1 style='font-size: 20px;'>Welcome to Bird Identification Page</h1>", unsafe_allow_html=True)
# st.write("This page will help you identify bird species and find the best nearest bird observation hotspots")
# st.write("Please upload the image file of bird to identify the species")

# # Create a file image uploader
# uploaded_file = st.file_uploader("Choose an image...", type="jpg")

# if uploaded_file is not None:
#     # Open the image using PIL
#     img = Image.open(uploaded_file)

#     # Display the uploaded image
#     st.image(img, caption='Uploaded Image.', use_container_width=False, width=500)
#     st.write("")
#     st.write("⌛ Classifying......")

#     # Loading the model and preprocessor using Pipeline
#     pipe = pipeline("image-classification", model="dennisjooo/Birds-Classifier-EfficientNetB2")
#     result = pipe(img)[0]
#     st.write(f"**Prediction: {result['label']}**")
#     label = result['label']

#     def convert_label(label):
#         return label.replace(" ", "_").lower()

#     # Define the endpoint
#     endpoint = "https://en.wikipedia.org/w/api.php"

#     # Define the parameters
#     params = {
#         "action": "query",
#         "format": "json",
#         "titles": f"{convert_label(label)}",
#         "prop": "extracts|pageimages",
#         "exintro": True,
#         "explaintext": True,
#         "pithumbsize": 400
#     }

#     # Make the request
#     response = requests.get(endpoint, params=params)

#     # Check if the response is empty
#     if response.text.strip() == "":
#         st.write("Received empty response from Wikipedia API")
#     else:
#         try:
#             # Parse the response
#             data = response.json()

#             # Extract the page content
#             page = next(iter(data['query']['pages'].values()))
#             extract = page.get('extract', 'No extract available')
#             thumbnail = page.get('thumbnail', {}).get('source', None)

#             # Display the image if available
#             if thumbnail:
#                 st.image(thumbnail)

#             # Display the description
#             st.write(f"🐤 **Description:** {' '.join(extract.split('.')[:3])}.")

#         except requests.exceptions.RequestException as e:
#             st.write("Failed to retrieve data from Wikipedia API")
#             st.write(f"Error: {e}")
#         except ValueError as e:
#             st.write("Failed to parse JSON response from Wikipedia API")
#             st.write(f"Error: {e}")

#     st.write("⬇️ Please press the button to get your current location")



# location = streamlit_geolocation()
# if location and "latitude" in location and "longitude" in location:

#     lat, lon = location["latitude"], location["longitude"]
#     st.write(f"Your location is: {lat}, {lon}")

#     # Create a map centered at the current location
#     m = folium.Map(location=[lat, lon], zoom_start=12)

#     folium.Marker(
#         [lat, lon], 
#         popup="Current Location", 
#         icon=folium.Icon(color='red')  # Set marker color
#     ).add_to(m)

#     st_folium(m, width=600, height=300)
# else:
#     st.write("Please enable location services and press the button to get your current location.")


import streamlit as st
import requests
from PIL import Image
from transformers import pipeline
import folium
from streamlit_folium import st_folium
from streamlit_geolocation import streamlit_geolocation
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)

st.markdown("<h1 style='font-size: 20px;'>Welcome to Bird Identification Page</h1>", unsafe_allow_html=True)
st.write("This page will help you identify bird species and find the best nearest bird observation hotspots")
st.write("Please upload the image file of bird to identify the species")

# Create a file image uploader
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Open the image using PIL
    img = Image.open(uploaded_file)

    # Display the uploaded image
    st.image(img, caption='Uploaded Image.', use_container_width=False, width=500)
    st.write("")
    st.write("⌛ Classifying......")

    # Loading the model and preprocessor using Pipeline
    pipe = pipeline("image-classification", model="dennisjooo/Birds-Classifier-EfficientNetB2")
    result = pipe(img)[0]
    st.write(f"**Prediction: {result['label']}**")
    label = result['label']

    def convert_label(label):
        return label.replace(" ", "_").lower()

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
        "pithumbsize": 400
    }

    # Make the request
    response = requests.get(endpoint, params=params)

    # Check if the response is empty
    if response.text.strip() == "":
        st.write("Received empty response from Wikipedia API")
    else:
        try:
            # Parse the response
            data = response.json()

            # Extract the page content
            page = next(iter(data['query']['pages'].values()))
            extract = page.get('extract', 'No extract available')
            thumbnail = page.get('thumbnail', {}).get('source', None)

            # Display the image if available
            if thumbnail:
                st.image(thumbnail)

            # Display the description
            st.write(f"🐤 **Description:** {' '.join(extract.split('.')[:3])}.")

        except requests.exceptions.RequestException as e:
            st.write("Failed to retrieve data from Wikipedia API")
            st.write(f"Error: {e}")
        except ValueError as e:
            logging.error("Failed to parse JSON response from Wikipedia API", exc_info=True)

    st.write("⬇️ Please press the button to get your current location")

    location = streamlit_geolocation()

    if location and "latitude" in location and "longitude" in location:
        lat, lon = location["latitude"], location["longitude"]
        st.write(f"Your location is: {lat}, {lon}")

        # Create a map centered at the current location
        m = folium.Map(location=[lat, lon], zoom_start=12)

        folium.Marker(
            [lat, lon], 
            popup="Current Location", 
            icon=folium.Icon(color='red')  # Set marker color
        ).add_to(m)

        st_folium(m, width=600, height=300)
    else:
        st.write("Please enable location services and press the button to get your current location.")