# from matplotlib.pylab import f
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



# st.markdown("## Report the suspicious HPAI case")
# #st.write("You can report the suspicious HPAI case to Authority")
# st.markdown("### You can upload multiple images")

# # Create a file image uploader
# uploaded_file = st.file_uploader("Choose an image...", type="jpg")


# if uploaded_file:
#     # Loading the model and preprocessor using Pipeline
#     pipe = pipeline("image-classification", model="chriamue/bird-species-classifier")

#     for uploaded_file in uploaded_file:
#         # Open the image using PIL
#         img = Image.open(uploaded_file)

#         # Display the uploaded image
#         st.image(img, caption='Uploaded Image.', use_container_width=True)

#         # Running the inference
#         result = pipe(img)[0]
#         label = result['label']

#         # Displaying the result label
#         st.write(f"**Prediction: {result['label']}**")



# def convert_label(label):
#     return st.write(label.replace(" ", " ").lower())

# st.write("⬇️ please press the button to get your current location")

# location = streamlit_geolocation()

# lat,lon = location["longitude"], location["latitude"]

# #st.markdown(f"#### Your location is: {lon}, {lat}")

# st.write(f"The suspicious HPAI case:  **{label}**  at location: {lon}, {lat}")

# st.write("To better help us understand the case, you can upload more images of the dead bird")
# st.write("Please take the photo from different angle, keep a **safe distance** and **do not touch** the dead bird")

# st.write("You can upload multiple images from here")
# uploaded_files = st.file_uploader("Choose an image...", type="jpg", accept_multiple_files=True)


# st.write("Press the button to report the suspicious HPAI case")

# # Create a button to report the label and location
# if st.button("Report"):
    
#     st.markdown("### Thank you for report. we will review your report shortly.")


from streamlit_folium import st_folium
from streamlit_geolocation import streamlit_geolocation
#import geemap.foliumap as geemap
import streamlit as st
from PIL import Image
from transformers import pipeline
from datetime import datetime

st.title("Report a suspicious HPAI case")
#st.markdown("### You can upload multiple images")
st.write("👉 **To help us assess the case, you may upload additional images of the dead bird.**")
st.write("👉 **Note: If you upload additional images, please take pictures from different angles, maintain a **safe distance**, and **avoid touching** the dead bird.**")

# Create a file image uploader that accepts multiple files
uploaded_files = st.file_uploader("Choose images...", type="jpg", accept_multiple_files=True)

if uploaded_files:
    # Loading the model and preprocessor using Pipeline
    pipe = pipeline("image-classification", model="chriamue/bird-species-classifier")

    labels = []  # List to store labels for all uploaded images

    for uploaded_file in uploaded_files:
        # Open the image using PIL
        img = Image.open(uploaded_file)

        # Display the uploaded image
        st.image(img, caption='Uploaded Image.', use_container_width=True)

        # Running the inference
        result = pipe(img)[0]

        # Displaying the result label
        st.write(f"**Prediction: {result['label']}**")
        labels.append(result['label'])  # Store the label

    def convert_label(label):
        return label.replace(" ", "_").lower()

    st.write("⬇️ Please press the button to get your current location")

    location = streamlit_geolocation()
    time = current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if location:
        lat, lon = location["latitude"], location["longitude"]
        st.write(f"**The suspicious HPAI case: {', '.join(labels)}**")
        st.write(f"**Location:** {lat}, {lon}")
        st.write(f"**Time:** {current_time}")

       
        st.write("Press the button to report the suspicious HPAI case")

        # Create a button to report the label and location
        if st.button("Report"):
            st.markdown("### Thank you for your report. We will review your report shortly.")
    else:
        st.write("**Please enable location services and press the button to get your current location.**")

# def run():
#     #st.title(".")
#     st.write("Upload an image to classify the dead bird species to help us understand the proteintial HPAI case")

# if __name__ == "__main__":
#     run()