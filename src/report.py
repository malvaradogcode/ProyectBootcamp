from pathlib import Path
import streamlit as st
import pandas as pd
import numpy as np
from tangled_up_in_unicode import lowercase

st.title('📊 Reporte: Consumo Global de Energía y Generación Renovable')

DATE_COLUMN = 'World'
DATA_URL = ('https://drive.google.com/file/d/1HFyzc4sfV93tA0CAMYSdFiYF1-v6q2n8/view?usp=sharing')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# st.subheader('Number of pickups by hour')
#hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)

# Some number in the range 0-23
#hour_to_filter = st.slider('hour', 0, 23, 17)
#filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

#st.subheader('Map of all pickups at %s:00' % hour_to_filter)
#st.map(filtered_data)