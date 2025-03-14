import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
st.markdown("""
<style>
.big-font {
    font-size:300px !important;
}
</style>
""", unsafe_allow_html=True)


custom_css = """
<style>
    /* Hide the sidebar */
    [data-testid="stSidebar"] {
        display: none;
    }
    /* Adjust main content area */
    .main > div {
        padding-left: 2rem;
        padding-right: 2rem;
    }
    /* Style buttons */
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        text-align: center;
        font-size: 16px;
        cursor: pointer;
        transition-duration: 0.4s;
    }
    .stButton>button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

colT1,colT2 = st.columns([1,2])
with colT2:
    st.title(':blue-background[:green[WELCOME TO...]]')
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("linkivity.png")
colT1,colT2 = st.columns([1,3])
with colT2:
    st.subheader("BUY SUSTAINABLE CLOTHES IN SEVILLE!")
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    colT1,colT2 = st.columns([1,30])
    with colT2:
        st.warning("Please log in to access this page.")
        col1 = st.columns([1])
        with col1:
            ModelIsClicked=st.button("login",use_container_width=True)
            if ModelIsClicked:
                st.switch_page("pages/login.py")
    st.stop()

headers = st.context.headers
button_container = st.container()
with button_container:
    col1, col2, col3 = st.columns([1, 2, 3])
    with col1:
        ModelIsClicked=st.button("About us",use_container_width=True)
    if ModelIsClicked:
        st.switch_page("pages/about_us.py")
    with col2:
        ModelIsClicked=st.button("login",use_container_width=True)
    if ModelIsClicked:
        st.switch_page("pages/login.py")
    with col3:
        ModelIsClicked=st.button("Shop", use_container_width=True)
    if ModelIsClicked:
        st.switch_page("pages/shop.py")
