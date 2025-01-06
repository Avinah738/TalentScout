# Hiring Assistant Chatbot

## **Overview**
The Hiring Assistant Chatbot is a Streamlit-based application designed to assist recruitment agencies by gathering candidate information, generating tailored technical interview questions, and facilitating context-aware chat interactions. This project demonstrates the use of OpenAI's GPT model to simulate intelligent conversations while maintaining a secure and user-friendly interface.

---

## **Features**

### 1. **Candidate Information Collection**
- Collects essential details such as:
  - Full Name
  - Email Address
  - Phone Number
  - Current Location
  - Years of Experience
  - Desired Positions
  - Tech Stack (e.g., programming languages, frameworks, tools)

### 2. **Technical Question Generation**
- Dynamically generates 3-5 technical interview questions based on the candidate’s specified tech stack using OpenAI’s language model.

### 3. **Context-Aware Chat Interactions**
- Facilitates seamless conversations between users and the chatbot with:
  - Real-time responses.
  - Stored conversation history for context management.

### 4. **Data Handling and Export**
- Securely stores candidate information in a local JSON file.
- Allows users to view and download all stored data for further analysis.

### 5. **User-Friendly Interface**
- Built using Streamlit for an intuitive and visually appealing interface.
- Interactive elements include forms, buttons, and live feedback.

---

## **Installation Instructions**

### Prerequisites
- Python 3.8 or higher installed.
- OpenAI API Key.
- Basic knowledge of running Python scripts.

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Avinah738/TalentScout.git
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   .\venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=
     ```

5. **Run the Application**
   ```bash
   streamlit run app.py
   ```
   This will open the application in your default web browser.

---

## **Usage Guide**

### 1. **Launching the Application**
- Navigate to the URL provided by Streamlit after running the app (typically `http://localhost:8501/`).

### 2. **Using the Chatbot**

#### Step 1: Fill in Candidate Information
- Enter your details in the form fields provided under the "Candidate Information" section.
- Click **Submit** to save the information and proceed.

#### Step 2: View Technical Questions
- Based on the tech stack provided, the chatbot will generate relevant technical questions.
- Review these questions under the "Technical Questions" section.

#### Step 3: Chat with the Bot
- Use the text input box in the "Chat Area" to interact with the chatbot.
- The chatbot will respond to your queries, maintaining the context of the conversation.

#### Step 4: View or Download Candidate Data
- Click **View All Candidates** to see all stored data in JSON format.
- Use the **Download Candidate Data** button to save the data locally.

---

## **Technical Details**

### **Technologies Used**
- **Streamlit**: For the frontend interface.
- **OpenAI GPT**: For generating dynamic and context-aware responses.
- **Python**: Core programming language for backend logic.
- **JSON**: For storing candidate data securely.

### **File Structure**
```
hiring_assistant/
├── app.py              # Main application file
├── prompts.py          # Prompt generation logic
├── utils.py            # Utility functions for data handling
├── requirements.txt    # List of dependencies
├── .env                # Environment variables
├── candidate_data.json # Local storage for candidate information
```

### **Core Libraries**
- `streamlit`
- `openai`
- `python-dotenv`
- `json`

---

## **Prompt Design**

### Candidate Information Prompt
```text
You are a Hiring Assistant chatbot. Your task is to collect the following information from the candidate:
- Full Name
- Email Address
- Phone Number
- Current Location
- Years of Experience
- Desired Positions
- Tech Stack (e.g., programming languages, frameworks, tools)

Ensure the candidate feels comfortable and guided during the process. Respond in a conversational tone.
```

### Technical Questions Prompt
```text
The candidate has the following tech stack: {tech_stack}.
Generate 3-5 technical interview questions to assess their proficiency.
Ensure the questions are relevant, challenging, and cover a variety of concepts.
```

---

## **Challenges & Solutions**

### Challenge 1: Maintaining Conversation Context
- **Solution**: Used `st.session_state` in Streamlit to store and manage conversation history.

### Challenge 2: Secure Data Handling
- **Solution**: Used a local JSON file with proper initialization and locking mechanisms to ensure data integrity.

### Challenge 3: Error Handling for API Calls
- **Solution**: Added try-except blocks to gracefully handle API failures and provide meaningful feedback to users.

---

## **Future Enhancements**

1. **Cloud Deployment**:
   - Deploy the chatbot on platforms like AWS or Heroku for public accessibility.
2. **Advanced Features**:
   - Add sentiment analysis to assess candidate emotions during interactions.
   - Support multilingual interactions.
3. **Database Integration**:
   - Replace JSON storage with a scalable database like PostgreSQL or MongoDB.

---

## **Acknowledgements**
- OpenAI for their GPT model.
- Streamlit for providing an intuitive framework for building interactive applications.

---

## **Contact**
For queries or issues, please contact:
- **Email**: raghuvanshiavinash8@gmail.com
- **GitHub Repository**: https://github.com/Avinah738/TalentScout.git

