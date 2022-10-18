import requests

import streamlit
import pandas as pd

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

fruitvyce_response = requests.get("{}/watermelon".format(FRUITYVICE_ENDPOINT))
fruitvyce_normalized_df = pd.json_normalize(fruitvyce_response.json())
streamlit.dataframe(fruitvyce_normalized_df)
