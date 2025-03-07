import streamlit as st
import json
import os

USER_FILE = "users.json"

# Function to load user data from JSON file
def load_users():
    if os.path.exists(USER_FILE):
        try:
            with open(USER_FILE, "r") as file:
                data = file.read().strip()
                return json.loads(data) if data else {}
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
    return {}

# Function to save user data to JSON file
def save_users(users):
    with open(users, "w") as file:
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
        full_name = st.text_input("Full Name")
        experience = st.text_area("Experience")
        details = st.text_area("Additional Details (Bio, Skills, etc.)")
        submit_button = st.form_submit_button("Sign Up")

        if submit_button:
            if username and password and full_name:
                if username not in st.session_state.users:
                    # Store user details in JSON
                    st.session_state.users[username] = {
                        "password": password,
                        "full_name": full_name,
                        "experience": experience,
                        "details": details,
                        "projects": []  # Each user can have their own projects
                    }
                    save_users(st.session_state.users)
                    st.success("Signed up successfully! Please log in.")
                else:
                    st.warning("Username already exists.")
            else:
                st.warning("Please fill in all required fields.")

# Function to handle user login
def login():
    st.header("Login")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")

        if submit_button:
            users = st.session_state.users
            if username in users and users[username]["password"] == password:
                st.session_state.authenticated = True
                st.session_state.current_user = username
                st.success(f"Logged in successfully! Welcome, {users[username]['full_name']}")
                st.rerun()
            else:
                st.error("Invalid username or password.")

# Function to handle user logout
def logout():
    st.session_state.authenticated = False
    st.session_state.current_user = None
    st.success("Logged out successfully!")
    st.rerun()

# Function to show personalized content
# Main application
def main():
    col1, col2 = st.columns([1, 30])  # Move login/logout to top-right

    with col2:
        if st.session_state.authenticated:
            st.button("Logout", on_click=logout)
        else:
            auth_option = st.selectbox("Authentication", ["Login", "Sign Up"])
            if auth_option == "Login":
                login()
            else:
                sign_up()

# Run the main application
main()
