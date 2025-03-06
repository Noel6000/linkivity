import streamlit as st
import numpy as np
import random
import time
from openai import OpenAI

isClicked = st.button("mainpage", use_container_width=True)
if isClicked :
    st.switch_page("main_page.py")
st.header("Test your knowledge.")
st.header(":warning:")
st.subheader(":red[:blue-background[This test will be used to classify your knowledge by companies wishing to hire web developers.]]")
st.header(":warning:")

