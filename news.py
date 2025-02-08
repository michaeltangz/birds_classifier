
from newsapi import NewsApiClient
import streamlit as st

api = NewsApiClient(api_key='e60e86de537341c990eed3f202a2f9f4')

bird_flu_news = api.get_everything(q='bird flu', language='en')

# for article in bird_flu_news['articles']:
#     st.write(f"Title: {article['title']}")
#     st.write(f"Description: {article['description']}")
#     st.write(f"Content: {article['content']}")
#     st.write(f"Published At: {article['publishedAt']}")
#     st.write(f"Source: {article['source']['name']}")
#     st.write(f"URL: {article['url']}")
#     st.write(f"Image: {article['urlToImage']}")
#     st.write("---------------------------------------------------")

for article in bird_flu_news['articles']:
    print(f"Title: {article['title']}")
    #print(f"Description: {article['description']}")
    #print(f"Content: {article['content']}")
    print(f"Published At: {article['publishedAt']}")
    print(f"Source: {article['source']['name']}")
    print(f"URL: {article['url']}")
    print("---------------------------------------------------")