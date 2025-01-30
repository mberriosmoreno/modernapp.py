import streamlit as st
import streamlit_authenticator as stauth

st.set_page_config(page_title="Login", page_icon="🔒", layout="centered")

# Configurar credenciales
users = {"admin": "pbkdf2:sha256:260000$Wxyz..."}

authenticator = stauth.Authenticate(users, "mi_app.py", "auth_cookie", cookie_expiry_days=30)
name, authentication_status, username = authenticator.login("Iniciar Sesión", "main")

if authentication_status:
    st.success(f"Bienvenido {name} 🎉")
elif authentication_status == False:
    st.error("Usuario o contraseña incorrectos")
