import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re
import plotly.express as px
import numpy as np





st.set_page_config(page_title="Smartphones", page_icon=":phone:")
st.markdown("<h1 style='text-align: center; color: Orange;'>SMARTPHONES</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: Cyan;'>Bryan Valerio Reyes</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: LightGreen;'>zs20006768</h3>", unsafe_allow_html=True)

DATA_URL = 'https://raw.githubusercontent.com/BryanVRe/Smartphone-Processors-Ranking-Scores/master/Smartphone_Evolution.csv'

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, encoding_errors='ignore')
    return data

@st.cache
def load_data_name(name):
    datafiltered = load_data(5000)

    #filtrar_data_nombre = datafiltered[datafiltered['Brand'].str.contains(name, flags=re.IGNORECASE)]  
    filtrar_data_nombre = datafiltered[datafiltered['Brand']==name]  
    return filtrar_data_nombre

@st.cache
def load_data_model(Model):
    data = load_data(5000)
    filtrar_data_modelo = data[data['Model'].str.match( Model, case=False)]
    return filtrar_data_modelo


st.sidebar.image('https://raw.githubusercontent.com/BryanVRe/Smartphone-Processors-Ranking-Scores/master/android.png')

sidebar = st.sidebar
agree = sidebar.checkbox("Mostrar todos los smartphones")
titulo = sidebar.text_input('buscar por nombre de smartphone:')
btnFiltrarSmartphone = sidebar.button('Buscar')
data = load_data(5000)
selected = sidebar.selectbox("Seleccionar por compañia", data['Brand'].unique())
btnFiltrarCompañia = sidebar.button('Filtrar por compañia')


if agree:
    estado = st.text('Cargando...')
    data = load_data(5000)
    estado.text("¡Cargando datos espere un momento...! ")
    st.dataframe(data)

if btnFiltrarSmartphone:
    st.write ("Titulo buscado: "+ titulo)
    filtrar = load_data_model(titulo)
    filas = filtrar.shape[0]
    st.write(f'Total de Smarphone mostrados: {filas}')
    st.dataframe(filtrar)

if btnFiltrarCompañia: 
    st.write("smartphones creados por "+selected)
    filtrar = load_data_name(selected)
    filas = filtrar.shape[0]
    st.write(f'Total de smartphones: {filas}')
    st.dataframe(filtrar)

#histograma de videojuegos
st.sidebar.title("Graficas:")
agree = st.sidebar.checkbox("Histograma")
if agree:
  fig_genre=px.bar(data,
                    x=data['Brand'],
                    y=data['Model'],
                    orientation="v",
                    title="Smartphones by company",
                    labels=dict(y="Model", x="Company"),
                    color_discrete_sequence=["cyan"],
                    template="plotly_white")
  st.plotly_chart(fig_genre)

#diagrama de barras
if st.sidebar.checkbox('Grafica de barras'):
    st.subheader('grafica de barras ')

    fig, ax = plt.subplots()

    y_pos = data['Battery']
    x_pos = data['Primary_Storage']

    ax.barh(x_pos, y_pos,color = "Cyan")
    ax.set_ylabel("Battery")
    ax.set_xlabel("Storage")
    ax.set_title('grafica de barras')
    st.header('grafica de barras battery and storage')
    st.pyplot(fig)

    st.markdown("___")

#diagrama de scatter
if st.sidebar.checkbox('scatter smartphone'):
    st.subheader('scatter de paints')
    imprint=data['Battery']
    years=data['Primary_Storage']
    rating=data['Display_Size']
    fig_age=px.scatter(data,
                   x=imprint,
                   y=rating,
                   color=years, 
                   title="comparacion de bateria, alamacenamiento y tamaño de display",
                   labels=dict(Imprenta="imprint", years="years", print="Print"),
                   template="plotly_white")
    st.plotly_chart(fig_age)




