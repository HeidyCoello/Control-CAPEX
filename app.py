import streamlit as st
import pandas as pd
st.title("Bolsa de Valores Quito BI")
st.sidebar.title("Parametros")
st.write("Elaborado por: Heidy Coello")


archivo = st.file_uploader("Cargue su archivo")

if archivo is not None:
tabla = pd.read_csv(archivo)
st.write(tabla)

