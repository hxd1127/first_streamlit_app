import streamlit
import pandas
import requests
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
def get_fruityvise_data(this_first_choice):
  fruitvise_response =requests.get("https://fruityvice.com/api/fruit/"+this_first_choice)
  fruitvise_normalize =pandas.json_normalize(fruitvise_response.json())
  return fruitvise_normalize
streamlit.header('fruitvise fruit Advice')
try:
  fruit_input=streamlit.text_input('What is fruit you want')
  if not fruit_input:
    streamlit.error("please select a fruit to get information.")
  else:
    back_from_function = get_fruityvise_data(fruit_input)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()

import snowflake.connector

streamlit.header("Fruit Load list contains :")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list ")
    return my_cur.fetchall()
  
if streamlit.button('get Fruit Load List')
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows=get_fruit_load_list()
  streamlit.dataframe(my_data_row)


def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('from strealit')")
    return "Thanks for adding "+ new_fruit
  
add_my_fruit=streamlit.text_input('What is fruit you like to add ')

if streamlit.button('Add a Fruit to Load List'):   
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function =insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)
