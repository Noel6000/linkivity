import json
import streamlit as st

PROJECTS_FILE = "pages/projects.json"

# Function to load projects from the JSON file
import json
import subprocess
import os

PROJECTS_FILE = "pages/projects.json"
GITHUB_REPO = "Noel6000/linkivity"  # Change to your repo name

def load_projects():
    try:
        with open("projects.json", "r") as file:
            data = json.load(file)
            return data.get("projects", [])  # ✅ Get the list, not the dictionary
    except FileNotFoundError:
        return []  # ✅ Return an empty list if file is missing

def save_projects(projects):
    with open("projects.json", "w") as file:
        json.dump({"projects": projects}, file, indent=4)  # ✅ Save in correct format

    # GitHub commit and push
    try:
        subprocess.run(["git", "config", "--global", "user.email", "your-email@example.com"], check=True)
        subprocess.run(["git", "config", "--global", "user.name", "your-username"], check=True)

        subprocess.run(["git", "add", PROJECTS_FILE], check=True)
        subprocess.run(["git", "commit", "-m", "Updated projects.json"], check=True)
        subprocess.run(["git", "push", "https://<GITHUB-TOKEN>@github.com/" + GITHUB_REPO + ".git"], check=True)

        print("✅ projects.json updated and pushed to GitHub!")

    except subprocess.CalledProcessError as e:
        print(f"❌ Error pushing to GitHub: {e}")

# Initialize session state for projects
if "projects" not in st.session_state:
    st.session_state.projects = load_projects()

# Function to create a new project
def create_project():
    st.header("Create a New Project")

    with st.form("create_project_form"):
        title = st.text_input("Project Title")
        description = st.text_area("Project Description")
        skills = st.text_input("Required Skills (optional)")
        submit_button = st.form_submit_button("Create Project")

    if submit_button:
        if title and description:  # Ensure required fields are filled
            new_project = {
                "title": title,
                "description": description,
                "skills": skills if skills else "Not specified",
                "manager": st.session_state.current_user,
                "participants": [],
                "requests": []
            }

            # Ensure projects is a list before adding a new project
            projects = load_projects()
            if not isinstance(projects, list):  # If somehow projects is a dict, reset it
                projects = []
            if 'pending_approvals' not in st.session_state:
                st.session_state.pending_approvals = []

            projects = load_projects()  # ✅ projects is now a LIST
            projects.append(new_project)  # ✅ This works because projects is a list
            save_projects(projects)  # ✅ Save back to the JSON file


            st.success(f"Project '{title}' created successfully!")
            st.rerun()

        else:
            st.error("Please fill in all required fields!")

create_project()
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
    p for p in st.session_state.projects if any(
        skill.lower() in p["skills"].lower() for skill in user_data.get("details", [])
    )
]

if matching_projects:
    for project in matching_projects:
        st.write(f"### {project['title']}")
        st.write(f"**Description:** {project['description']}")
        st.write(f"**Skills:** {project['skills']}")
        st.write("---")
else:
    st.write("No projects match your skills.")


