import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from Transect import Transect


def load_data():
    return pd.read_csv('./action_state.csv')


# Add a title
st.title('Explore GMT Action-States')
# Load Data
data_load_state = st.text('Loading Actions and States')
df = load_data()
data_load_state.text('Loading States...Done!')


## User Options
state_def = st.sidebar.selectbox('Select state components or definition:', df.columns[4:])
action_type = st.sidebar.selectbox('Select action type:', ['Any']+list(set(df.action.values)))
min_year=min(df.survey_year); max_year=max(df.survey_year)
start_year, end_year = st.sidebar.slider('Select year range', min_value=min_year, max_value=max_year,value=(min_year,max_year), step=1)

## Raw Data Display
#st.subheader('Raw data')
#st.write(df)

## Get years needed
df_in_range = df.loc[df['survey_year'].between(start_year,end_year)]

####
st.subheader("Relative counts of actions given state")
tab = pd.crosstab( df_in_range[state_def],df_in_range.action,margins=False, normalize='index')
tab_blue = tab.style.format("{:.2}").background_gradient(cmap='Blues')
st.write(tab_blue)


if action_type != 'Any':
    df_in_range = df_in_range.loc[df_in_range['action']==action_type]

counts = df_in_range[state_def].value_counts()

try:
    counts.index = counts.index.astype(int)
except TypeError:
    pass
counts.sort_index(inplace=True)

st.subheader('Counts for years {} to {} for {} action\n Includes {} surveys'.format(start_year,end_year,action_type,sum(counts)))
st.write(counts)
st.bar_chart(counts)
st.text('Counts of {}'.format(state_def.replace('_', ' ').title()))

