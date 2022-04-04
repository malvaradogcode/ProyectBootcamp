from enum import unique
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='Reporte: Consumo Global de Energía y Generación Renovable', page_icon='📊', layout='wide')

st.title('📊 Reporte: Consumo Global de Energía y Generación Renovable')


@st.cache
def load_data(nrows):
    df_continent = pd.read_csv('./data/Continent_Consumption_TWH.csv', nrows=nrows)
    return df_continent

df_continent_load_state = st.text('Loading data...done!')
df_continent = load_data(10000)
df_continent_load_state.text("Done! (using st.cache)")

# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(df_Continent)

st.subheader('Consumo Energético (TWh) 1990 - 2020')
st.markdown('Esta tabla nos muestra el consumo energético desde el 1990 al 2020, agrupados por Continentes, Organizaciones y el consumo mundial.')
st.write(df_continent)

# ---- SIDEBAR-----
# st.sidebar.header('Filtre aquí:')
# continent = st.sidebar.multiselect(
#     'Selecciona el continente:',
#     options=df_continent['Year'].unique(),
#     default=df_continent['Year'].unique()
# )

# df_selection = df_continent_year.query(
#     'Year == @Year'
# )

# st.dataframe(df_selection)

# world_energy_consumption = df_continent['World'].values
# years = df_continent['Year'].values

# st.plt.figure(figsize=(12,9))
# st.plt.plot(years,world_energy_consumption)
# st.plt.xlabel('Years')
# st.plt.ylabel('TWh')
# st.plt.title('World energy consumption')
# st.plt.grid(True)
# st.plt.show()