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
headers = st.context.headers
button_container = st.container()
with button_container:
    col1, col2 = st.columns([1, 1])
    with col1:
        ModelIsClicked=st.button("Look for projects!",use_container_width=True)
    if ModelIsClicked:
        st.switch_page("pages/find_project.py")
    with col2:
        ModelIsClicked=st.button("About us",use_container_width=True)
    if ModelIsClicked:
        st.switch_page("pages/about_us.py")
