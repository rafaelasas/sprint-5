import pandas as pd
import plotly.express as px
import streamlit as st

# ler o dataset
car_data = pd.read_csv('vehicles.csv')

# cabeçalho
st.header("Análise de Dados de Veículos")

# checkbox para histograma
build_histogram = st.checkbox("Criar histograma")

if build_histogram:
    st.write("Criando um histograma para a quilometragem (odômetro) dos veículos")
    fig = px.histogram(car_data, x="odometer", nbins=50,
                       title="Distribuição da Quilometragem dos Veículos")
    st.plotly_chart(fig, use_container_width=True)

# checkbox para scatterplot
build_scatter = st.checkbox("Criar gráfico de dispersão")

if build_scatter:
    st.write("Criando um gráfico de dispersão: Quilometragem vs Preço")
    fig = px.scatter(car_data, x="odometer", y="price",
                     title="Preço vs Quilometragem",
                     opacity=0.5)
    st.plotly_chart(fig, use_container_width=True)