import streamlit as st
from streamlit_app.components import interactive_cards

# Lista de tarjetas
cards = [
    {
        "image": "assets/images/shield.png",
        "word": "Shield",
        "definition": "A protective item that increases your defense.",
        "audio": "assets/fortnite/shield.mp3",
        "question": "What does 'Shield' do?",
        "options": ["Heals you", "Protects you", "Makes you faster"],
        "answer": "Protects you"
    },
    {
        "image": "assets/images/storm.png",
        "word": "Storm",
        "definition": "A dangerous zone that reduces health.",
        "audio": "assets/fortnite/storm.mp3",
        "question": "What happens in the storm?",
        "options": ["You get more loot", "You lose health", "You revive teammates"],
        "answer": "You lose health"
    }
]

# Estado de navegación y puntuación
if "card_index" not in st.session_state:
    st.session_state.card_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0

# Mostrar tarjeta actual
card = cards[st.session_state.card_index]
st.title("🧩 FortNITE Vocabulary Gallery")
interactive_cards.show_card(card["image"], card["word"], card["definition"], card["audio"])

# Pregunta de comprensión
st.write(f"**Pregunta:** {card['question']}")
selected = st.radio("Elige la respuesta:", card["options"])

if st.button("Comprobar respuesta"):
    if selected == card["answer"]:
        st.success("¡Correcto!")
        st.session_state.score += 1
    else:
        st.error(f"No exactamente... Era: **{card['answer']}**")

# Navegación
if st.button("Siguiente tarjeta"):
    if st.session_state.card_index < len(cards) - 1:
        st.session_state.card_index += 1
    else:
        st.warning("¡Has llegado al final de la galería!")

# Mostrar puntuación
st.markdown(f"**Puntuación actual:** {st.session_state.score} puntos")

# Reiniciar
if st.button("Reiniciar sesión"):
    st.session_state.card_index = 0
    st.session_state.score = 0
