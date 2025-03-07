import streamlit as st
import numpy as np
import random
import time
from openai import OpenAI


client = OpenAI()



global pureResponse
def response_generator(AllMessages):
    global pureResponse
    GPTresponse = client.chat.completions.create(
        model="gpt-4o-mini",
        messages= AllMessages
    )
    pureResponse = str(GPTresponse.choices[0].message.content)
    response = "Job Bot: " + str(GPTresponse.choices[0].message.content)
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.set_page_config(layout="wide")

isClicked = st.button("mainpage", use_container_width=True)

if isClicked :
    st.switch_page("main_page.py")



if not "AllMessages" in st.session_state:
    st.session_state.AllMessages=[{"role": "system", "content": f"You are an assistant that helps web developers to find jobs and projects ongoing, and you can also set up their project and find people to work with them."}]

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

with st.chat_message("assistant"):
    st.markdown(f"Job Bot: Please input your experience and diplomas:")

# Accept user input
if prompt := st.chat_input("Type a question"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": f"User: {prompt}"})
    st.session_state.AllMessages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(f"User: {prompt}")

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(st.session_state.AllMessages))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.session_state.AllMessages.append({"role": "assistant", "content": pureResponse})
    print(st.session_state.AllMessages)
