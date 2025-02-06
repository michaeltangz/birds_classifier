# import streamlit as st

# st.set_page_config(
#     page_title="HPAI Reporting Page"

# )

# st.title("HPAI Reporting Page")

# #st.sidebar.success("Select a page to start")

# st.sidebar.title('Navigation')
# page = st.sidebar.radio("Go to", ["Live Bird Identify", "Report Dead Bird Case", "Hotspot Finder", "Useful HPAI Information"])


# # add pic here
# st.image("h5n1.webp", use_container_width=True)

# st.markdown(
#     """

#     <br> This App can help you to identify the bird species and report the suspicious HPAI case.  
    
#     **Live Bird Identify<br>** Classify the bird species based on the **image & voice**  
    
#     **Report Dead Bird Case**<br> Classify the Dead bird species and reporting the potential HPAI case.  
    
#     **Hotspot Finder**<br> Find the nearest bird observation hotspot near you.  
    
#     **Useful HPAI Information**<br> This page provides the HPAI relative information.
#     """, unsafe_allow_html=True
# )

# live_page1 = st.Page("live_classify.py", title="Image classify", icon=":material/add_circle:")
# voice_page2 = st.Page("voice.py", title="Voice classify", icon=":material/add_circle:")
# dead_page3 = st.Page("report_case.py", title="Report HPAI Case", icon=":material/add_circle:")
# info_page4 = st.Page("useful_info.py", title="HPAI Useful Info", icon=":material/add_circle:")
# hospot_page5 = st.Page("hotspot.py", title="Hotspot Finder", icon=":material/add_circle:")

# pg = st.navigation([live_page1, voice_page2, dead_page3, info_page4, hospot_page5])

# pg.run()

import streamlit as st

st.set_page_config(page_title="HPAI Reporting Page", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to", 
    ["Home", "Live Bird Identification", "Voice Classification", "Report HPAI Case", "Hotspot Finder", "HPAI Useful Info"]
)

# Display the selected page
if page == "Home":
    st.title("HPAI Reporting Page")
    st.sidebar.success("Select a page to start")

    # Add image
    st.image("h5n1.webp", use_container_width=True)

    st.markdown(
        """
        <br> This App can help you to identify the bird species and report the suspicious HPAI case.  

        **Live Bird Identify**<br> Classify the bird species based on the **image & voice**  

        **Report Dead Bird Case**<br> Classify the Dead bird species and report the potential HPAI case.  

        **Hotspot Finder**<br> Find the nearest bird observation hotspot near you.  

        **Useful HPAI Information**<br> This page provides relevant HPAI information.
        """, unsafe_allow_html=True
    )

elif page == "Live Bird Identification":
    import pages.live_classify as live_classify
    live_classify.run()

elif page == "Voice Classification":
    import pages.voice as voice
    voice.run()

elif page == "Report HPAI Case":
    import pages.report_case as report_case
    report_case.run()

elif page == "Hotspot Finder":
    import pages.hotspot as hotspot
    hotspot.run()

elif page == "HPAI Useful Info":
    import pages.useful_info as useful_info
    useful_info.run()




# Hide Streamlit's default sidebar
# hide_streamlit_style = """
#     <style>
#         [data-testid="stSidebarNav"] {display: none;}
#     </style>
# """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)


