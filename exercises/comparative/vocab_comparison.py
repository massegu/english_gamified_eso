import streamlit as st

# Diccionario de palabras comparadas
vocab_pairs = {
    "shield": "goalkeeper",
    "storm": "rival team",
    "revive": "substitute",
    "loot": "ball possession",
    "ramp": "counterattack"
}

# Definiciones
definitions = {
    "shield": "Protects you from damage in FortNITE.",
    "goalkeeper": "Protects the goal in football.",
    "storm": "Dangerous zone that reduces health.",
    "rival team": "Opponent team in a match.",
    "revive": "Bring a teammate back to life.",
    "substitute": "Player who replaces another.",
    "loot": "Items collected from the ground.",
    "ball possession": "Control of the ball during play.",
    "ramp": "Structure used to gain height.",
    "counterattack": "Quick offensive move after defending."
}

# Inicializar puntuación
if "score" not in st.session_state:
    st.session_state.score = 0

st.title("⚔️ Comparación de vocabulario: FortNITE vs Fútbol")

# Selección de palabra
word = st.selectbox("Selecciona una palabra de FortNITE", list(vocab_pairs.keys()))
st.write(f"**FortNITE:** {word} → {definitions[word]}")

# Pregunta de comparación
st.write("¿Cuál es su equivalente en fútbol?")
options = list(set(vocab_pairs.values()) | {"referee", "stadium", "coach"})
selected = st.radio("Elige la opción correcta:", options)

# Verificación
if st.button("Comprobar"):
    correct = vocab_pairs[word]
    if selected == correct:
        st.success("¡Correcto!")
        st.session_state.score += 1
    else:
        st.error(f"No exactamente... La respuesta era: **{correct}**")

# Mostrar progreso
st.markdown(f"**Puntuación actual:** {st.session_state.score} puntos")

# Reiniciar
if st.button("Reiniciar puntuación"):
    st.session_state.score = 0
