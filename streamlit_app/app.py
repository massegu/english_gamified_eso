import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 📦 Importa el menú desde la carpeta components
from components import menu

# ⚙️ Configuración general de la app
st.set_page_config(
    page_title="English Gamified ESO",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🚀 Lanza el menú principal
menu.show()
