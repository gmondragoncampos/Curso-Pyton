
import streamlit as st 
import pandas as pd 
import numpy as np

st.title('UPC Data Science 2024')
st.header('Simulador Ventas')
n = st.slider("cant. ventas", 5,100, step=1)
chart_data = pd.DataFrame(np.random.randn(n),columns=['ventas'])
st.line_chart(chart_data)
