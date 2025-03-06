import streamlit as st
import numpy as np
import random
import time
from openai import OpenAI

question_dict1 = {
 "question_number": 1, 
 "question": "What is a correct syntax to output 'hello world' in Python?",
 "options": ["print(hello world)", "p('hello world')", "print('hello world')", "print(hello.world)"],
 "correct_answer": "print('hello world')",
 "explanation": ""
 }
"""
question_dict2
question_dict3
question_dict4
question_dict5
question_dict6
question_dict7
question_dict8
question_dict9
question_dict10
question_dict11"""


questions = [question_dict1, """question_dict2, question_dict3, question_dict4, question_dict5, question_dict6, question_7, question_8, question_9, question_10, question_11"""]

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

# Function for button click
def btn_click():
    ss.counter += 1
    if ss.counter > 2: 
        ss.counter = 0
        ss.clear()
    else:
        update_session_state()
        with st.spinner("*this may take a while*"):
            time.sleep(2)

# Function to update current session
def update_session_state():
    if ss.counter == 1:
        ss['start'] = True
        ss.current_quiz = random.sample(quiz.questions, 10)
    elif ss.counter == 2:
        # Set start to False
        ss['start'] = True 
        # Set stop to True
        ss['stop'] = True

# Initializing Button Text
st.button(label=ss.button_label[ss.counter], 
        key='button_press', on_click= btn_click)

# Function to display a question
def quiz_app():
    # create container
    with st.container():
        if (ss.start):
            for i in range(len(ss.current_quiz)):
                number_placeholder = st.empty()
                question_placeholder = st.empty()
                options_placeholder = st.empty()
                results_placeholder = st.empty()
                expander_area = st.empty()                
                # Add '1' to current_question tracking variable cause python starts counting from 0
                current_question = i+1
                # display question_number
                number_placeholder.write(f"*Question {current_question}*")
                # display question based on question_number
                question_placeholder.write(f"**{ss.current_quiz[i].get('question')}**") 
                # list of options
                options = ss.current_quiz[i].get("options")
                # track the user selection
                options_placeholder.radio("", options, index=1, key=f"Q{current_question}")
                nl(1)
                # Grade Answers and Return Corrections
                if ss.stop:
                    # Track length of user_answers
                    if len(ss.user_answers) < 10: 
                        # comparing answers to track score
                        if ss[f'Q{current_question}'] == ss.current_quiz[i].get("correct_answer"):
                            ss.user_answers.append(True)
                        else:
                            ss.user_answers.append(False)
                    else:
                        pass
                    # Results Feedback
                    if ss.user_answers[i] == True:
                        results_placeholder.success("CORRECT")
                    else:
                        results_placeholder.error("INCORRECT")
                    # Explanation of the Answer
                    expander_area.write(f"*{ss.current_quiz[i].get('explanation')}*")

    # calculate score
    if ss.stop:  
        ss['grade'] = ss.user_answers.count(True)           
        scorecard_placeholder.write(f"### **Your Final Score : {ss['grade']} / {len(ss.current_quiz)}**")        



