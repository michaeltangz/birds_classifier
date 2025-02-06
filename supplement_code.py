# # # Make the request
# response = requests.get(endpoint, params=params)

# # Parse the response
# data = response.json()
# st.write(data)

# Extract the page content
# page = next(iter(data['query']['pages'].values()))
# extract = page.get('extract', 'No extract available')
# thumbnail = page.get('thumbnail', {}).get('source', None)
# # Display the image if available
# if thumbnail:
#     st.image(thumbnail)

# st.write(f"🐤 **Discription:** {extract}")
# #EARTHENGINE_TOKEN = 'AIzaSyAQTdxrxn-K0UopmS82mSP4inkfd9ivRNI'
# st.write("⬇️ please press the button to get your current location")
# st.write("⬇️ please press button few time if the map does not show up")

# location = streamlit_geolocation()

# lon = location["latitude"]   #= -43.5053818
# lat = location["longitude"] #=:172.5837443

# lon = -43.5053818
# lat = 172.5837443
#lon,lat = location["longitude"], location["latitude"]
# st.write(lat,lon)

# # Use existing lat and lon variables

# lat = 172.5837443
# lon = -43.5053818

# #from geopy.geocoders import Nominatim

# # Get current location (replace with actual coordinates if needed)
# #geolocator = Nominatim(user_agent="geo_locator")
# # location = geolocator.geocode("Los Angeles, CA")
# # lat, lon = location.latitude, location.longitude

# # Create a map centered at the current location
# m = folium.Map(location=[lon, lat], zoom_start=12)

# folium.Marker(
#     [lon, lat], 
#     popup="Current Location", 
#     icon=folium.Icon(color='red')  # Set marker color
# ).add_to(m)

# st_folium(m, width=600, height=400)



# st.markdown(
#     """
#     The following map shows the 5 nearest bird hotspots your location. 
    
#     **What is an eBird Hotspot?**
    
#     **Hotspots** are public birding locations created by eBird users where is the best place to go birding. 
    
#     The app will automatic calculate the 5 nearest hotspots to your location based on the recent uploaded hotspot coordinates. 
 
# """
# )

# # #lon = -43.5053818
# # #lat = 172.5837443
# # Map = geemap.Map(center=(lat,lon), zoom=15)
# # Map.add_marker(location=(lat, lon), popup="You are here")

# # Map.to_streamlit(width=800, height=300)

# url = f"https://api.ebird.org/v2/ref/hotspot/geo?lat={lat}&lng={lon}"

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
#     parts = line.split(',')
#     latitude = float(parts[4])
#     longitude = float(parts[5])
#     coordinates.append((latitude, longitude))

# # Create a GeoDataFrame
# gdf = gpd.GeoDataFrame(geometry=gpd.points_from_xy([lon for lat, lon in coordinates], [lat for lat, lon in coordinates]))

# center = (lon,lat)

# center_point = Point(center)

# gdf['distance'] = gdf.distance(center_point)

# # Set the CRS to WGS84 (EPSG:4326) before transforming

# gdf.set_crs(epsg=4326, inplace=True)
# gdf.to_crs(epsg=4326, inplace=True)

# gdf['distance'] = gdf.distance(center_point)

# # Find the nearest points
# nearest_points = gdf.nsmallest(5, 'distance')  # Adjust the number of nearest points as needed

# # # Print the nearest points
# # print(nearest_points)

# Map = geemap.Map(center=(lon,lat), zoom=12)
# popup = widgets.HTML(value="Your Location")
# Map.add_marker(location=(lat,lon), popup=popup, name="Current Location")
# Map.add_gdf(nearest_points, "Nearest Hotspots")

# <<<<<<< HEAD
# Map.to_streamlit(width=800, height=600)

# #4/1ASVgi3JJNdYIVFea0vgFdzh8jPhbYN1Al0xhg4MHIHATdme4faSQKR6yZ4U
# =======
# # Map.to_streamlit(width=800, height=600)
# >>>>>>> 521c284d62e6af5ea53ad4d8684b315282d65364



 # Display the images
# images = page.get('images', [])
# st.write(images)
# for image in images:
#     image_title = image['title']
#     image_url = f"https://en.wikipedia.org/wiki/Special:FilePath/{image_title.replace(' ', '_')}"
#     st.image(image_url, caption=image_title)

##########################################################################
# #EARTHENGINE_TOKEN = 'AIzaSyAQTdxrxn-K0UopmS82mSP4inkfd9ivRNI'


#import wikipediaapi
# wiki_wiki = wikipediaapi.Wikipedia(user_agent='MyProjectName (merlin@example.com)', language='en')

# page_py = wiki_wiki.page(convert_label(label))

# #print("Page - Exists: %s" % page_py.exists())

# # Get the summary of the page
# #print(page_py.summary)

# # Print the entire text of the page
# st.write(page_py.text)

#///////???????????????????????????????????????????????????
# show more button
# import random
# import time
# import streamlit as st
# import SessionState


# @st.cache
# def long_calculation(i):
#     time.sleep(1)
#     return 1000 * i + random.randrange(100)


# def main():
#     session_state = SessionState.get(length=5)
#     if st.button("Show more"):
#         session_state.length += 5
#     for i in range(1, session_state.length + 1):
#         st.write("item %d: %d" % (i, long_calculation(i)))


# main()