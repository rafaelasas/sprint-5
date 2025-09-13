import streamlit as st
import pandas as pd
import plotly.express as px

# título da aplicação
st.title("Análise Exploratória de Veículos")

# lendo o dataset
car_data = pd.read_csv("vehicles.csv")

st.write("### Primeiras linhas do conjunto de dados")
st.write(car_data.head())