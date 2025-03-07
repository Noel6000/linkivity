import json
import streamlit as st
import requests
import base64

GITHUB_REPO = "Noel6000/linkivity"
GITHUB_FILE_PATH = "pages/projects.json"  # Adjust based on your repo structure
GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
# Function to load projects from the JSON file
import json
import subprocess
import os
PROJECTS_FILE = "pages/projects.json"
GITHUB_REPO = "Noel6000/linkivity"  # Change to your repo name
import json

import streamlit as st

def load_projects():
    """Load projects from JSON file."""
    with open(PROJECTS_FILE, "r") as file:
        projects = json.load(file)
        return projects

if "projects" not in st.session_state:
    st.session_state.projects = load_projects()  # Load from JSON

if "current_user" not in st.session_state:
    st.session_state.current_user = None  # Or set to a default user if needed


# Initialize projects in session state properly
for project in st.session_state.projects:
    if isinstance(project, dict) and "manager" in project:
        if project["manager"] == st.session_state.current_user:
            st.write(f"### {project['title']}")
            st.write(f"**Participants:** {project['participants']}")
    else:
        st.warning("Invalid project data format.")

def save_projects(users_data):
    """Save users.json back to GitHub"""
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{GITHUB_FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    # Convert data to JSON
    json_content = json.dumps(users_data, indent=4)
    encoded_content = base64.b64encode(json_content.encode()).decode()

    # Get latest file SHA for updating
    response = requests.get(url, headers=headers)
    sha = response.json().get("sha", None) if response.status_code == 200 else None

    # Update file on GitHub
    data = {
        "message": "Update projects.json",
        "content": encoded_content,
        "sha": sha
    }

    response = requests.put(url, headers=headers, json=data)
    
    if response.status_code == 200:
        st.success("User data updated successfully.")
    else:
        st.error("Failed to update projects.json on GitHub.")
        
# Initialize session state for projects
if "projects" not in st.session_state:
    st.session_state.projects = load_projects()

# Function to create a new project
def create_project():
    st.header("Create a New Project")
    
    with st.form("create_project_form"):
        title = st.text_input("Project Title")
        description = st.text_area("Project Description")
        submit_button = st.form_submit_button("Create Project")

    if submit_button and title and description:
        if "current_user" not in st.session_state or not st.session_state.current_user:
            st.error("You must be logged in to create a project.")
            return

        new_project = {
            "title": title,
            "description": description,
            "manager": st.session_state.current_user,  # ✅ Set current user as manager
            "participants": [st.session_state.current_user],  # ✅ Add manager as participant
            "requests": [],
        }

        # Load existing projects
        projects = load_projects()
        projects.append(new_project)
        save_projects(projects)

        # Update session state
        st.session_state.projects = projects
        st.success(f"Project '{title}' created successfully!")
        st.rerun()

create_project()
st.divider()

st.title("Find a Project")
def find_projects():
    st.header("Find a Project")

    projects = load_projects()

    if not projects:
        st.warning("No projects available.")
        return

    for project in projects:
        # Skip projects where the user is already a participant
        if st.session_state.current_user in project.get("participants", []):
            continue

        st.write(f"## {project['title']}")
        st.write(f"**Description:** {project['description']}")

        # Check if the user already requested to join
        if st.session_state.current_user in project.get("requests", []):
            st.info("Request sent ✅")
        else:
            if st.button(f"Request to Join {project['title']}", key=f"request_{project['title']}"):
                project.setdefault("requests", []).append(st.session_state.current_user)
                save_projects(projects)
                st.success(f"Requested to join {project['title']}!")
                st.rerun()  # Refresh to reflect changes


# Load projects
projects = load_projects()  # Ensure this function correctly loads `projects.json`
find_projects()
