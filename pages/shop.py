import streamlit as st


isClicked = st.button("mainpage", use_container_width=True)

if isClicked :
    st.switch_page("main_page.py")
