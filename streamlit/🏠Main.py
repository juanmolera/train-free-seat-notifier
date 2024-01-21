# Streamlit
import streamlit as st

# Images
from PIL import Image

# Pandas
import pandas as pd

# My functions
from src import data_functions as dat
from src import validation_functions as val
from src import request_functions as req
from src import email_functions as ema

# Streamlit page configuration
st.set_page_config(layout='wide', initial_sidebar_state='collapsed', page_title='Main', page_icon='💺')

# CSS access
with open('css/style.css') as f:
    st.markdown(
        f'<style>{f.read()}</style>',
        unsafe_allow_html=True)
    
    
#st.markdown('# Train booking updates')
st.markdown("<h1 style='text-align: center; color: white;'>Train Free Seat Notifier</h1>", unsafe_allow_html=True)

col3, col4, col5 = st.columns(3)  

with col3:
    pass

with col4:
    image = Image.open('../images/logo.png')
    st.image(image, use_column_width=True)

with col5:
    pass

col1, col2 = st.columns(2)

with col1:

    st.markdown('### Please, enter the following info:')

    # Email input
    email = st.text_input('Email')

    if bool(email):

        val.check_email(email)

    date = st.date_input("Date")

    if date is not None:

        day_of_the_week = date.strftime('%A')

        timetable = dat.get_timetable(day_of_the_week)

        time = st.multiselect('Time', timetable)

with col2:

    if bool(email) and bool(date) and bool(time):

        st.markdown('### Summary:')

        st.write('Email:', email)
        st.write('Date:', date)
        st.write('Time:', time)

        if st.button('Confirm'):           

            st.write(f'Confirmation email sent to {email}')
            #ema.send_confirmation_email(email, date, time)

            req.save_customer_request(email, date, time)

        else:

            st.write('Please, confirm')
