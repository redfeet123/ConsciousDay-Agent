import streamlit as st
from db.db import get_dates, get_by_date, delete_entry
from datetime import datetime
from auth import check_auth
# check_auth()

# Temporary demo login
if "authenticated" not in st.session_state:
    st.session_state.authenticated = True
    st.session_state.username = "demo"

st.set_page_config(page_title="History")
st.caption(f"You are logged in as: **{st.session_state.username}**")
st.title("Past Reflections")

# Fetch dates from DB
dates = get_dates()
if not dates:
    st.info("No entries yet.")
    st.stop()

# Convert string dates to datetime.date objects
date_objects = [datetime.strptime(d, "%Y-%m-%d").date() for d in dates]

# Calendar UI
selected_date = st.date_input(
    "Choose a date",
    value=date_objects[0],
    min_value=min(date_objects),
    max_value=max(date_objects),
    format="DD/MM/YYYY"  # cosmetic
)

# Format date for database query
selected = selected_date.strftime("%Y-%m-%d")

# Get entries for that date
entries = get_by_date(selected)
for entry in entries:
    formatted_date = datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%d/%m/%Y")

    with st.expander(f"Entry #{entry['id']} – {formatted_date}"):
        st.markdown(f"**Intention:**\n{entry['intention']}")
        st.markdown(f"**Priorities:**\n{entry['priorities']}")
        st.markdown(f"**Journal:**\n{entry['journal']}")
        st.markdown(f"**Dream:**\n{entry['dream']}")
        st.markdown("---")
        st.markdown("### Reflection & Strategy")
        st.markdown(entry['reflection'], unsafe_allow_html=True)

        # Add delete button
        if st.button(f"🗑️ Delete Entry #{entry['id']}", key=f"delete_{entry['id']}"):
            delete_entry(entry["id"])
            st.success("Entry deleted. Please refresh the page.")
            st.experimental_rerun()

