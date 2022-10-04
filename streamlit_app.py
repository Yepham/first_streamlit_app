# Create the main python file
import streamlit as st


#streamlit.title('Hello, Streamlit!!')

#import streamlit as st

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
