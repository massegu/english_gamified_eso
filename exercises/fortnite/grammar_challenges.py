import streamlit as st

def run():
    st.title("🔄 FortNITE Grammar Challenge")
    st.write("Frase incorrecta: *He builded a ramp*")
    slider = st.slider("Desliza para ver la corrección", 0, 100, 0)
    if slider > 50:
        st.write("✅ Frase correcta: *He built a ramp*")
        with st.expander("¿Por qué?"):
            st.markdown("El verbo 'build' es irregular. El pasado es 'built', no 'builded'.")
