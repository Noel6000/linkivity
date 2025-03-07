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
st.title(':blue-background[:green[Welcome to...] :sunglasses:]')
st.header('LINKIVITY!')
st.subheader(":red-background[This website is for web developers to find a job and for companies to find a web developer.]")
import streamlit as st

if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("Please log in to access this page.")
    st.stop()

headers = st.context.headers
button_container = st.container()
with button_container:
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        ModelIsClicked=st.button("Look for projects!",use_container_width=True)
    if ModelIsClicked:
        st.switch_page("pages/find_project.py")
    with col2:
        ModelIsClicked=st.button("About us",use_container_width=True)
    if ModelIsClicked:
        st.switch_page("pages/about_us.py")
    with col3:
        ModelIsClicked=st.button("Go to Dashboard",use_container_width=True)
    if ModelIsClicked:
        st.switch_page("pages/dashboard.py")
    with col4:
        ModelIsClicked=st.button("login",use_container_width=True)
    if ModelIsClicked:
        st.switch_page("pages/login.py")
