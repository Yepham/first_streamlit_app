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

streamlit.header('🥝🍇 I built my own menu')

# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)






