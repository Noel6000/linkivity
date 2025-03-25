import requests
import streamlit as st
import bcrypt
import json

GITHUB_REPO = "Noel6000/linkivity"
USER_FILE = "pages/users.json"

def load_users():
    """Fetch users.json from GitHub."""
    url = f"https://raw.githubusercontent.com/{GITHUB_REPO}/main/{USER_FILE}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to load users.")
        return {}
# Initialize session state for users and authentication
if 'users' not in st.session_state:
    st.session_state.users = {}
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'current_user' not in st.session_state:
    st.session_state.current_user = None
if 'page' not in st.session_state:
    st.session_state.page = "main"

    
products = [
    {"id": 1, "name": "\"Oh yeah Mr. A\" T-shirt", "price": 16.00, "description": "The life meme with Mr. A's typical quotes."},
    {"id": 2, "name": "Life EXCLUSIVE T-shirt", "price": 20.00, "description": "The exclusive (signed by the GOAT, Mr. A) T-shirt."},
    {"id": 3, "name": "Life keychain", "price": 1.00, "description": "The Mr. A meme keychain."},
    {"id": 4, "name": "GOAT T-shirt", "price": 16.00, "description": "The Mr. A T-shirt with \"the GOAT\" meme."},
    {"id": 5, "name": "Original Life MEME T-shirt", "price": 16.00, "description": "The original life t-shirt with the Mr. A life meme."}
]
# Function to handle user sign-up
def sign_up():
    st.header("Sign Up")
    with st.form(key='signup_form'):
        username = st.text_input("Username", placeholder="Enter your desired username", key="signup_username")
        password = st.text_input("Password", type="password", placeholder="Enter your password", key="signup_password")
        submit_button = st.form_submit_button(label="Sign Up")

        if submit_button:
            if username and password:
                if username not in st.session_state.users:
                    st.session_state.users[username] = password
                    with open(USER_FILE, "w") as file:
                        json.dump(st.session_state.users, file)
                        st.write("Users saved to JSON file.")
                    st.session_state.authenticated = True
                    st.session_state.current_user = username
                    st.success("Signed up and logged in successfully!")
                    st.session_state.page = "main"
                    st.rerun()
                else:
                    st.warning("Username already exists.")
            else:
                st.warning("Please fill in all fields.")

                
# Function to handle user login
def login():
    st.header("Login")
    with st.form(key='login_form'):
        username = st.text_input("Username", placeholder="Enter your username", key="login_username")
        password = st.text_input("Password", type="password", placeholder="Enter your password", key="login_password")
        submit_button = st.form_submit_button(label="Login")

        if submit_button:
            users = st.session_state.get("users", {})  # Ensure users are loaded properly
            
            user_data = users.get(username)  # ✅ Ensure we get a dictionary
            if not isinstance(user_data, dict):
                st.error("Invalid user data format.")
                st.stop()  # Prevent further execution
            
            stored_hashed_password = user_data.get("password")  # ✅ Now safely extract password
            
            if verify_password(password, stored_hashed_password):
                st.session_state.authenticated = True
                st.session_state.current_user = username
                st.session_state.page = "main"
                st.rerun()
            else:
                st.error("Invalid username or password.")
    
def shop():
    st.title("Shop Page")
    st.write(f"Welcome to the shop, {st.session_state.current_user}!")
    st.write("Here you can browse and purchase items.")
    # Add shop-related content here
    # Display available products
    st.header("Available Products")
    for product in products:
        st.write(f"**{product['name']}**")
        st.write(f"Price: €{product['price']:.2f}")
        st.write(f"Description: {product['description']}")
        st.write("---")

# Main application
def logout():
    """Logs out the current user by resetting session state."""
    st.session_state.authenticated = False
    st.session_state.current_user = None
    st.rerun()  # Refresh the app to reflect changes

def main():
    if st.session_state.page == "main":
        if not st.session_state.authenticated:
            st.title("Welcome to Our Shopping Page!")
            st.write("To access our features, please sign up or log in.")

            # Sign-up and Login buttons
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Sign Up", key="main_signup_button"):
                    st.session_state.page = "signup"
                    st.rerun()
            with col2:
                if st.button("Login", key="main_login_button"):
                    st.session_state.page = "login"
                    st.rerun()
        else:
            shop()
    elif st.session_state.page == "signup":
        sign_up()
    elif st.session_state.page == "login":
        login()

# Run the main application
main()
# Display logout button only if user is logged in
if st.session_state.get("authenticated", False):
    st.sidebar.button("Logout", on_click=logout)  # Place it in the sidebar
