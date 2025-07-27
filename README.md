🧘 ConsciousDay – AI-Powered Daily Reflection App
ConsciousDay is a journaling web app that combines mindful reflection with AI-generated insights. Built using Streamlit, LangChain, and Together AI, the app helps users gain clarity, focus, and intentionality each day through structured journaling and intelligent reflection.

🚀 Features:
📝 Morning Journal: Input your thoughts, dreams, goals, and intentions
🤖 AI-Powered Reflections: LangChain agent analyzes your input using Together AI
💡 Daily Strategy Output: Get personalized advice, energy insights, and suggested strategy
📅 View Past Entries: Browse journal entries using a calendar-based history tab
🔐 Username & Password Login: Protect your journal data using Streamlit session state
💾 SQLite Storage: Local persistence of all entries
🎨 Clean UI: Responsive layout, readable fonts, and intuitive design

🗂️ Project Structure
graphql
Copy
Edit
consciousday/
├── agent/                # LangChain agent logic
│   └── agent.py
├── auth.py               # Simple login system
├── db/                   # Database logic
│   ├── db.py
│   └── schema.sql
├── pages/                # Streamlit multipage files
│   └── 1_📅_History.py
├── app.py                # Main app UI
├── requirements.txt
└── .streamlit/
    └── secrets.toml      # API keys (not pushed to GitHub)

📦 Installation

✅ Prerequisites
Python 3.10 or higher

Together AI API Key (get it from https://api.together.ai)

📥 Clone the Repo
bash
Copy
Edit
git clone https://github.com/yourusername/conscious-day.git
cd conscious-day

🧪 Create Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate   # On macOS/Linux

📦 Install Requirements
bash
Copy
Edit
pip install -r requirements.txt

🔐 Set Up API Key
Inside the .streamlit folder, create a file called secrets.toml:

toml
Copy
Edit
[together]
api_key = "your_together_api_key"

▶️ Run the App
bash
Copy
Edit
streamlit run app.py

🌐 Live Demo
You can access the deployed version here:
https://yourusername-conscious-day.streamlit.app
(Login is optional or disabled for demo purposes)

