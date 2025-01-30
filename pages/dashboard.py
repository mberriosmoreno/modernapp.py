import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

st.title("📊 Panel de Control")

# Cargar datos de ejemplo
data = pd.DataFrame({
    "Categoría": ["Ventas", "Usuarios", "Suscripciones"],
    "Cantidad": [500, 1200, 300]
})

st.subheader("Resumen General")
st.dataframe(data)

# Gráfico de barras
fig = px.bar(data, x="Categoría", y="Cantidad", color="Categoría", title="Resumen de Datos")
st.plotly_chart(fig)
