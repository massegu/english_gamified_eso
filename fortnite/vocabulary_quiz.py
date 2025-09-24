import streamlit as st
import json

def run():
    st.title("🛡️ FortNITE Vocabulary Quiz")
    st.image("assets/images/shield.png", width=200)
    
    with open("data/vocab_lists.json") as f:
        vocab = json.load(f)["fortnite"]

    word = st.selectbox("Choose a word", list(vocab.keys()))
    if st.button("Show meaning"):
        st.info(vocab[word])
