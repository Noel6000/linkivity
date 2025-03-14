import streamlit as st

# Initialize session state for users and authentication
if 'users' not in st.session_state:
    st.session_state.users = {}
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'current_user' not in st.session_state:
    st.session_state.current_user = None
if 'page' not in st.session_state:
    st.session_state.page = "main"

# Function to handle user sign-up
def sign_up():
    st.header("Sign Up")
    with st.form(key='signup_form'):
        username = st.text_input("Username", key="signup_username")
        password = st.text_input("Password", type="password", key="signup_password")
        submit_button = st.form_submit_button("Sign Up")

        if submit_button:
            if username and password:
                if username not in st.session_state.users:
                    st.session_state.users[username] = password
                    st.success("Signed up successfully! Please log in.")
                    st.session_state.page = "login"
                    st.experimental_rerun()
                else:
                    st.warning("Username already exists.")
            else:
                st.warning("Please fill in all fields.")

# Function to handle user login
def login():
    st.header("Login")
    with st.form(key='login_form'):
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")
        submit_button = st.form_submit_button("Login")

        if submit_button:
            if username in st.session_state.users and st.session_state.users[username] == password:
                st.session_state.authenticated = True
                st.session_state.current_user = username
                st.success("Logged in successfully!")
                st.session_state.page = "main"
                st.experimental_rerun()  # Refresh the app to reflect login state
            else:
                st.error("Invalid username or password.")

# Function to handle user logout
def logout():
    st.session_state.authenticated = False
    st.session_state.current_user = None
    st.success("Logged out successfully!")
    st.session_state.page = "main"

# Main application
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
                    st.experimental_rerun()
            with col2:
                if st.button("Login", key="main_login_button"):
                    st.session_state.page = "login"
                    st.experimental_rerun()
        else:
            st.title("Main Page")
            st.write(f"Welcome, {st.session_state.current_user}! You are logged in.")
            st.button("Logout", key="logout_button", on_click=logout)
    elif st.session_state.page == "signup":
        sign_up()
    elif st.session_state.page == "login":
        login()

# Run the main application
main()
