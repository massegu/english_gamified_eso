import streamlit as st

def run():
    st.title("👟 Real Madrid Player Profiles")
    st.image("assets/images/vinicius.png", width=250)
    st.write("**Name:** Vinícius Jr.")
    st.write("**Position:** Winger")
    st.write("**Skill:** Speed and dribbling")
    st.markdown("Complete the sentence:")
    st.markdown("*Vinícius is a very ___ player.*")
    adj = st.text_input("Your answer:")
    if st.button("Check"):
        if adj.lower() in ["fast", "skilful", "quick"]:
            st.success("Great choice!")
        else:
            st.warning("Hmm... maybe try a different adjective.")
