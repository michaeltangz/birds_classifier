#  ### Want to learn more?
#     - Check out [streamlit.io](https://streamlit.io)
#     - Jump into our [documentation](https://docs.streamlit.io)
#     - Ask a question in our [community
#         forums](https://discuss.streamlit.io)
#     ### See more complex demos
#     - Use a neural net to [analyze the Udacity Self-driving Car Image
#         Dataset](https://github.com/streamlit/demo-self-driving)
#     - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)

# Example label
label = "Common Loon"

# Define the endpoint
endpoint = "https://en.wikipedia.org/w/api.php"

# Define the parameters to get the categories
params = {
    "action": "query",
    "format": "json",
    "titles": f"{convert_label(label)}",
    "prop": "categories",
    "cllimit": 100  # Limit the number of categories to retrieve
}

# Make the request to get categories
response = requests.get(endpoint, params=params)

# Check if the response is empty
if response.text.strip() == "":
    st.write("Received empty response from Wikipedia API")
else:
    try:
        # Parse the response
        data = response.json()

        # Extract the categories
        page = next(iter(data['query']['pages'].values()))
        categories = [cat['title'] for cat in page.get('categories', [])]
        
        # Display the categories
        st.write(f"📚 **Categories:** {', '.join(categories)}")

        # Filter the categories to choose the ones you want
        chosen_categories = [cat for cat in categories if "Articles with short description" in cat]
        st.write(f"🔍 **Chosen Categories:** {', '.join(chosen_categories)}")

        # Use the chosen categories to find related pages
        for category in chosen_categories:
            category_name = category.replace("Category:", "")
            st.write(f"🔍 **Searching for pages in category:** {category_name}")

            # Define the parameters to get pages in the category
            params = {
                "action": "query",
                "format": "json",
                "list": "categorymembers",
                "cmtitle": f"Category:{category_name}",
                "cmlimit": 5  # Limit the number of pages to retrieve
            }

            # Make the request to get pages in the category
            response = requests.get(endpoint, params=params)
            data = response.json()

            # Extract the page titles
            pages = [page['title'] for page in data.get('query', {}).get('categorymembers', [])]
            st.write(f"📄 **Pages in category {category_name}:** {', '.join(pages)}")

            # Extract content from the related pages
            for page_title in pages:
                params = {
                    "action": "query",
                    "format": "json",
                    "titles": page_title,
                    "prop": "extracts",
                    "exintro": True,
                    "explaintext": True
                }

                response = requests.get(endpoint, params=params)
                data = response.json()

                page = next(iter(data['query']['pages'].values()))
                extract = page.get('extract', 'No extract available')
                
                # Display the extract
                st.write(f"**{page_title}**")
                st.write(f"{extract}")

    except requests.exceptions.RequestException as e:
        st.write("Failed to retrieve data from Wikipedia API")
        st.write(f"Error: {e}")
    except ValueError as e:
        st.write("Failed to parse JSON response from Wikipedia API")
        st.write(f"Error: {e}")