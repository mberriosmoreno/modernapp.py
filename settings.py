import streamlit as st

st.set_page_config(page_title="Configuración", page_icon="⚙️", layout="wide")

st.title("⚙️ Configuración del Usuario")

with st.form("config_form"):
    nombre = st.text_input("Nombre", "Usuario")
    email = st.text_input("Correo Electrónico", "usuario@email.com")
    password = st.text_input("Nueva Contraseña", type="password")
    
    submit = st.form_submit_button("Guardar Cambios")
    
    if submit:
        st.success("Información actualizada con éxito.")
