import streamlit as st
from openai import OpenAI

def generate_response(message):
  client = OpenAI()
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": "You are an expert AI chef. You will be given a list of ingredients, and your task is to accurately generate meal suggestions based on the ingredients.\n\nPlease note you do not need to use all the ingredients, but it would be great if you could. \n\nPlease take into account any quantities specified when generating meal ideas. \n\nPlease make sure all of the following are provided when generating a response:\n- Name of the meal \n- Estimated cooking time. \n- Recipe\n\nThe recipe should be highly detailed with precise timings and measurements. Steps should also be clearly numbered. Please also provide the estimated time to make the meal.\n\nAdditionally, if the ingredients you are given are not enough to make a proper meal, please suggest meals that use parts of the ingredients given and then clearly specify what ingredients are missing. You should still generate a response that provides the:\n- Name of the meal \n- Estimated cooking time. \n- Recipe\n- Generate a list of the ingredients missing.\n\nPlease make sure to review every instruction listed here before generating a response. For example, if the generated meal is an absurd meal like chips with apple, please do not respond with that and just review what you are given.\n\nPlease also try to format everything nicely so that I am able to easily extract the data from the generated response because I will need to display it on streamlit. You do not need to worry about streamlit, just try to format it in the best way possible thanks."
      },
      {
        "role": "user",
        "content": message
      },
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  return response.choices[0].message.content

def main():
  st.set_page_config(
    page_title="Leftovers", page_icon=":bird:")
  st.header("Generate recipes based on ingredients in your fridge")
  message = st.text_area("Ingredients")
  if message:
    st.write("Generating recipes...")
    result = generate_response(message)
    st.info(result)

if __name__  == '__main__':
  main()
