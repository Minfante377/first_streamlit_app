import streamlit
import pandas as pd

FRUIT_LIST_PATH = "https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/"\
                  "fruit_macros.txt"

streamlit.title("My Parents New Healthy Dinner")

streamlit.header("Breakfast Menu")
streamlit.text("Omega 3 and Blueberry Oatmeal")
streamlit.text("Kale, Spinach and Rocket Smoothie")
streamlit.text("Hard-Boiled Free-Range Egg")

streamlit.header("Build your own Fruit Smoothie")
my_fruit_df = pd.reac_csv(FRUIT_LIST_PATH)
streamlit.dataframe(my_fruit_df)
