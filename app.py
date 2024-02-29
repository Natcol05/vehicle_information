import pandas as pd 
import plotly.express as px
import streamlit as st


st.markdown("<h1 style='text-align: center; font-family: calibri, sans-serif; '>Información de carros vendidos</h1>", unsafe_allow_html=True)
car_data = pd.read_csv('vehicles_us.csv')
car_data


col1, col2 = st.columns(2)

# Botón de histograma en la primera columna
hist_button = col1.button('Construir histograma')

# Botón de gráfico de dispersión en la segunda columna
fig_button = col2.button('Construir grafico de dispersión')

# Manejar la visibilidad y ejecutar la acción correspondiente
if hist_button:
    fig = px.histogram(car_data, x="odometer")
    st.markdown("<h3 style='text-align: center;'>Histograma para el conjunto de carros vendidos</h3>", unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)

if fig_button:
    fig = px.scatter(car_data, x="odometer", y="price")
    st.markdown("<h3 style='text-align: center;'>Gráfico de dispersión para el conjunto de carros vendidos</h3>", unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)
    
