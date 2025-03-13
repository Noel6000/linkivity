import streamlit as st
import numpy as np
import random
import time
from openai import OpenAI

st.header("About us")
st.write("Our clothing brand consists of one product which is a LIFE shirt, it comes in different sizes, colors and editions. ")
st.write("There is a special limited edition Mr.A shirt with Mr.A's signature.")
st.subheader("Why are we sustainable?")
st.write("We will offer some handcrafted and local t-shirts to avoid sub-human conditions for workers, as “Wituka” collaborates with the Eden project which helps give good conditions to the workers, and so we can sell them for more money. Additionally, all our products will be done with 100% recycled materials, from old, discarded t-shirts. All our textile will be locally produced, and our dyes, safe. All of this is a benefit for society and environment because it offers an alternative to the usual products. Then, every 30 € we earn (profits) will result in five euros for Save The Children. ")


isClicked = st.button("mainpage", use_container_width=True)

if isClicked :
    st.switch_page("main_page.py")
