import streamlit
import pandas
from urllib.error import URLError

streamlit.title("My Parents New Healthy Dinner")
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('fruitvise fruit Advice')
try:
  fruit_input=streamlit.text_input('What is fruit you want')
  if not fruit_input:
    streamlit.error("please select a fruit to get information.")
  else:
    fruitvise_response =requests.get("https://fruityvice.com/api/fruit/"+fruit_input)
    fruitvise_normalize =pandas.json_normalize(fruitvise_response.json())
    streamlit.dataframe(fruitvise_normalize)
except URLError as e:
  streamlit.error()

import requests

#streamlit.text(fruitvise_response.json())

streamlit.stop()
import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list ")
my_data_row = my_cur.fetchall()
streamlit.header("Fruit Load list contains :")
streamlit.dataframe(my_data_row)

fruit_input=streamlit.text_input('What is fruit you like to add ','Kiwi')
streamlit.write(' Thanks for adding', fruit_input)
