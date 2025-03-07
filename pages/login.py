import streamlit as st
import json
import os

# File to store user credentials
USER_FILE = "users.json"

# Function to load user data from JSON file
def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            return json.load(file)
    return {}

# Function to save user data to JSON file
def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)

# Load users into session state
if 'users' not in st.session_state:
    st.session_state.users = load_users()

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if 'current_user' not in st.session_state:
    st.session_state.current_user = None

# Function to handle user sign-up
def sign_up():
    st.header("Sign Up")
    with st.form("sign_up_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Sign Up")

        if submit_button:
            if username and password:
                if username not in st.session_state.users:
                    # Update users dictionary and save to JSON
                    st.session_state.users[username] = password
                    save_users(st.session_state.users)
                    st.success("Signed up successfully! Please log in.")
                else:
                    st.warning("Username already exists.")
            else:
                st.warning("Please fill in all fields.")

# Function to handle user login
def login():
    st.header("Login")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")

        if submit_button:
            users = st.session_state.users
            if username in users and users[username] == password:
                st.session_state.authenticated = True
                st.session_state.current_user = username
                st.success("Logged in successfully!")
                st.rerun()
            else:
                st.error("Invalid username or password.")

# Function to handle user logout
def logout():
    st.session_state.authenticated = False
    st.session_state.current_user = None
    st.success("Logged out successfully!")

# Main application
def main():
    st.sidebar.header("Navigation")
    page = st.sidebar.selectbox("Go to", ["Home", "Dashboard", "Projects"])

    if not st.session_state.authenticated:
        st.sidebar.header("Authentication")
        auth_option = st.sidebar.selectbox("Choose an option", ["Login", "Sign Up"])

        if auth_option == "Sign Up":
            sign_up()
        elif auth_option == "Login":
            login()
    else:
        st.sidebar.header(f"Welcome, {st.session_state.current_user}!")
        st.sidebar.button("Logout", on_click=logout)

        if page == "Home":
            st.switch_page("main_page.py")
        elif page == "Dashboard":
            st.switch_page("pages/dashboard.py")
        elif page == "Projects":
            st.switch_page("pages/find_project.py")

# Run the main application
main()


