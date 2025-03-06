import streamlit as st
import numpy as np
import random
import time
from openai import OpenAI

st.header("About us")
st.write("We are Baltasar, Andrés, Michael, Jiajia, Lilian, and Noël, a group of 8th grade students that have developed an alternative to linkedin for the Eureka Starter Days.")
st.image("group.png")


isClicked = st.button("mainpage", use_container_width=True)

if isClicked :
    st.switch_page("main_page.py")
