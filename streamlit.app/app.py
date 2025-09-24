import streamlit as st

st.set_page_config(page_title="English Gamified ESO", layout="wide")

st.sidebar.title("🎮 Menú de ejercicios")
option = st.sidebar.radio("Selecciona una temática", [
    "Vocabulario FortNITE",
    "Crónica Real Madrid",
    "Corrección gramatical FortNITE",
    "Escucha y responde",
    "Traducción de cánticos"
])

# Ejercicio 1: Vocabulario FortNITE
if option == "Vocabulario FortNITE":
    st.title("🛡️ Vocabulario básico FortNITE")
    st.image("assets/fortnite/shield.png", width=200)
    st.write("**Palabra:** Shield")
    if st.button("¿Qué significa?"):
        st.info("Shield: A protective item that increases your defense in the game.")
    st.audio("assets/fortnite/shield.mp3")

# Ejercicio 2: Crónica Real Madrid
elif option == "Crónica Real Madrid":
    st.title("⚽ Crónica de partido")
    st.image("assets/madrid/bernabeu.jpg", width=300)
    st.markdown("Yesterday, Real Madrid ___ the match against Barcelona.")
    verb = st.selectbox("Selecciona el verbo correcto", ["wins", "won", "winned"])
    if st.button("Comprobar"):
        if verb == "won":
            st.success("¡Correcto!")
        else:
            st.error("Intenta de nuevo.")

# Ejercicio 3: Corrección gramatical FortNITE
elif option == "Corrección gramatical FortNITE":
    st.title("🔄 Corrige la frase")
    st.write("Frase incorrecta: *He builded a ramp*")
    slider = st.slider("Desliza para ver la corrección", 0, 100, 0)
    if slider > 50:
        st.write("✅ Frase correcta: *He built a ramp*")
        with st.expander("¿Por qué?"):
            st.markdown("El verbo 'build' es irregular. El pasado es 'built', no 'builded'.")

# Ejercicio 4: Escucha y responde
elif option == "Escucha y responde":
    st.title("🎧 Escucha y responde")
    st.audio("assets/fortnite/dialogue.mp3")
    answer = st.radio("¿Qué dijo el personaje?", [
        "I need a medkit!",
        "Watch out for the storm!",
        "Let's build a ramp!"
    ])
    if st.button("Verificar respuesta"):
        if answer == "Watch out for the storm!":
            st.success("¡Correcto!")
        else:
            st.error("No es lo que dijo.")

# Ejercicio 5: Traducción de cánticos
elif option == "Traducción de cánticos":
    st.title("🧠 Traducción de cánticos")
    st.markdown("Cántico: *¡Hala Madrid y nada más!*")
    translation = st.text_area("Escribe tu traducción en inglés")
    if st.button("Analizar"):
        st.write("Traducción sugerida: *Go Madrid and nothing else!*")
        with st.expander("Análisis lingüístico"):
            st.markdown("""
            - *Hala* es una expresión de ánimo, similar a *Go* o *Come on*.
            - *Nada más* enfatiza exclusividad o pasión total.
            """)

