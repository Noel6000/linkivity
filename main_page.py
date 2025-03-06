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
st.title(':blue-background[:green[Welcome to...] :sunglasses:')
st.header('LINKIVITY!')
st.subheader(':blue-background[:red[Hello John! Today is your] :birthday:.]')
st.image("linkivity.png", caption="linkivity", width=None)
headers = st.context.headers
button_container = st.container()
with button_container:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        ModelIsClicked=st.button("Find a job!",use_container_width=True)
    if ModelIsClicked:
        st.switch_page("pages/artificial_intelligence.py")
        col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        ModelIsClicked=st.button("Resume generator",use_container_width=True)
    if ModelIsClicked:
        st.switch_page("pages/curriculum_generator.py")
    with col3:
        ModelIsClicked=st.button("Look for companies!",use_container_width=True)
    if ModelIsClicked:
        st.switch_page("pages/bussineses.py")
