import streamlit as st
import streamlit_book as stb
import numpy as np
import random
import time

correct = 0
if stb.true_or_false(f"To print 'Hello world', you would write \"print(\"Hello World\")\"", True):
  correct += 1
