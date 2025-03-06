import streamlit as st
import numpy as np
import random
import time
from openai import OpenAI

st.header("About us")

isClicked = st.button("mainpage", use_container_width=True)

if isClicked :
    st.switch_page("main_page.py")
