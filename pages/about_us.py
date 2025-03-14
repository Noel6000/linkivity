import streamlit as st
import numpy as np
import random
import time
from openai import OpenAI


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

st.header("About us")
st.write("Our clothing brand consists of one product which is a LIFE shirt, it comes in different sizes, colors and editions. ")
st.write("There is a special limited edition Mr.A shirt with Mr.A's signature.")
st.image("exclusive.png")
st.subheader("Why are we sustainable?")
st.write("We offer some handcrafted and local t-shirts to avoid sub-human conditions for workers, as “Wituka” collaborates with the Eden project which helps give good conditions to the workers. Additionally, all our products are done with 100% recycled materials, from old, discarded t-shirts. All our textile is locally produced, and our dyes, safe. With our T-Shirts for Everyone program, for every 30 € we earn at the end of the months we give five euros for Save The Children. With LIFE Products, choose to defend the workers right and escape the lie of fast fashion.")


isClicked = st.button("MAINPAGE", use_container_width=True)

if isClicked :
    st.switch_page("main_page.py")
