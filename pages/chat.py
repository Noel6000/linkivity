import streamlit as st
import json
import datetime

USER_FILE = "users.json"  # Ensure this is your actual file

# Load user data
def load_users():
    try:
        with open(USER_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"projects": []}

# Save user data
def save_users(data):
    with open(USER_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Ensure user is authenticated
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("Please log in to access the chat.")
    st.stop()

users_data = load_users()
current_user = st.session_state.current_user

st.title("Project Chat")

# Get projects where the user is a participant
user_projects = [p for p in users_data["projects"] if current_user in p["participants"]]

if not user_projects:
    st.info("You're not part of any projects yet.")
    st.stop()

# Select a project
project_title = st.selectbox("Select a project", [p["title"] for p in user_projects])

# Ensure project is selected before proceeding
if project_title:
    project = next((p for p in users_data["projects"] if p["title"] == project_title), None)
    
    if project:
        st.subheader(f"Chat for {project_title}")

        # Display chat messages
        st.write("### Chat History")
        for message in project.get("chat", []):
            st.write(f"**{message['sender']}** ({message['timestamp']}): {message['message']}")

        # Input field for new messages
        message = st.text_input("Type your message")

        if st.button("Send"):
            if message:
                new_message = {
                    "sender": current_user,
                    "message": message,
                    "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                }
                project.setdefault("chat", []).append(new_message)
                save_users(users_data)
                st.rerun()  # Refresh chat
