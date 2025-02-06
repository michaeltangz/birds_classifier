from streamlit_folium import st_folium
from streamlit_geolocation import streamlit_geolocation
import geemap.foliumap as geemap
import streamlit as st
from transformers import pipeline
import numpy as np
import soundfile as sf
import requests


st.markdown("### This page will identify bird species by voice")
st.write("Please upload the voice file of bird to identify the species")
uploaded_file = st.file_uploader("Choose a voice file...", type="wav")
#################voice file 
if uploaded_file is not None:
    # Read the uploaded file
    data, samplerate = sf.read(uploaded_file)

    # Convert to single channel if necessary
    if len(data.shape) > 1:
        data = data[:, 0]  # Use the first channel

    # Convert the data to a numpy ndarray
    audio_array = np.array(data)

    # Play the uploaded audio file
    st.audio(uploaded_file, format='audio/wav')

    # Loading the model and preprocessor using Pipeline
    pipe_voice = pipeline("audio-classification", model="dima806/bird_sounds_classification")
    # Running the inference
    result_voice = pipe_voice(audio_array)

    # Displaying the result label
    st.write(f"**Prediction: {result_voice[0]['label']}**")

    # Define the endpoint
    endpoint = "https://en.wikipedia.org/w/api.php"

    # Define the parameters
    params = {
        "action": "query",
        "format": "json",
        "titles": f"{result_voice[0]['label'].lower()}",
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
        #"pithumbsize": 600  # Set the thumbnail size
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
        st.image(thumbnail, caption=f"{result_voice[0]['label']}")

        
    st.write(f"**Description:** {extract}")

    