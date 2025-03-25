import requests
import streamlit as st
import bcrypt
import json

GITHUB_REPO = "Noel6000/linkivity"
USER_FILE = "pages/users.json"

def verify_password(plain_password, hashed_password):
    """Verifies a password against its hash."""
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

def load_users():
    """Fetch users.json from GitHub."""
    url = f"https://raw.githubusercontent.com/{GITHUB_REPO}/main/{USER_FILE}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to load users.")
        return {}

def save_users(users):
    """Save users to JSON file."""
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)  # Pretty-print for easier debugging
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
    {"id": 1, "name": "\"Oh yeah Mr. A\" T-shirt", "image": "quotes.png", "price": 16.00, "description": "The life meme with Mr. A's typical quotes."},
    {"id": 2, "name": "Life EXCLUSIVE T-shirt", "image": "exclusive.png", "price": 20.00, "description": "The exclusive (signed by the GOAT, Mr. A) T-shirt."},
    {"id": 3, "name": "Life keychain", "image": "keychain.jpg", "price": 1.00, "description": "The Mr. A meme keychain."},
    {"id": 4, "name": "GOAT T-shirt", "image": "goat.jpg", "price": 16.00, "description": "The Mr. A T-shirt with \"the GOAT\" meme."},
    {"id": 5, "name": "Original Life MEME T-shirt", "image": "original.png", "price": 16.00, "description": "The original life t-shirt with the Mr. A life meme."}
]
# Function to handle user sign-up
def sign_up():
    """Handles user sign-up."""
    st.header("Sign Up")
    
    with st.form(key='signup_form'):
        username = st.text_input("Username", placeholder="Enter your desired username", key="signup_username")
        password = st.text_input("Password", type="password", placeholder="Enter your password", key="signup_password")
        submit_button = st.form_submit_button(label="Sign Up")

    if submit_button:
        if username and password:
            users = load_users()  # Load existing users

            if username in users:
                st.warning("Username already exists. Try another one.")
            else:
                # ✅ Hash password before saving
                hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

                # ✅ Store user details as a dictionary
                users[username] = {"password": hashed_password}

                save_users(users)  # Save updated users

                # ✅ Update session state
                st.session_state.authenticated = True
                st.session_state.current_user = username
                st.session_state.users = users  # Keep session updated

                st.success("Signed up and logged in successfully!")
                st.session_state.page = "main"
                st.rerun()  # Refresh the page to reflect login state
        else:
            st.warning("Please fill in all fields.")
            
def login():
    st.header("Login")
    with st.form(key='login_form'):
        username = st.text_input("Username", placeholder="Enter your username", key="login_username")
        password = st.text_input("Password", type="password", placeholder="Enter your password", key="login_password")
        submit_button = st.form_submit_button(label="Login")

        if submit_button:
            users = st.session_state.get("users", {})  # Load users safely
            
            user_data = users.get(username)
            
            # ✅ Check if user_data is actually a dictionary
            if not isinstance(user_data, dict):
                st.error("Invalid user data format. Try signing up again.")
                st.stop()
            
            stored_hashed_password = user_data.get("password")  # Now safe to access password
            
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
    # Loop through the list of products and display them in pairs (two per row)
    for i in range(0, len(products), 2):
        # Create two columns for each pair of products
        col1, col2 = st.columns(2)
        
        # Display the first product in the first column
        with col1:
            st.header(products[i]["name"])
            st.image(products[i]["image"], caption=products[i]["name"], width=300)
            st.write(products[i]["description"])
            if not products[i]["reserved"]:
                if st.button(f"Reserve {products[i]['name']}", key=f"reserve_{i}"):
                    # Handle reserve action
                    products[i]["reserved"] = True
                    st.success(f"{products[i]['name']} has been reserved! Please pick it up.")
            else:
                st.success(f"{products[i]['name']} is reserved.")
        
        # Check if there is a second product in the current pair (avoid index errors)
        if i + 1 < len(products):
            # Display the second product in the second column
            with col2:
                st.header(products[i + 1]["name"])
                st.image(products[i + 1]["image"], caption=products[i + 1]["name"], width=300)
                st.write(products[i + 1]["description"])
                if not products[i]["reserved"]:
                    if st.button(f"Reserve {products[i]['name']}", key=f"reserve_{i}"):
                        # Handle reserve action
                        products[i]["reserved"] = True
                        st.success(f"{products[i]['name']} has been reserved! Please pick it up.")
                else:
                    st.success(f"{products[i]['name']} is reserved.")

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
