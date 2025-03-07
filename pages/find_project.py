import json
import streamlit as st

PROJECTS_FILE = "projects.json"

# Load projects from JSON
def load_projects():
    try:
        with open(PROJECTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save projects to JSON
def save_projects(projects):
    with open(PROJECTS_FILE, "w") as file:
        json.dump(projects, file, indent=4)

# Initialize projects
if "projects" not in st.session_state:
    st.session_state.projects = load_projects()

st.header("Create a New Project")

# ✅ Create Project Form
with st.form("new_project_form"):
    title = st.text_input("Project Title")
    description = st.text_area("Project Description")
    skills = st.text_input("Required Skills (comma-separated)")
    submit_button = st.form_submit_button("Create Project")

    if submit_button and title and description and skills:
        # ✅ Define new project dictionary before using it
        new_project = {
            "title": title,
            "description": description,
            "skills": skills.split(","),
            "manager": st.session_state.current_user,  # Assuming the creator is the manager
            "participants": [],
            "requests": [],
        }

        # ✅ Add the new project to session state and save
        st.session_state.projects.append(new_project)
        save_projects(st.session_state.projects)

        st.success(f"Project '{title}' created successfully!")
        st.rerun()  # Refresh the app to update the project list
        
selected_project_title = st.selectbox("Select a project", [p["title"] for p in st.session_state.projects])


if selected_project_title:
    project = find_project_by_title(selected_project_title)  # ✅ Define project

    if project:
        if st.session_state.current_user not in project.get("requests", []):
            st.write("User has not requested to join this project yet.")
        else:
            st.write("User is already in the request list.")
    else:
        st.error("Project not found!")

if st.button("Go to Dashboard"):
    st.switch_page("pages/dashboard.py")

if st.button("Go home"):
    st.switch_page("pages/dashboard.py")

# Ensure user is logged in
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("Please log in to access projects.")
    st.stop()

user_data = st.session_state.users.get(st.session_state.current_user, {})

st.header("Available Projects")

if "projects" in st.session_state and st.session_state.projects:
    selected_project_title = st.selectbox(
        "Select a project",
        [p["title"] for p in st.session_state.projects],
        key="project_selectbox"
    )

    # ✅ Find the selected project
    project = next((p for p in st.session_state.projects if p["title"] == selected_project_title), None)

    if project:
        # ✅ Now we can safely access project
        if st.session_state.current_user not in project.get("requests", []):
            if st.button(f"Request to Join {project['title']}", key=f"join_{project['title']}"):
                project.setdefault("requests", []).append(st.session_state.current_user)
                st.success(f"Requested to join {project['title']}!")

    else:
        st.error("Project not found!")
else:
    st.warning("No projects available.")
    
    # Allow users to request to join
    if st.session_state.current_user not in project.get("requests", []):
        if st.button(f"Request to Join {project['title']}", key=project['title']):
            project.setdefault("requests", []).append(st.session_state.current_user)
            st.success(f"Requested to join {project['title']}!")
    
    st.write("---")

# Form to add new projects
st.subheader("Create a New Project")
with st.form("new_project_form"):
    title = st.text_input("Project Title")
    description = st.text_area("Project Description")
    skills = st.text_input("Required Skills (comma-separated)")
    submit_button = st.form_submit_button("Create Project")

    if submit_button and title and description and skills:
        new_project = {
            "title": title,
            "description": description,
            "skills": skills,
            "manager": st.session_state.current_user,
            "participants": 1,  # Manager is the first participant
            "requests": []
        }
        st.session_state.projects.append(new_project)
        st.success(f"Project '{title}' created successfully!")

st.divider()
def create_project():
    """Allows users to create new projects."""
    st.header("Create a New Project")
    with st.form("create_project_form"):
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
                    "participants": []
                }

                # Load current projects and add new one
                projects = load_projects()
                projects.append(new_project)
                save_projects(projects)

                # Update session state
                st.session_state.projects = projects

                st.success("Project created successfully! Other users can now see it.")
                st.rerun()  # Refresh the page
            else:
                st.warning("Please fill in all fields.")

# Ensure 'projects' exists in session state
if "projects" not in st.session_state:
    st.session_state.projects = load_projects()

# Load existing projects
projects = load_projects()

# Add new project
projects.append(new_project)

# Save updated projects
save_projects(projects)  # ✅ Make sure this is called

# Update session state
st.session_state.projects = projects
st.divider()

# Button to go to the pending approvals page
if st.button("View Pending Approvals"):
    st.header("Pending Approvals")
    if st.session_state.pending_approvals:
        for approval in st.session_state.pending_approvals:
            st.write(f"- {approval}")
    else:
        st.write("No pending approvals.")
st.divider()

# Initialize session state for pending approvals and projects
if 'pending_approvals' not in st.session_state:
    st.session_state.pending_approvals = []
