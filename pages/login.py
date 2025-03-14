import streamlit as st
import json
import os
import requests
import base64
import hashlib
import bcrypt

custom_css = """
<style>
    /* Hide the sidebar */
    [data-testid="stSidebar"] {
        display: none;
    }
    /* Adjust main content area */
    .main > div {
        padding-left: 2rem;
        padding-right: 2rem;
    }
    /* Style buttons */
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        text-align: center;
        font-size: 16px;
        cursor: pointer;
        transition-duration: 0.4s;
    }
    .stButton>button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

def hash_password(password):
    """Hashes a password using bcrypt."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()
    
def verify_password(plain_password, hashed_password):
    """Verifies a password against its hash."""
    print("🔍 Stored hashed password:", repr(hashed_password))  # Debugging step
    print("🔍 Type of hashed_password:", type(hashed_password))  # Check if it's str or bytes

    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode('utf-8')  # Convert string to bytes

    return bcrypt.checkpw(plain_password.encode(), hashed_password)
    
USER_FILE = "pages/users.json"
GITHUB_REPO = "Noel6000/linkivity"
GITHUB_FILE_PATH = "pages/users.json"  # Adjust based on your repo structure
GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    """Load users.json from GitHub and ensure the 'users' key exists."""
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{GITHUB_FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        file_info = response.json()
        content = base64.b64decode(file_info["content"]).decode()
        
        try:
            data = json.loads(content)
        except json.JSONDecodeError:
            data = {}  # 🔹 Fix: If the file is corrupt, reset it
        
        # 🔹 Ensure "users" key exists
        if "users" not in data:
            data["users"] = {}

        return data  
    else:
        return {"users": {}}  # 🔹 Fix: Return a proper structure if file is missing
        # Ensure users are loaded into session state
if "users" not in st.session_state:
    st.session_state.users = load_users()

def save_users(users_data):
    """Save users.json back to GitHub"""
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{GITHUB_FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    # Convert data to JSON
    json_content = json.dumps(users_data, indent=4)
    encoded_content = base64.b64encode(json_content.encode()).decode()

    # Get latest file SHA for updating
    response = requests.get(url, headers=headers)
    sha = response.json().get("sha", None) if response.status_code == 200 else None

    # Update file on GitHub
    data = {
        "message": "Update users.json",
        "content": encoded_content,
        "sha": sha
    }

    response = requests.put(url, headers=headers, json=data)
    
    if response.status_code == 200:
        st.success("User data updated successfully.")
    else:
        st.error("Failed to update users.json on GitHub.")
        
# Function to handle user sign-up
def sign_up():
    st.header("Sign Up")
    with st.form("sign_up_form"):
        username = st.text_input("Username").lower()
        password = st.text_input("Password", type="password")
        email = st.text_input("email")
        submit_button = st.form_submit_button("Sign Up")

        if submit_button:
            users_data = load_users()
            if "users" not in users_data:
                users_data["users"] = {}

            if username and password:
                if username not in users_data["users"]:
                    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

                    users_data["users"][username] = {
                        "password": hashed_password,
                        "email": email
                    }

                    save_users(users_data)  # Save users.json
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
        username = username.lower()  # Convert to lowercase 
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")

        if submit_button:
            users_data = load_users()
            username = username.lower()  # Ensure case-insensitive login

            if username in users_data["users"]:
                stored_password = users_data["users"][username]["password"]
                
                if verify_password(password, stored_password):  # Compare hashed password
                    st.session_state.authenticated = True
                    st.session_state.current_user = username
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
button_container = st.container()
with button_container:
    col1, col2, col3 = st.columns([1, 2, 3])
    with col1:
        ModelIsClicked=st.button("About us",use_container_width=True)
    if ModelIsClicked:
        st.switch_page("pages/about_us.py")
    with col2:
        ModelIsClicked=st.button("Main Page",use_container_width=True)
    if ModelIsClicked:
        st.switch_page("main_page.py")
    with col3:
        ModelIsClicked=st.button("Shop", use_container_width=True)
    if ModelIsClicked:
        st.switch_page("pages/shop.py")
