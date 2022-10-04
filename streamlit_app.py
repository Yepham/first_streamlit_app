# Create the main python file
import streamlit
import pandas


streamlit.title('Hello, Streamlit 🥑 🐔')
streamlit.header('🥣 Starter')
streamlit.text('Warm milk')
streamlit.text('🍞 Warm coffe')
streamlit.text('Warm waffel')
streamlit.text('Warm drinks')
streamlit.text('🥗 Warm vegetable')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)



streamlit.header('🥝🍇 I built my own menu')


