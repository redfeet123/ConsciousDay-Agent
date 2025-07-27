import os
os.environ["STREAMLIT_WATCH_USE_POLLING"] = "true"
import streamlit as st
from dotenv import load_dotenv
from datetime import date
from agent.agent import run_agent
from db.db import init_db, insert_entry
from auth import check_auth
#check_auth()
today = date.today()  

# temporary for no login demo mode
if "authenticated" not in st.session_state:
    st.session_state.authenticated = True
    st.session_state.username = "demo"


load_dotenv()
if "TOGETHER_API_KEY" in st.secrets:
    os.environ["TOGETHER_API_KEY"] = st.secrets["TOGETHER_API_KEY"]

st.set_page_config(page_title="Conscious Day Agent", layout="centered")
st.caption(f"You are logged in as: **{st.session_state.username}**")
st.title("Conscious Day Agent")

init_db()

with st.form("reflection_form"):
    # today = st.date_input("Date", value=date.today())
    journal = st.text_area("Morning Journal", height=150)
    dream = st.text_area("Dream", height=100)
    intention = st.text_input("Intention of the Day")
    priorities = st.text_area("Top 3 Priorities of the Day (comma or newline-separated)")

    submitted = st.form_submit_button("Generate Reflection & Strategy")

if submitted:
    if not any([journal.strip(), dream.strip(), intention.strip(), priorities.strip()]):
        st.warning("Please fill in at least one field.")
        st.stop()

    with st.spinner("Thinking..."):
        try:
            response = run_agent(journal, intention, dream, priorities)
        except Exception as e:
            st.error(f"Agent failed: {e}")
            st.stop()

    st.subheader("AI Reflection & Strategy")
    st.markdown()

    entry_id = insert_entry({
        "date": today.isoformat(),
        "journal": journal,
        "intention": intention,
        "dream": dream,
        "priorities": priorities,
        "reflection": response,
        "strategy": response,
    })

    formatted_date = today.strftime("%d/%m/%Y")
    st.success(f"Entry #{entry_id} saved for {formatted_date}")
