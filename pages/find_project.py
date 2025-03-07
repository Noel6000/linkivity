import streamlit as st


if st.button("Go to Dashboard"):
    st.switch_page("pages/dashboard.py")

st.divider()
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
                    "skills": skills
                }
                st.session_state.projects.append(new_project)
                st.success("New project created successfully!")
            else:
                st.warning("Please fill in all fields.")

# Button to create a new project
if st.button("Create New Project"):
    create_new_project()

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
        {"title": "Task Management App", "description": "Develop a mobile application that allows users to create, organize, and track their daily tasks and to-do lists. Features include reminders, priority settings, and integration with calendar apps to help users stay organized and productive.", "skills": "React Native, JavaScript, Redux"},
        {"title": "Portfolio Website", "description": "Design and develop a personalized website for a graphic designer to showcase their portfolio of work. The site should include galleries, project descriptions, and a contact form to facilitate client interactions.", "skills": "HTML, CSS, JavaScript"},
        {"title": "Blogging Platform", "description": "Create a platform where users can write, publish, and share blog posts. Features include user authentication, comment sections, and social sharing options to foster a community of writers and readers.", "skills": "Django, Python, SQL"},
        {"title": "2D Video Game", "description": "Develop a 2D video game for mobile devices with engaging gameplay mechanics and levels. The game should include features like in-app purchases and leaderboards to enhance user engagement.", "skills": "Unity, C#"},
        {"title": "Social Networking App", "description": "Build a social networking app for professionals to connect, share updates, and collaborate on projects. Features include user profiles, messaging, and group discussions to promote networking and collaboration.", "skills": "Flutter, Dart, Firebase"},
        {"title": "Recommendation System", "description": "Implement a recommendation system for an e-commerce site that suggests products to users based on their browsing and purchase history. Use machine learning algorithms to improve accuracy and personalize the shopping experience.", "skills": "Python, Machine Learning, Pandas"},
        {"title": "Health Tracking App", "description": "Develop an app that allows users to track their health metrics such as steps, sleep, and heart rate. Features include goal setting, progress tracking, and integration with wearable devices to support health and fitness goals.", "skills": "Swift, iOS, HealthKit"},
        {"title": "E-commerce Website", "description": "Create an online store for selling handmade products. The site should include product listings, a shopping cart, secure payment processing, and order tracking to provide a seamless shopping experience.", "skills": "Shopify, Liquid, HTML, CSS"},
        {"title": "Real-Time Chat App", "description": "Build a real-time chat application for work teams to communicate and collaborate efficiently. Features include group chats, file sharing, and message history to enhance team productivity.", "skills": "Node.js, Socket.IO, JavaScript"},
        {"title": "Marketing Data Analysis", "description": "Analyze marketing data to help a company understand customer behaviors and preferences. Provide insights and recommendations to improve marketing strategies and drive business growth.", "skills": "Python, Data Analysis, Matplotlib"},
        {"title": "Augmented Reality App", "description": "Develop an augmented reality app for educational purposes, allowing students to interact with virtual objects in a real-world environment. Features include 3D models and interactive lessons to enhance learning experiences.", "skills": "ARKit, Swift, iOS"},
        {"title": "Travel Booking Website", "description": "Create a website that allows users to book travel packages, flights, and hotels. Features include search filters, user reviews, and secure booking processes to simplify travel planning.", "skills": "Ruby on Rails, JavaScript, PostgreSQL"},
        {"title": "Expense Tracking App", "description": "Build an app that helps users track their daily expenses and manage their budget. Features include expense categorization, spending reports, and integration with bank accounts to support financial planning.", "skills": "Kotlin, Android, SQLite"},
        {"title": "Online Learning Platform", "description": "Develop a platform that offers online courses on various subjects. Features include video lessons, quizzes, and certificates of completion to support continuous learning and skill development.", "skills": "PHP, Laravel, MySQL"},
        {"title": "Fitness Tracking App", "description": "Create an app that allows users to track their workout sessions, set fitness goals, and monitor their progress. Features include exercise logs, progress charts, and motivational notifications to support fitness journeys.", "skills": "React Native, JavaScript, Firebase"}
    ]

# Function to handle enrollment for a project
def enroll_in_project(project_title):
    st.session_state.pending_approvals.append(project_title)
    st.success(f"Enrolled in {project_title}. Approval is pending.")

# Function to create a new project
# Main page with project listings
st.header("Available Projects")
for project in st.session_state.projects:
    st.write(f"**{project['title']}**")
    st.write(f"Description: {project['description']}")
    st.write(f"Required Skills: {project['skills']}")
    if st.button(f"Enroll in {project['title']}"):
        enroll_in_project(project['title'])
    st.write("---")
    st.divider()

