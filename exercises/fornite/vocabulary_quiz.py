import streamlit as st
import json
from streamlit_app.components import interactive_cards

def run():
    st.title("🛡️ Vocabulario FortNITE")
    
    interactive_cards.show_card(
        image_path="assets/images/shield.png",
        word="Shield",
        definition="A protective item that increases your defense.",
        audio_path="assets/fortnite/shield.mp3"
    )

    interactive_cards.show_card(
        image_path="assets/images/storm.png",
        word="Storm",
        definition="A dangerous zone that reduces health.",
        audio_path="assets/fortnite/storm.mp3"
    )


def run():
    st.title("🛡️ FortNITE Vocabulary Quiz")
    st.image("assets/images/shield.png", width=200)
    
    with open("data/vocab_lists.json") as f:
        vocab = json.load(f)["fortnite"]

    word = st.selectbox("Choose a word", list(vocab.keys()))
    if st.button("Show meaning"):
        st.info(vocab[word])
