import streamlit as st
import numpy as np
import random
import time


isClicked = st.button("mainpage", use_container_width=True)

if isClicked :
    st.switch_page("main_page.py")
