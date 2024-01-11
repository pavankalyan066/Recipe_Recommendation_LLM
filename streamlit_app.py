import streamlit as st
from usellm import Message, Options, UseLLM
st.set_page_config(page_title="🦜🔗 Quickstart App")
st.title('🦜🔗 Quickstart App')

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

  return reponse.content 
  

with st.form('my_form'):
  cuisine = st.selectbox("Select Cuisine:", ["Italian", "Mexican", "Asian", "Mediterranean"])
  meat = st.selectbox("Select Meat Type:", ["Chicken", "Beef", "Pork", "Vegetarian"])
  # text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  # if not openai_api_key.startswith('sk-'):
  #   st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted:
    generate_response(cuisine, meat)
