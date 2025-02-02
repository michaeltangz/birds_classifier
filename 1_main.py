import streamlit as st

st.set_page_config(
    page_title="HPAI Reporting Page"

)

st.title("HPAI Reporting Page")

st.sidebar.success("Select a page to start")

st.markdown(
    """
    This App can help you to identify the bird species and report the suspicious HPAI case.

    ## Introduction 
    1. **Live Bird Identify** : Classifying the bird species based on the **image & voice** 
    2. **Report Dead Bird Case**: Classifying the Dead bird species and reporting the proteintial HPAI case.
    3. **Useful HPAI Information**: This page provide the HPAI relative information.
"""
)


live_page1 = st.Page("live_classify.py", title="Image classify Species", icon=":material/add_circle:")
voice_page2 = st.Page("voice.py", title="Voice classify Species", icon=":material/add_circle:")
dead_page3 = st.Page("report_case.py", title="Report Case", icon=":material/add_circle:")
info_page4 = st.Page("useful_info.py", title="HPAI Useful Info", icon=":material/add_circle:")

pg = st.navigation([live_page1, voice_page2, dead_page3, info_page4])

pg.run()