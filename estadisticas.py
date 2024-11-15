import streamlit as st
import pandas as pd
import numpy as np
import json
from streamlit_echarts import st_echarts
from streamlit_echarts import JsCode
from streamlit_echarts import st_pyecharts
from pyecharts.charts import Bar
from pyecharts import options as opts

hide_streamlit_style = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)




hide_streamlit_style = """
            <style>
                
                header {visibility: hidden;}
                footer {visibility: hidden;} 
                .streamlit-footer {display: none;}
                
                .st-emotion-cache-uf99v8 {display: none;}
            </style>
            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown(""" <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """, unsafe_allow_html=True)

conn = st.connection("postgresql", type="sql")
df = conn.query('SELECT periodo,"CERVEZAS","VINOS_COMUNES","VINOS_FINOS","APERITIVOS_ALC","APERITIVOS_RTD","ESPUMANTES","FRIZANTES","SIDRAS_Y_SABORES","VINOS_FORTIFICADOS" FROM scentia_res;', ttl="0")
#st.write(df)

col = st.columns((1.5, 4.5, 2), gap='medium')

with col[0]:
    st.markdown('Exportaciones')
    st.metric(label='HL', value= 814101 , delta=-0.97)
