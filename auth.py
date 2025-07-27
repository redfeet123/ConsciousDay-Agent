import streamlit as st

def check_auth():
    """Username + Password auth"""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "username" not in st.session_state:
        st.session_state.username = ""

    if not st.session_state.authenticated:
        st.subheader("Login Required")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            users = st.secrets["auth"]["users"]
            if username in users and password == users[username]:
                st.session_state.authenticated = True
                st.session_state.username = username
                st.success(f"Welcome, {username}!")

                
                st.rerun()
            else:
                st.error("Invalid username or password")

        st.stop()
