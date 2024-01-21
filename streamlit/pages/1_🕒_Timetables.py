import streamlit as st

# My functions
from src import data_functions as data

st.markdown('### Train timetables')

col1, col2 = st.columns(2)

with col1:

    st.markdown('#### Monday to friday:')
    timetable1 = data.get_timetable('monday')
    st.dataframe(timetable1)

with col2:

    st.markdown('#### Saturday and sunday:')
    timetable2 = data.get_timetable('saturday')
    st.dataframe(timetable2)