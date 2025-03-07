import streamlit as st

# Initialize session state for users and authentication
if 'users' not in st.session_state:
    st.session_state.users = {}
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
                    st.session_state.users[username] = password
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
            if username in st.session_state.users and st.session_state.users[username] == password:
                st.session_state.authenticated = True
                st.session_state.current_user = username
                st.success("Logged in successfully!")
                st.experimental_rerun()  # Refresh the app to reflect login state
            else:
                st.error("Invalid username or password.")

# Function to handle user logout
def logout():
    st.session_state.authenticated = False
    st.session_state.current_user = None
    st.success("Logged out successfully!")

# Main application
if not st.session_state.authenticated:
    st.sidebar.header("Authentication")
    auth_option = st.sidebar.selectbox("Choose an option", ["Login", "Sign Up"])

    if auth_option == "Sign Up":
        sign_up()
    elif auth_option == "Login":
        login()
else:
    st.sidebar.header("Welcome, {}!".format(st.session_state.current_user))
    st.sidebar.button("Logout", on_click=logout)

    # Dashboard page displaying only the user's managed projects
    st.header("My Projects Dashboard")

    # Function to create a new project
    def create_new_project():
        st.header("Create a New Project")
        with st.form("new_project_form"):
            title = st.text_input("Project Title")
            description = st.text_area("Project Description")
            skills = st.text_input("Required Skills (comma-separated)")
            submit_button = st.form_submit_button("Create Project")

            if submit_button:
                if title and description and skills:
                    new_project = {
                        "title": title,
                        "description": description,
                        "skills": skills,
                        "manager": st.session_state.current_user,
                        "participants": 1  # Assuming the manager is the first participant
                    }
                    st.session_state.projects.append(new_project)
                    st.success("New project created successfully!")
                    st.experimental_rerun()  # Refresh the app to reflect changes
                else:
                    st.warning("Please fill in all fields.")

    # Always show the form to create a new project
    create_new_project()

    # Filter projects managed by the user
    managed_projects = [project for project in st.session_state.projects if project["manager"] == st.session_state.current_user]

    # Display managed projects
    if managed_projects:
        for project in managed_projects:
            st.write(f"**{project['title']}**")
            st.write(f"Description: {project['description']}")
            st.write(f"Participants: {project['participants']}")
            st.write("---")
    else:
        st.write("No managed projects.")
