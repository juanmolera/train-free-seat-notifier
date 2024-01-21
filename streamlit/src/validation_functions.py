import streamlit as st
import re

# Regex email pattern
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# Checks if email is valid
def check_email(email):

    if(re.fullmatch(pattern, email)):

        return st.markdown(':green[Valid email]')

    else:
        
        return st.markdown(':red[Invalid email]')