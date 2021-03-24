import streamlit as st
import pandas as pd
import numpy as np
from Transect import Transect


def load_data():
    return pd.read_csv('./states.csv')


# Add a title
st.title('Explore GMT States')
# Load Data
data_load_state = st.text('Loading States')
df = load_data()
data_load_state.text('Loading States...Done!')


## User Options
state_def = st.sidebar.selectbox('Select state components or definition:', df.columns[3:])
system_type = st.sidebar.selectbox('Select prairie type:', ['All'] + list(set(df.system_type.values)))
min_year=min(df.survey_year); max_year=max(df.survey_year)
start_year, end_year = st.sidebar.slider('Select year range', min_value=min_year, max_value=max_year,value=(min_year,max_year), step=1)

## Raw Data Display
st.subheader('Raw data')
st.write(df)


df_in_range = df.loc[df['survey_year'].between(start_year,end_year)]
if system_type != 'All':
    df_in_range = df_in_range.loc[df_in_range['system_type']==system_type]

counts = df_in_range[state_def].value_counts()

try:
    counts.index = counts.index.astype(int)
except TypeError:
    pass
counts.sort_index(inplace=True)

st.subheader('Counts for years {} to {} for {} system types\n Includes {} surveys'.format(start_year,end_year,system_type,sum(counts)))
st.write(counts)
st.bar_chart(counts)
st.text('Counts of {}'.format(state_def.replace('_', ' ').title()))

#st.write(df[['state']].values_counts())
#st.bar_chart(hist_values)