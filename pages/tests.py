import streamlit as st
import streamlit_book as stb
import numpy as np
import random
import time

correct = 0
questions = 0
var = True
vvar = 0
while var:
  if stb.true_or_false(f"To print 'Hello world', you would write \"print(\"Hello World\")\"", True):
    correct += 1
    questions += 1
    vvar +=1
  else:
    questions += 1
    questions -= 1
    vvar +=1
  
    
  if stb.single_choice("How do you insert COMMENTS in Python code?", ["\#This is a comment", "//This is a comment", "/*This is a comment*/"], 0):
    correct += 1
    questions += 1
    vvar +=1
  else:
    questions += 1
    questions -= 1
    vvar +=1

  if vvar = 2:
    var = False

st.write(f"You have had {correct}/{questions} questions right.")
