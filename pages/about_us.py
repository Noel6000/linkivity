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
st.write("There is a special limited edition, the official Mr. A shirt with Mr. A's signature!")
st.image("exclusive.png")
st.subheader("Why are we sustainable?")
st.write("We offer some handcrafted and local T-shirts to avoid sub-human conditions for workers, as “Wituka” collaborates with the Eden project, which helps give good conditions to the workers. Additionally, all our products are made with 100% recycled materials, from old, discarded T-shirts. All our textiles are locally produced, and our dyes are safe. With our T-shirts for Everyone program. We will give 10% of profits at the end of the month to Save The Children. With LIFE Products, choose to defend the worker's right and escape the lie of fast fashion.")


isClicked = st.button("Go back to the main page", use_container_width=True)

if isClicked :
    st.switch_page("main_page.py")
