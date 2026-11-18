import pandas as pd
import numpy as np
import streamlit as st
import plotly as pl

df = pd.read_excel("saeb_aprendizado_territorios-7-2023-EM.xlsx",
sheet_name="estados", engine="openpyxl")

#2. Filtre apenas as UFs MG, BA, CE e PR (coluna uf)

df_filtrado = pd.DataFrame({
    'UF': ['MG', 'BA', 'CE', 'PR'],
})


st.set_page_config(
    page_title="Insuficiencia por estado",
    page_icon="😥",
    layout="wide",
)

st.title("Insuficiencia por estado")