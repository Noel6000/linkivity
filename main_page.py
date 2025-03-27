import requests
import streamlit as st
import bcrypt
import json
import smtplib

GITHUB_REPO = "Noel6000/linkivity"
USER_FILE = "pages/users.json"

def reserve_product(product_id):
    for product in st.session_state.products:
        if product["id"] == product_id:
            user = st.session_state.current_user or "Guest"
            product["reserved"].append(st.session_state.current_user)
            st.success(f"You reserved {product['name']}.")
            return
            
def pre_reserve_product(product_id):
    for product in st.session_state.products:
        if product["id"] == product_id:
            product["reserved"].append(st.session_state.current_user)
            st.success(f"You have pre-reserved a {product['name']}. We will notify you when it's available.")
    

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
    {"id": 1, "name": "\"Oh yeah Mr. A\" T-shirt", "image": "quotes.png", "price": 16.00, "description": "The \"life\" meme with Mr. A's typical quotes", "available_quantity": 0, "reserved": []},
    {"id": 2, "name": "Life EXCLUSIVE T-shirt", "image": "exclusive.png", "price": 20.00, "description": "The exclusive (signed by Mr. A) T-shirt.", "available_quantity": 0, "reserved": []},
    {"id": 3, "name": "Life keychain", "image": "keychain.jpg", "price": 1.00, "description": "The Mr. A meme keychain.", "available_quantity": 4, "reserved": []},
    {"id": 4, "name": "GOAT T-shirt", "image": "goat.jpg", "price": 16.00, "description": "The Mr. A T-shirt with \"the GOAT\" meme.", "available_quantity": 0, "reserved": []},
    {"id": 5, "name": "Original Life MEME T-shirt", "image": "original.png", "price": 16.00, "description": "The original \"life\" T-shirt with the Mr. A life meme.", "available_quantity": 0, "reserved": []}
]

# Initialize session state if not set
if "products" not in st.session_state:
    st.session_state.products = products  # Load products into session state

if "current_user" not in st.session_state:
    st.session_state.current_user = None  # Ensure current_user exists
def shop():
    st.title("Visit our catalog:")
    st.write("T-shirts are made to order: please send a message at lilian.tillie@sfpaula.com to reserve a T-shirt or Keychain.")
    
    columns = st.columns(2)  # Create two columns
    
    for index, product in enumerate(st.session_state.products):
        with columns[index % 2]:  # Alternate between columns
            st.image(product["image"], caption=product["name"], width=100)
            st.write(f"**{product['name']}** - €{product['price']}")
            st.write(product["description"])
            st.write(f"**Available:** {product['available_quantity']}")
    
 
    
            st.write("--------")  # Separator
    
# Main application
def logout():
    """Logs out the current user by resetting session state."""
    st.session_state.authenticated = False
    st.session_state.current_user = None
    st.rerun()  # Refresh the app to reflect changes

def main():
    shop()


# Run the main application
main()
