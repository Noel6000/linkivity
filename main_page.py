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


def reserve_product(product_id):
    for product in st.session_state.products:
        if product["id"] == product_id:
            if product["available_quantity"] > 0:
                product["available_quantity"] -= 1
                product["reserved"].append(st.session_state.current_user)
                st.success(f"You reserved a {product['name']}. Pick it up soon!")
            else:
                st.warning(f"No stock available. You can pre-reserve a {product['name']}.")

def pre_reserve_product(product_id):
    for product in st.session_state.products:
        if product["id"] == product_id:
            product["reserved"].append(st.session_state.current_user)
            st.success(f"You have pre-reserved a {product['name']}. We will notify you when it's available.")

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
    {"id": 1, "name": "\"Oh yeah Mr. A\" T-shirt", "image": "quotes.png", "price": 16.00, "description": "The life meme with Mr. A's typical quotes", "available_quantity": 0, "reserved": []},
    {"id": 2, "name": "Life EXCLUSIVE T-shirt", "image": "exclusive.png", "price": 20.00, "description": "The exclusive (signed by the GOAT, Mr. A) T-shirt.", "available_quantity": 0, "reserved": []},
    {"id": 3, "name": "Life keychain", "image": "keychain.jpg", "price": 1.00, "description": "The Mr. A meme keychain.", "available_quantity": 0, "reserved": []},
    {"id": 4, "name": "GOAT T-shirt", "image": "goat.jpg", "price": 16.00, "description": "The Mr. A T-shirt with \"the GOAT\" meme.", "available_quantity": 0, "reserved": []},
    {"id": 5, "name": "Original Life MEME T-shirt", "image": "original.png", "price": 16.00, "description": "The original life t-shirt with the Mr. A life meme.", "available_quantity": 0, "reserved": []}
]

def shop():
st.title("Shop")

columns = st.columns(2)  # Create two columns

for index, product in enumerate(st.session_state.products):
    with columns[index % 2]:  # Alternate between columns
        st.image(product["image"], caption=product["name"], width=200)
        st.write(f"**{product['name']}** - ${product['price']}")
        st.write(product["description"])
        st.write(f"**Available:** {product['available_quantity']}")

        if product["available_quantity"] > 0:
            if st.button(f"Reserve", key=f"reserve_{product['id']}"):
                reserve_product(product["id"])
        else:
            if st.button(f"Pre-Reserve", key=f"prereserve_{product['id']}"):
                pre_reserve_product(product["id"])

        st.write("---")  # Separator

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
shop()


# Run the main application
main()
