import streamlit as st
from langchain_community.llms import OpenAI

st.set_page_config(
    page_title="Recipe Craft || Recipe Recommendation System",
    page_icon="🍳"
)

background_image_style = """
    <style>
        body {
            background-image: url('D:/Project/Images/foodbg.jpg');
            background-size: cover;
            background-repeat: no-repeat;
        }
    </style>
"""

st.title('🍳Recipe Craft || Recipe Recommendation System')
openai_api_key = "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"


def generate_recommendations(input_text):
    try:
        if not input_text:
            st.warning("Please provide some ingredients.")
            return ""

        llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key, model="gpt-3.5-turbo-instruct")
        prompt = f"Given the ingredients: {input_text}, suggest an easy-to-cook step-by-step recipe of a food not beverage. Give nutritional information of the recipe created as a table after displaying the recipe. Give additional ingredient suggestions to the current recipe to make the present recipe better.Display that below the recipie."
        response = llm(prompt)
        return response
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

with st.form('my_form'):
    user_input = st.text_area('Enter your preferred ingredients (separated by commas):')
    submitted = st.form_submit_button('Get Crafting')

if submitted:
    recommended_recipe = generate_recommendations(user_input)

    if recommended_recipe:
        st.info(recommended_recipe)
