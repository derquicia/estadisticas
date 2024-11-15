import streamlit as st
import pandas as pd
import numpy as np
import json
from streamlit_echarts import st_echarts
from streamlit_echarts import JsCode
from streamlit_echarts import st_pyecharts
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.charts import Line


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


footer = """
  <style> your css code put here</style>
  <div class='footer'>
  <p>the word you want to tell<a style='display:block;text-align:center;' 
  href='https://www.streamlit.io' target='_blank'>your email address put here</a></p>
  </div>"""
st.markdown(footer, unsafe_allow_html=True)


conn = st.connection("postgresql", type="sql")
df = conn.query('select anio,litros,color from info_desp_anio;', ttl="0"),
df1 = conn.query('select anio,litros from info_desp_anio where color = 'Tinto' ;', ttl="0"),
df2 = conn.query('select anio,litros from info_desp_anio where color = 'Blanco' ;', ttl="0"),
df3 = conn.query('select anio,litros from info_desp_anio where color = 'Rosado' ;', ttl="0"),
#st.write(df)
 
st.subheader('Evolución de los despachos por año')

if st.checkbox('Ver datos en forma de tabla'):
    st.write(df)


df['anio'] = df['anio'].astype(str)

newdf=df.set_index('anio',inplace=False).rename_axis(None)

option = {
    "tooltip": {
        "trigger": 'axis',
        "axisPointer": { "type": 'cross' }
    },
    "legend": {},    
    "xAxis": {
        "type": "category",
        "data": df['anio'].to_list(),
    },
    "yAxis": {"type": "value"},
    "series": [{"data": df1['litros'].to_list(), "type": "line", "name": 'Tintos'},
               {"data": df2['litros'].to_list(), "type": "line", "name": 'Blancos'},
               {"data": df3['litros'].to_list(), "type": "line", "name": 'Rosados'},
               ]
}
st_echarts(
    options=option, height="400px" ,
)

