import streamlit as st

def run():
    st.title("⚽ Real Madrid Match Report")
    st.image("assets/images/bernabeu.jpg", width=300)
    st.markdown("Yesterday, Real Madrid ___ the match against Barcelona.")
    verb = st.selectbox("Choose the correct verb", ["wins", "won", "winned"])
    if st.button("Check"):
        if verb == "won":
            st.success("Correct!")
        else:
            st.error("Try again.")
