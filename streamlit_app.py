import streamlit as st
from usellm import Message, Options, UseLLM
st.set_page_config(page_title="🦜🔗 Quickstart App")
st.title('🦜🔗 Recipe Recommendation using UseLLM')

# Sidebar with app description
st.sidebar.header("App Description")
st.sidebar.write("This app recommends recipes based on your chosen cuisine and meat type.")

# openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(cuisine, meat):
  service = UseLLM(service_url="https://usellm.org/api/llm")
  # Prepare the conversation
  prompt = f"generate one healthy recipe in {cuisine} cuisine using {meat}"
  messages = [
    Message(role="system", content="You are a master chef."),
    Message(role="user", content=prompt),
  ]
  options = Options(messages=messages)
  # Interact with the service
  response = service.chat(options)
  
  st.info(response.content ) 
  

with st.form('my_form'):
  cuisine = st.selectbox("Select Cuisine:", ["Italian", "Mexican", "Asian", "Mediterranean"])
  meat = st.selectbox("Select Meat Type:", ["Chicken", "Beef", "Pork", "Vegetarian"])
  submitted = st.form_submit_button('Submit')
  if submitted:
    generate_response(cuisine, meat)
