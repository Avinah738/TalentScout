import streamlit as st
from openai import OpenAI
from prompts import generate_candidate_info_prompt, generate_technical_questions_prompt
import json
import os
import logging

# Set page configuration at the very beginning
st.set_page_config(page_title="Hiring Assistant Chatbot", layout="wide")

# Configure logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

# Load environment variables
api_key = st.secrets["default"]["OPENAI_API_KEY"]
# api_key = "Enter the actual api key directly here if .env key not working"
client = OpenAI(api_key=api_key)

# File path for simulated storage
DATA_FILE = "candidate_data.json"

# Initialize storage file
def init_storage():
    logging.debug("Checking if storage file exists.")
    if not os.path.exists(DATA_FILE):
        logging.debug("Storage file not found. Creating a new one.")
        with open(DATA_FILE, "w") as file:
            json.dump({"candidates": []}, file)

# Save candidate details
def save_candidate_data(candidate):
    logging.debug(f"Saving candidate data: {candidate}")
    init_storage()
    try:
        with open(DATA_FILE, "r+") as file:
            data = json.load(file)
            data["candidates"].append(candidate)
            file.seek(0)
            json.dump(data, file, indent=4)
        logging.debug("Candidate data saved successfully.")
    except Exception as e:
        logging.error(f"Error saving candidate data: {e}")

# Get all stored data
def get_all_candidates():
    logging.debug("Fetching all candidates from storage.")
    init_storage()
    try:
        with open(DATA_FILE, "r") as file:
            candidates = json.load(file)["candidates"]
            logging.debug(f"Retrieved candidates: {candidates}")
            return candidates
    except Exception as e:
        logging.error(f"Error fetching candidate data: {e}")
        return []
        
st.markdown("""
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f7f8fc;
        color: #333;
    }
    .main-header {
        background: linear-gradient(90deg, #6a11cb 0%, #2575fc 100%);
        color: white;
        padding: 15px 20px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        border-radius: 8px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .subheader1 {
        color: #5e5e5e;
        font-size: 18px;
        text-align: center;
        margin-top: -10px;
        margin-bottom: 30px;
    }  
    
    .subheader_tech {
        font-size: 1.5rem;
        color: #4CAF50;
        margin-top: 20px;
        margin-bottom: 10px;
        font-weight: bold;
    }
    .question {
        background: #f9f9f9;
        padding: 10px 15px;
        margin-bottom: 10px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        font-size: 1.1rem;
    }
    .question:hover {
        background: #e8f5e9;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    }
    
    .conversation-box {
        background: #fff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
        overflow-y: auto;
        max-height: 300px; /* Adjust height as needed */
        font-size: 16px;
        line-height: 1.6;
    }
    .conversation-box div {
        margin-bottom: 10px;
    }
    .conversation-box strong {
        color: #2575fc;
    }
    .footer {
        background: linear-gradient(90deg, #2575fc 0%, #6a11cb 100%);
        color: white;
        padding: 10px;
        text-align: center;
        font-size: 14px;
        margin-top: 50px;
        border-top: 1px solid #ccc;
        border-radius: 8px;
    }
    button {
        background-color: #2575fc !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
    }
    button:hover {
        background-color: #6a11cb !important;
    }
    </style>
""", unsafe_allow_html=True)


# Header Section
st.markdown('<div class="main-header">Hiring Assistant Chatbot</div>', unsafe_allow_html=True)
st.markdown('<p class="subheader1">Welcome to TalentScout\'s Hiring Assistant! Effortlessly collect candidate details and assess technical skills.</p>', unsafe_allow_html=True)

# Candidate Information Form
st.header("Candidate Information")
with st.form(key="candidate_form"):
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    full_name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    location = st.text_input("Current Location")
    experience = st.number_input("Years of Experience", min_value=0, max_value=50, step=1)
    desired_positions = st.text_input("Desired Position(s)")
    tech_stack = st.text_area("Tech Stack (e.g., Python, Django, React)")

    # Submit Button
    submitted = st.form_submit_button("Submit")
    st.markdown('</div>', unsafe_allow_html=True)

if submitted:
    logging.debug("Candidate form submitted.")
    candidate = {
        "full_name": full_name,
        "email": email,
        "phone": phone,
        "location": location,
        "experience": experience,
        "desired_positions": desired_positions,
        "tech_stack": tech_stack,
    }
    save_candidate_data(candidate)
    st.success(f"Thank you, {full_name}! Your information has been recorded.")

    if tech_stack.strip():
        logging.debug("Generating technical questions.")
        with st.spinner("Generating technical questions..."):
            try:
                prompt = generate_technical_questions_prompt(tech_stack)
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "user", "content": prompt}],
                )
                questions = response.choices[0].message.content.strip().split("\n")
                # Display subheader with custom class
                st.markdown('<div class="subheader_tech">Technical Questions</div>', unsafe_allow_html=True)

                # Display questions with custom styling
                for _ , question in enumerate(questions, start=1):
                    st.markdown(
                        f'<div class="question">{question}</div>',
                        unsafe_allow_html=True
                    )

                logging.debug("Technical questions generated successfully.")
            except Exception as e:
                logging.error(f"Error generating technical questions: {e}")
                st.error("There was an error generating questions. Please try again later.")
            else:
                st.warning("Please provide a tech stack to generate technical questions.")

# Chat Area (Dynamic Interaction)
st.header("Chat Area")
st.write("Interact with the chatbot below:")

if "conversation" not in st.session_state:
    st.session_state["conversation"] = []

user_input = st.text_input("Your message:")

if st.button("Send"):
    logging.debug(f"User input received: {user_input}")
    if user_input.strip():
        st.session_state["conversation"].append({"role": "user", "content": user_input})
        with st.spinner("Chatbot is thinking..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                                 {"role": "system", "content": "You are a helpful Hiring Assistant chatbot."}
                             ] + st.session_state["conversation"],
                )
                chatbot_reply = response.choices[0].message.content
                st.session_state["conversation"].append({"role": "assistant", "content": chatbot_reply})
                logging.debug(f"Chatbot reply: {chatbot_reply}")
            except Exception as e:
                logging.error(f"Error in chatbot response generation: {e}")
                chatbot_reply = "Sorry, I couldn't process your message. Please try again later."
                st.session_state["conversation"].append({"role": "assistant", "content": chatbot_reply})
    else:
        st.warning("Please enter a message.")

# Display conversation history
st.subheader("Conversation History")
conversation_html = '<div class="conversation-box">'
for message in st.session_state["conversation"]:
    if message["role"] == "user":
        conversation_html += f'<div><strong>You:</strong> {message["content"]}</div>'
    else:
        conversation_html += f'<div><strong>Chatbot:</strong> {message["content"]}</div>'
conversation_html += '</div>'
st.markdown(conversation_html, unsafe_allow_html=True)


# Data Export
st.header("Candidate Data")
if st.button("View All Candidates"):
    candidates = get_all_candidates()
    st.json(candidates)
    st.download_button(
        label="Download Candidate Data",
        data=json.dumps(candidates, indent=4),
        file_name="candidate_data.json",
        mime="application/json",
    )

# Footer Section
st.markdown('<div class="footer">© 2025 TalentScout Inc. | Designed with ❤️ for modern hiring needs.</div>', unsafe_allow_html=True)
