import streamlit as st

# Initialize session state for users and authentication
if 'users' not in st.session_state:
    st.session_state.users = {}
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'current_user' not in st.session_state:
    st.session_state.current_user = None
if 'projects' not in st.session_state:
    st.session_state.projects = [
        {"title": "Task Management App", "description": "Develop a mobile application that allows users to create, organize, and track their daily tasks and to-do lists. Features include reminders, priority settings, and integration with calendar apps to help users stay organized and productive.", "skills": "React Native, JavaScript, Redux", "manager": "Alice", "participants": 5},
        {"title": "Portfolio Website", "description": "Design and develop a personalized website for a graphic designer to showcase their portfolio of work. The site should include galleries, project descriptions, and a contact form to facilitate client interactions.", "skills": "HTML, CSS, JavaScript", "manager": "Bob", "participants": 3},
        {"title": "Blogging Platform", "description": "Create a platform where users can write, publish, and share blog posts. Features include user authentication, comment sections, and social sharing options to foster a community of writers and readers.", "skills": "Django, Python, SQL", "manager": "Alice", "participants": 7},
        {"title": "2D Video Game", "description": "Develop a 2D video game for mobile devices with engaging gameplay mechanics and levels. The game should include features like in-app purchases and leaderboards to enhance user engagement.", "skills": "Unity, C#", "manager": "Charlie", "participants": 4},
        {"title": "Social Networking App", "description": "Build a social networking app for professionals to connect, share updates, and collaborate on projects. Features include user profiles, messaging, and group discussions to promote networking and collaboration.", "skills": "Flutter, Dart, Firebase", "manager": "David", "participants": 6},
    ]

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
                st.rerun()  # Refresh the app to reflect login state
            else:
                st.error("Invalid username or password.")

# Function to handle user logout
def logout():
    st.session_state.authenticated = False
    st.session_state.current_user = None
    st.success("Logged out successfully!")

# Main application
def main():
    st.sidebar.header("Navigation")
    page = st.sidebar.selectbox("Go to", ["Home", "Dashboard", "Projects"])

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

        if page == "Home":
            st.header("Home Page")
            st.write("Welcome to the home page!")

        elif page == "Dashboard":
            st.header("My Projects Dashboard")
            # Display managed projects
            managed_projects = [project for project in st.session_state.projects if project["manager"] == st.session_state.current_user]
            if managed_projects:
                for project in managed_projects:
                    st.write(f"**{project['title']}**")
                    st.write(f"Description: {project['description']}")
                    st.write(f"Participants: {project['participants']}")
                    st.write("---")
            else:
                st.write("No managed projects.")

        elif page == "Projects":
            st.header("Available Projects")
            # Display all projects
            for project in st.session_state.projects:
                st.write(f"**{project['title']}**")
                st.write(f"Description: {project['description']}")
                st.write(f"Manager: {project['manager']}")
                st.write(f"Participants: {project['participants']}")
                st.write("---")

# Run the main application
main()

