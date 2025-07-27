import streamlit as st
from db.db import get_dates, get_by_date
from datetime import datetime
from auth import check_auth
#check_auth()


# temporary for no login demo mode
if "authenticated" not in st.session_state:
    st.session_state.authenticated = True
    st.session_state.username = "demo"

st.set_page_config(page_title="History")
st.caption(f"You are logged in as: **{st.session_state.username}**")
st.title("Past Reflections")

dates = get_dates()
if not dates:
    st.info("No entries yet.")
    st.stop()

# convert string dates (yyyy-mm-dd) to datetime.date objects
date_objects = [datetime.strptime(d, "%Y-%m-%d").date() for d in dates]

selected_date = st.date_input(
    "Choose a date",
    value=date_objects[0],
    min_value=min(date_objects),
    max_value=max(date_objects),
    format="DD/MM/YYYY"  # this is cosmetic. Streamlit may ignore it but its future proof
)

# convert to string for db query
selected = selected_date.strftime("%Y-%m-%d")


entries = get_by_date(selected)
for entry in entries:

    formatted_date = datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%d/%m/%Y")

    with st.expander(f"Entry #{entry['id']} – {formatted_date}"):
        st.markdown(f"**Intention:** {entry['intention']}")
        st.markdown(f"**Priorities:** {entry['priorities']}")
        st.markdown(f"**Journal:** {entry['journal']}")
        st.markdown(f"**Dream:** {entry['dream']}")
        st.markdown("---")
        st.markdown(f"### Reflection & Strategy\n\n{entry['reflection']}")
