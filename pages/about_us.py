import streamlit as st
import numpy as np
import random
import time
from openai import OpenAI


custom_css = """
<style>
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

st.header("About us")
st.subheader("Why are we sustainable?")
st.write("We make local, handcrafted T-shirts that offer better conditions for its workers.")
st.write("For that, we've partnered with Wituka, whose T-shirts are made with 100% organic cotton; reducing water consumption in the production of the T-shirt by 91%. Wituka also collaborates with the Eden Project which helps improve workers' labour conditions.")
st.write("Additionally, we give 10% of our remaining monthly profits to Save The Children.")
st.image("exclusive.png")
st.write("Image above: Exclusive LIFE T-shirt, with Mr. A's signature.")


isClicked = st.button("Go back to the main page", use_container_width=True)

if isClicked :
    st.switch_page("main_page.py")
