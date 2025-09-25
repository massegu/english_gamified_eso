import streamlit as st
import os

def show_card(image_path, word, definition, audio_path=None):
    default_image = "assets/images/personaje_1.png"
    
    if os.path.exists(image_path):
        st.image(image_path, width=200)
    else:
        st.image(default_image, width=200)
        st.warning(f"⚠️ Imagen no encontrada: {image_path}")
    
    st.write(f"**Palabra:** {word}")
    
    if st.button(f"¿Qué significa '{word}'?"):
        st.info(definition)
    
    if audio_path and os.path. exists(audio_path):
        st.audio(audio_path)



