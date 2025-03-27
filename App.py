import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv("Dataset_Unificado.csv")

st.title("Dashboard de Calidad del Aire en Bucaramanga")

# Mostrar dataframe
st.subheader("Datos del Aire")
st.dataframe(df.head())

# Histogramas
st.subheader("Distribución de Contaminantes")
fig, axs = plt.subplots(2, 3, figsize=(15, 8))
contaminantes = ['PM10', 'PM2.5', 'SO2', 'NO2', 'O3']
for i, var in enumerate(contaminantes):
    sns.histplot(df[var], bins=30, kde=True, ax=axs[i//3, i%3], color="orange")
    axs[i//3, i%3].set_title(f"Distribución de {var}")
st.pyplot(fig)

# Correlación
st.subheader("Matriz de Correlación")
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(df[contaminantes].corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Predicción simple (simbólica)
st.subheader("Simulador de Predicción de Calidad del Aire")
pm10 = st.slider("PM10", 0, 100, 20)
pm25 = st.slider("PM2.5", 0, 100, 20)
so2 = st.slider("SO2", 0, 10, 1)
no2 = st.slider("NO2", 0, 100, 20)
o3 = st.slider("O3", 0, 100, 20)

# Clasificación ficticia ajustada
ica = pm10 + pm25 + so2*10 + no2 + o3

if ica <= 150:
    categoria = "BUENA ✅"
    st.success(f"✅ Calidad del Aire: {categoria}")
elif ica <= 300:
    categoria = "MODERADA 🟡"
    st.warning(f"🟡 Calidad del Aire: {categoria}")
else:
    categoria = "MALA 🔴"
    st.error(f"🔴 Calidad del Aire: {categoria}")
