import streamlit as st
import numpy as np
import random
import time
from openai import OpenAI

isClicked = st.button("mainpage", use_container_width=True)
if isClicked:
    st.switch_page("main_page.py")
st.header("Test your knowledge.")
st.header(":warning:")
st.subheader(":red[:blue-background[This test will be used to classify your knowledge by companies wishing to hire web developers.]]")
st.header(":warning:")

# newline char
def nl(num_of_lines):
    for i in range(num_of_lines):
        st.write(" ")

# in reality, we are really just printing whitespaces before/after
# components, leveraging on streamlit's top to botom rendering of components.
# the num_of_lines we want as spacing is passed into the nl() function
# and streamlit just prints rows of whitespaces before rendering the next
# component in our code.

nl(1)

# Text Prompt
st.markdown("""
            Write Quiz Description and Instructions.
            """)

# Create Placeholder to print test score
scorecard_placeholder = st.empty()

# Activate Session States
ss = st.session_state
# Initializing Session States
if 'counter' not in ss:
    ss['counter'] = 0
if 'start' not in ss:
    ss['start'] = False
if 'stop' not in ss:
    ss['stop'] = False
if 'refresh' not in ss:
    ss['refresh'] = False
if "button_label" not in ss:
    ss['button_label'] = ['START', 'SUBMIT', 'RELOAD']
if 'current_quiz' not in ss:
    ss['current_quiz'] = {}
if 'user_answers' not in ss:
    ss['user_answers'] = []
if 'grade' not in ss:
    ss['grade'] = 0


