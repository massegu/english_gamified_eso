import streamlit as st

def show_card(image_path, word, definition, audio_path=None):
    st.image(image_path, width=200)
    st.write(f"**Palabra:** {word}")
    
    if st.button(f"¿Qué significa '{word}'?"):
        st.info(definition)
    
    if audio_path:
        st.audio(audio_path)
