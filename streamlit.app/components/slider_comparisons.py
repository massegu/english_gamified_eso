import streamlit as st

def show_comparison(title, incorrect_text, correct_text, explanation=None):
    st.subheader(title)
    slider = st.slider("Desliza para comparar", 0, 100, 0)
    
    if slider < 50:
        st.markdown(f"❌ **Incorrecto:** {incorrect_text}")
    else:
        st.markdown(f"✅ **Correcto:** {correct_text}")
        if explanation:
            with st.expander("¿Por qué?"):
                st.markdown(explanation)
