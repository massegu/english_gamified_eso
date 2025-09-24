import streamlit as st
from exercises.fortnite import vocabulary_quiz, grammar_challenges
from exercises.real_madrid import match_report_fill, player_profiles

def show():
    st.sidebar.title("🎮 Menú de ejercicios")
    option = st.sidebar.radio("Selecciona una temática", [
        "FortNITE: Vocabulario",
        "FortNITE: Gramática",
        "Real Madrid: Crónica",
        "Real Madrid: Jugadores"
    ])

    if option == "FortNITE: Vocabulario":
        vocabulary_quiz.run()
    elif option == "FortNITE: Gramática":
        grammar_challenges.run()
    elif option == "Real Madrid: Crónica":
        match_report_fill.run()
    elif option == "Real Madrid: Jugadores":
        player_profiles.run()
