import streamlit as st
import random

isClicked = st.button("main page", use_container_width=True)
if isClicked :
    st.switch_page("main_page.py")

Clicked = st.button("Find a Project", use_container_width=True)
if isClicked :
    st.switch_page("find_project.py")

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

# Dashboard page displaying only the user's managed projects
st.header("My Projects Dashboard")

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

Explanation:

    Filtering: The code filters the list of projects to include only those managed by the current user (Alice in this case).
    Display: The dashboard displays the managed projects, showing the project title, description, and the number of participants.

This setup provides a dashboard for the user to view only the projects they manage. You can further customize the layout and functionality as needed.
