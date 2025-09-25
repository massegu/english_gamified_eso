import streamlit as st
from exercises.fortnite import vocabulary_quiz, grammar_challenges
from exercises.real_madrid import match_report_fill, player_profiles
from exercises.fortnite import vocab_gallery  # ← Añade esta línea

def show():
    option = st.sidebar.radio("Selecciona una temática", [
         "FortNITE: Vocabulario",
         "FortNITE: Gramática",
         "FortNITE: Galería con puntuación",  # ← Nueva opción
         "Real Madrid: Crónica",
         "Real Madrid: Jugadores"
])

if option == "FortNITE: Vocabulario":
    vocabulary_quiz.run()
elif option == "FortNITE: Gramática":
    grammar_challenges.run()
elif option == "FortNITE: Galería con puntuación":
    vocab_gallery.run()  # ← Llama al nuevo ejercicio
elif option == "Real Madrid: Crónica":
    match_report_fill.run()
elif option == "Real Madrid: Jugadores":
    player_profiles.run()



