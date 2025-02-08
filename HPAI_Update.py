
from newsapi import NewsApiClient
import streamlit as st

st.set_page_config(page_title="HPAI Reporting Page", layout="wide")

# Sidebar Navigation
#st.sidebar.title("Navigation")
# page = st.sidebar.radio(
#     "Go to", 
#     ["Home", "Live Bird Identification", "Voice Classification", "Report HPAI Case", "Hotspot Finder", "HPAI Useful Info"]
# )

# Display the selected page

st.title("HPAI Case Reporting Page")
st.sidebar.success("Select a page to start")



# st.markdown(
#         """
#         <br> This App can help you to identify the bird species and report the suspicious HPAI case.  

#         **Live Bird Identify**<br> Classify the bird species based on the **image & voice**  

#         **Report Dead Bird Case**<br> Classify the Dead bird species and report the potential HPAI case.  

#         **Hotspot Finder**<br> Find the nearest bird observation hotspot near you.  

#         **Useful HPAI Information**<br> This page provides relevant HPAI information.
#         """, unsafe_allow_html=True
#     )


st.markdown("##### This App can help you to identify the bird species and report the suspicious HPAI case.")

st.write("---------------------------------------------------")

st.markdown("## The HPAI News & Updates") 

api = NewsApiClient(api_key='e60e86de537341c990eed3f202a2f9f4')

bird_flu_news = api.get_everything(q='bird flu', language='en')

# for article in bird_flu_news['articles'][:5]:
#     st.write(f"Title: {article['title']}")
#     #st.write(f"Description: {article['description']}")
#     #st.write(f"Content: {article['content']}")
#     #st.write(f"Published At: {article['publishedAt']}")
#     #st.write(f"Source: {article['source']['name']}")
#     st.write(f"URL: {article['url']}")
#     #st.write(f"Image: {article['urlToImage']}")
#     st.components.v1.iframe(article['url'], height=200, scrolling=False)
#     st.write("---------------------------------------------------")

# for article in bird_flu_news['articles'][:5]:
#     st.title(f"{article['title']}")
#     st.write(f"[Read more]({article['url']})")
#     #st.write(f"Image: {article['urlToImage']}")
#     # display the image
#     st.image(article['urlToImage'], caption=article['title'], use_container_width=True) 
#     st.write("---------------------------------------------------")

# for article in bird_flu_news['articles']:
#     print(f"Title: {article['title']}")
#     #print(f"Description: {article['description']}")
#     #print(f"Content: {article['content']}")
#     print(f"Published At: {article['publishedAt']}")
#     print(f"Source: {article['source']['name']}")
#     print(f"URL: {article['url']}")
#     print("---------------------------------------------------")

from newsapi import NewsApiClient
from datetime import datetime



api = NewsApiClient(api_key='e60e86de537341c990eed3f202a2f9f4')

bird_flu_news = api.get_everything(q='bird flu', language='en')

for article in bird_flu_news['articles'][:6]:
    st.markdown(f"#### {article['title']}")
    # Convert publishedAt to datetime
    published_at = datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
    formatted_date = published_at.strftime('%Y-%m-%d')
    st.write(f"**Date:** {formatted_date}")
 
    #st.write(f"Date: {article['publishedAt']}") 
    if article['urlToImage']:
        st.markdown(f"[![{article['title']}]({article['urlToImage']})]({article['url']})")
    st.write("---------------------------------------------------")

