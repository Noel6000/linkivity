import streamlit as st
import numpy as np
import random
import time
from openai import OpenAI

st.header("About us")
st.write("Our clothing brand consists of one product which is a LIFE shirt, it comes in different sizes, colors and editions. ")
st.write("There is a special limited edition Mr.A shirt with Mr.A's signature.")
st.subheader("Why are we sustainable?")
st.write("We offer some handcrafted and local t-shirts to avoid sub-human conditions for workers, as \“Wituka\” collaborates with the Eden project which helps give good conditions to the workers. Additionally, all our products are done with 100% recycled materials, from old, discarded t-shirts. All our textile is locally produced, and our dyes, safe. With our T-Shirts for Everyone program, for every 30 € we earn at the end of the months we give five euros for Save The Children. With LIFE Products, choose to defend the workers right and escape the lie of fast fashion.")


isClicked = st.button("MAINPAGE", use_container_width=True)

if isClicked :
    st.switch_page("main_page.py")
