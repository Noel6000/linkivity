import streamlit as st
import json
import os

USER_FILE = "pages/users.json"
GITHUB_REPO = "Noel6000/linkivity"
GITHUB_FILE_PATH = "pages/users.json"  # Adjust based on your repo structure
GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
import streamlit as st
import json
import requests
import base64
import hashlib

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    """Load users.json from GitHub"""
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{GITHUB_FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        file_info = response.json()
        content = base64.b64decode(file_info["content"]).decode()
        return json.loads(content)["users"]  # Return only the users dictionary
    else:
        return {}  # Default empty dict if file is missing

# Ensure users are loaded into session state
if "users" not in st.session_state:
    st.session_state.users = load_users()

def save_users(data):
    """Save users.json and push to GitHub"""
    json_data = json.dumps(data, indent=4)

    # Get current file SHA from GitHub
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{GITHUB_FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        file_info = response.json()
        sha = file_info["sha"]  # Required for updates
    else:
        sha = None  # If file doesn’t exist, create it

    # Prepare the update request
    payload = {
        "message": "Update users.json",
        "content": base64.b64encode(json_data.encode()).decode(),  # Encode to Base64
        "branch": "main"  # Adjust branch if needed
    }
    
    if sha:
        payload["sha"] = sha  # Required when updating an existing file

    # Push update to GitHub
    response = requests.put(url, headers=headers, json=payload)

    if response.status_code in [200, 201]:
        st.success("✅ users.json updated on GitHub successfully!")
    else:
        st.error(f"❌ Error updating GitHub: {response.json()}")
        
# Function to handle user sign-up
def sign_up():
    st.header("Sign Up")
    with st.form("sign_up_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        full_name = st.text_input("Full Name")
        experience = st.text_area("Experience")
        details = st.text_area("Details")
        submit_button = st.form_submit_button("Sign Up")

        if submit_button:
            users_data = load_users()  # Load current users from GitHub
            
            if username and password:
                if username not in users_data["users"]:
                    users_data["users"][username] = {
                        "password": hash_password(password),  # 🔹 Store hashed password
                        "full_name": full_name,
                        "experience": experience,
                        "details": details,
                        "projects": []
                    }
                    save_users(users_data)  # Save updated users.json
                    st.success("Signed up successfully! Please log in.")
                else:
                    st.warning("Username already exists.")
            else:
                st.warning("Please fill in all fields.")

if 'users' not in st.session_state:
    st.session_state.users = load_users()

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if 'current_user' not in st.session_state:
    st.session_state.current_user = None

# Debugging: Check if username and password exist# Function to handle user login
def login():
    st.header("Login")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")

        if submit_button:
            users = load_users()  # Always load latest users

            if username in users:
                stored_password = users[username]["password"]
                
                # 🔹 If passwords are stored in plaintext:
                if stored_password == password:
                    st.session_state.authenticated = True
                    st.session_state.current_user = username
                    st.success(f"Logged in successfully! Welcome, {users[username]['full_name']}")
                    st.rerun()
                else:
                    st.error("Invalid password.")
            else:
                st.error("Username not found.")

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
