import streamlit as st
import numpy as np
import random
import time
from openai import OpenAI

st.header("About us")
st.write("Our clothing brand consist of one product which is a LIFE shirt, it comes in diferent sizes, colours and editions. ")
st.subheader("Why are we sustainable?")
st.write("aqui va el textaco de lilian")


isClicked = st.button("mainpage", use_container_width=True)

if isClicked :
    st.switch_page("main_page.py")