if 'projects' not in st.session_state:
    st.session_state.projects = [
        {"title": "Task Management App, GOOGLE", "description": "Develop a mobile application that allows users to create, organize, and track their daily tasks and to-do lists. Features include reminders, priority settings, and integration with calendar apps to help users stay organized and productive.", "skills": "React Native, JavaScript, Redux"},
        {"title": "Portfolio Website, MICROSOFT", "description": "Design and develop a personalized website for a graphic designer to showcase their portfolio of work. The site should include galleries, project descriptions, and a contact form to facilitate client interactions.", "skills": "HTML, CSS, JavaScript"},
        {"title": "Blogging Platform, NVIDIA", "description": "Create a platform where users can write, publish, and share blog posts. Features include user authentication, comment sections, and social sharing options to foster a community of writers and readers.", "skills": "Django, Python, SQL"},
        {"title": "2D Video Game, SONY", "description": "Develop a 2D video game for mobile devices with engaging gameplay mechanics and levels. The game should include features like in-app purchases and leaderboards to enhance user engagement.", "skills": "Unity, C#"},
        {"title": "Social Networking App, SAMSUNG", "description": "Build a social networking app for professionals to connect, share updates, and collaborate on projects. Features include user profiles, messaging, and group discussions to promote networking and collaboration.", "skills": "Flutter, Dart, Firebase"},
        {"title": "Recommendation System, GOOGLE", "description": "Implement a recommendation system for an e-commerce site that suggests products to users based on their browsing and purchase history. Use machine learning algorithms to improve accuracy and personalize the shopping experience.", "skills": "Python, Machine Learning, Pandas"},
        {"title": "Health Tracking App, EUREKA", "description": "Develop an app that allows users to track their health metrics such as steps, sleep, and heart rate. Features include goal setting, progress tracking, and integration with wearable devices to support health and fitness goals.", "skills": "Swift, iOS, HealthKit"},
        {"title": "E-commerce Website, HP", "description": "Create an online store for selling handmade products. The site should include product listings, a shopping cart, secure payment processing, and order tracking to provide a seamless shopping experience.", "skills": "Shopify, Liquid, HTML, CSS"},
        {"title": "Real-Time Chat App, Marsh & McLennan", "description": "Build a real-time chat application for work teams to communicate and collaborate efficiently. Features include group chats, file sharing, and message history to enhance team productivity.", "skills": "Node.js, Socket.IO, JavaScript"},
        {"title": "Marketing Data Analysis, American Axle & Manufacturing", "description": "Analyze marketing data to help a company understand customer behaviors and preferences. Provide insights and recommendations to improve marketing strategies and drive business growth.", "skills": "Python, Data Analysis, Matplotlib"},
        {"title": "Augmented Reality App, TESLA", "description": "Develop an augmented reality app for educational purposes, allowing students to interact with virtual objects in a real-world environment. Features include 3D models and interactive lessons to enhance learning experiences.", "skills": "ARKit, Swift, iOS"},
        {"title": "Travel Booking Website, C.H. Robinson Worldwide", "description": "Create a website that allows users to book travel packages, flights, and hotels. Features include search filters, user reviews, and secure booking processes to simplify travel planning.", "skills": "Ruby on Rails, JavaScript, PostgreSQL"},
        {"title": "Expense Tracking App, Jabil", "description": "Build an app that helps users track their daily expenses and manage their budget. Features include expense categorization, spending reports, and integration with bank accounts to support financial planning.", "skills": "Kotlin, Android, SQLite"},
        {"title": "Online Learning Platform, American Family Insurance Group", "description": "Develop a platform that offers online courses on various subjects. Features include video lessons, quizzes, and certificates of completion to support continuous learning and skill development.", "skills": "PHP, Laravel, MySQL"},
        {"title": "Fitness Tracking App, CarMax", "description": "Create an app that allows users to track their workout sessions, set fitness goals, and monitor their progress. Features include exercise logs, progress charts, and motivational notifications to support fitness journeys.", "skills": "React Native, JavaScript, Firebase"}
    ]

# Function to handle enrollment for a project
def enroll_in_project(project_title):
    st.session_state.pending_approvals.append(project_title)
    st.success(f"Enrolled in {project_title}. Approval is pending.")
               
# Ensure user is logged in
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("Please log in to find projects.")
    st.stop()

user_data = st.session_state.users.get(st.session_state.current_user, {})

st.title("Available Projects")

# Example: Filter projects based on skills (assuming a project list exists)
matching_projects = [
    p for p in st.session_state.projects if user_data.get("details", "").lower() in p["skills"].lower()
]

if matching_projects:
    for project in matching_projects:
        st.write(f"### {project['title']}")
        st.write(f"**Description:** {project['description']}")
        st.write(f"**Skills:** {project['skills']}")
        st.write("---")
else:
    st.write("No projects match your skills.")


