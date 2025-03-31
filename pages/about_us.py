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
st.write("We offer some handcrafted and local T-shirts to avoid sub-human conditions for workers by choosing a sustainable provider, Wituka.  Wituka collaborates with the Eden project, which helps give good conditions to the workers. All of the T-shirt we buy from Wituka are made with 100% organic cotton, which reduces the water used in the production of the T-shirt by 91%. At  the ed of each month, we give 10% of our remaining profits to Save The Children. With LIFE Products, choose to defend the worker's right and escape the lie of fast fashion.")
st.write("There is a special limited edition, the official Mr. A shirt with Mr. A's signature!")
st.image("exclusive.png")


isClicked = st.button("Go back to the main page", use_container_width=True)

if isClicked :
    st.switch_page("main_page.py")
