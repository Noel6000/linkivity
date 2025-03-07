import streamlit as st
import random


# Check if the user is authenticated
if not st.session_state.get('authenticated'):
    st.error("You must be logged in to view this page.")
    st.stop()


isClicked = st.button("main page", use_container_width=True)
if isClicked:
    st.switch_page("main_page.py")

Clixed = st.button("Find a Project", use_container_width=True)
if Clixed:
    st.switch_page("pages/find_project.py")

st.divider()
# Initialize session state for projects and user management
if 'projects' not in st.session_state:
    st.session_state.projects = [
        {"title": "Task Management App", "description": "Develop a mobile application that allows users to create, organize, and track their daily tasks and to-do lists. Features include reminders, priority settings, and integration with calendar apps to help users stay organized and productive.", "skills": "React Native, JavaScript, Redux", "manager": "Alice", "participants": 5},
        {"title": "Portfolio Website", "description": "Design and develop a personalized website for a graphic designer to showcase their portfolio of work. The site should include galleries, project descriptions, and a contact form to facilitate client interactions.", "skills": "HTML, CSS, JavaScript", "manager": "Bob", "participants": 3},
        {"title": "Blogging Platform", "description": "Create a platform where users can write, publish, and share blog posts. Features include user authentication, comment sections, and social sharing options to foster a community of writers and readers.", "skills": "Django, Python, SQL", "manager": "Alice", "participants": 7},
        {"title": "2D Video Game", "description": "Develop a 2D video game for mobile devices with engaging gameplay mechanics and levels. The game should include features like in-app purchases and leaderboards to enhance user engagement.", "skills": "Unity, C#", "manager": "Charlie", "participants": 4},
        {"title": "Social Networking App", "description": "Build a social networking app for professionals to connect, share updates, and collaborate on projects. Features include user profiles, messaging, and group discussions to promote networking and collaboration.", "skills": "Flutter, Dart, Firebase", "manager": "David", "participants": 6},
    ]

if 'user' not in st.session_state:
    st.session_state.user = {"name": "Alice"}

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
                    "manager": st.session_state.user["name"],
                    "participants": 1  # Assuming the manager is the first participant
                }
                st.session_state.projects.append(new_project)
                st.success("New project created successfully!")
                st.experimental_rerun()  # Rerun the app to reflect changes
            else:
                st.warning("Please fill in all fields.")

# Dashboard page displaying only the user's managed projects
st.header("My Projects Dashboard")


user_data = st.session_state.users.get(st.session_state.current_user, {})

st.title(f"Welcome, {user_data.get('full_name', 'User')}!")

st.subheader("Your Projects")
for project in st.session_state.projects:
    if project["manager"] == st.session_state.current_user:
        st.write(f"### {project['title']}")
        st.write(f"**Participants:** {project['participants']}")

        # Approve or Reject Requests
        if project["requests"]:
            st.subheader("Join Requests")
            for user in project["requests"]:
                col1, col2 = st.columns(2)
                col1.write(f"- {user}")
                if col2.button(f"Approve {user}", key=f"approve_{user}_{project['title']}"):
                    project["participants"] += 1
                    project["requests"].remove(user)
                    st.success(f"Approved {user} for {project['title']}.")
                elif col2.button(f"Reject {user}", key=f"reject_{user}_{project['title']}"):
                    project["requests"].remove(user)
                    st.warning(f"Rejected {user} for {project['title']}.")
# Filter projects managed by the user
managed_projects = [project for project in st.session_state.projects if project["manager"] == st.session_state.user["name"]]

# Display managed projects
if managed_projects:
    for project in managed_projects:
        st.write(f"**{project['title']}**")
        st.write(f"Description: {project['description']}")
        st.write(f"Participants: {project['participants']}")
        st.write("---")
else:
    st.write("No managed projects.")

# Remove Participants
st.subheader("Manage Participants")
for participant in user_data.get("projects", {}).get(project["title"], []):
    if participant != project["manager"]:  # Managers can't remove themselves
        if st.button(f"Remove {participant}", key=f"remove_{participant}_{project['title']}"):
            project["participants"] -= 1
            user_data["projects"][project["title"]].remove(participant)
            st.success(f"Removed {participant} from {project['title']}.")

import streamlit as st

# Ensure user is logged in
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("Please log in to access the dashboard.")
    st.stop()

# Get the logged-in user's data
user_data = st.session_state.users.get(st.session_state.current_user, {})

st.title(f"Welcome, {user_data.get('full_name', 'User')}!")

st.subheader("Your Experience")
st.write(user_data.get("experience", "No experience added yet."))

st.subheader("Your Details")
st.write(user_data.get("details", "No details added yet."))

