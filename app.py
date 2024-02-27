import streamlit as st
from langchain_community.llms import OpenAI

st.title('Find The Recipe You Desire || Recipe Recommendation System')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_recommendations(input_text):
    try:
        llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key, model="gpt-3.5-turbo-instruct")
        prompt = f"Given the ingredients: {input_text}, suggest an easy-to-cook step-by-step recipe."
        response = llm(prompt)
        return response
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

with st.form('my_form'):
    user_input = st.text_area('Enter your preferred ingredients (separated by commas):')
    submitted = st.form_submit_button('Get Recipe Recommendations')

if submitted and openai_api_key.startswith('sk-'):
    recommended_recipe = generate_recommendations(user_input)
    st.info(recommended_recipe)

