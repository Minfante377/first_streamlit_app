import requests

import streamlit
import pandas as pd
from snowflake import connector

FRUIT_LIST_PATH = "https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/"\
                  "fruit_macros.txt"
FRUITYVICE_ENDPOINT = "https://fruityvice.com/api/fruit"

streamlit.title("My Parents New Healthy Dinner")

streamlit.header("Breakfast Menu")
streamlit.text("Omega 3 and Blueberry Oatmeal")
streamlit.text("Kale, Spinach and Rocket Smoothie")
streamlit.text("Hard-Boiled Free-Range Egg")

streamlit.header("Build your own Fruit Smoothie")

my_fruit_df = pd.read_csv(FRUIT_LIST_PATH)
my_fruit_df = my_fruit_df.set_index("Fruit")

fruits_selected = streamlit.multiselect(
    "Pick some fruits:",
    list(my_fruit_df.index)
)
fruits_to_show_df = my_fruit_df.loc[fruits_selected]
streamlit.dataframe(fruits_to_show_df)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input(
    "What fruit would you like information about",
    "Kiwi"
)
fruitvyce_response = requests.get("{}/{}".format(
    FRUITYVICE_ENDPOINT,
    fruit_choice)
)
fruitvyce_normalized_df = pd.json_normalize(fruitvyce_response.json())
streamlit.dataframe(fruitvyce_normalized_df)

my_cnx = connector.connect(**streamlit.secrets["snowflake"])
cursor = my_cnx.cursor()
cursor.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = cursor.fetchone()
streamlit.text("Hello from snowflake: {}".format(my_data_row))

cursor.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_row = cursor.fetchall()
streamlit.header("Fruit list: ")
streamlit.dataframe(my_data_row)
