import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("vehicles_clean.csv")
st.title("Análisis de anuncios de venta de vehículos")
st.header("Conjunto de datos")

mostrar_tabla = st.checkbox("Mostrar tabla de datos")

if mostrar_tabla:
    st.dataframe(car_data.head(10))


hist_button = st.button('Construir histograma')  # crear un botón
# Botón para gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

box_button = st.button("Construir diagrama de caja")

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

if box_button:
    st.write(
        "Creación de un diagrama de caja del conjunto de datos de anuncios de venta de coches")
    fig = px.box(
        car_data,
        x='decade',
        y='price',
        title="Precio de los automóviles por década de lanzamiento"
    )
    st.plotly_chart(fig, use_container_width=True)
