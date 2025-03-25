import requests
import streamlit as st
import bcrypt
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Accessing secrets from the secrets file
email = st.secrets["general"]["email"]
password = st.secrets["general"]["password"]
smtp_server = st.secrets["email_service"]["smtp_server"]
smtp_port = st.secrets["email_service"]["smtp_port"]
token = st.secrets["GITHUB_TOKEN"]

def send_email(product_name, recipient_email):
    subject = f"Product Reservation: {product_name}"
    body = f"A user has reserved the {product_name}. Please ensure they pick it up."

    # Create the message
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server using the secrets
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email, password)

        # Send the email
        text = msg.as_string()
        server.sendmail(email, recipient_email, text)

        server.quit()

        st.success(f"Email sent to {recipient_email}")
    except Exception as e:
        st.error(f"Failed to send email: {str(e)}")


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
    {"id": 1, "name": "\"Oh yeah Mr. A\" T-shirt", "image": "quotes.png", "price": 16.00, "description": "The life meme with Mr. A's typical quotes", "reserved": 0},
    {"id": 2, "name": "Life EXCLUSIVE T-shirt", "image": "exclusive.png", "price": 20.00, "description": "The exclusive (signed by the GOAT, Mr. A) T-shirt.", "reserved": 0},
    {"id": 3, "name": "Life keychain", "image": "keychain.jpg", "price": 1.00, "description": "The Mr. A meme keychain.", "reserved": 0},
    {"id": 4, "name": "GOAT T-shirt", "image": "goat.jpg", "price": 16.00, "description": "The Mr. A T-shirt with \"the GOAT\" meme.", "reserved": 0},
    {"id": 5, "name": "Original Life MEME T-shirt", "image": "original.png", "price": 16.00, "description": "The original life t-shirt with the Mr. A life meme.", "reserved": 0}
]
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
                reserve_key = f"reserve_{i}"  # Make key unique by adding index
                if st.button(f"Reserve {products[i]['name']}", key=reserve_key):
                    # Handle reserve action
                    products[i]["reserved"] += 1
                    st.success(f"{products[i]['name']} has been reserved! Please pick it up.")
                    send_email(products[i + 1]["name"], "noelsantiago.briand@gmail.com")
            else:
                st.success(f"{products[i + 1]['name']} is reserved.")
        
        # Check if there is a second product in the current pair (avoid index errors)
        if i + 1 < len(products):
            # Display the second product in the second column
            with col2:
                i += 1
                st.header(products[i]["name"])
                st.image(products[i]["image"], caption=products[i + 1]["name"], width=300)
                st.write(products[i]["description"])
                if not products[i]["reserved"]:
                    reserve_key = f"reserve_{i}"  # Make key unique by adding index
                    if st.button(f"Reserve {products[i]['name']}", key=reserve_key):
                        # Handle reserve action
                        products[i]["reserved"] += 1
                        st.success(f"{products[i]['name']} has been reserved! Please pick it up.")
                        send_email(products[i + 1]["name"], "noelsantiago.briand@gmail.com")
                else:
                    st.success(f"{products[i + 1]['name']} is reserved.")

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
shop()


# Run the main application
main()
