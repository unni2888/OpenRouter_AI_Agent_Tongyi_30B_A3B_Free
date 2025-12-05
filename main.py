from openai import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY")
)

st.title("Reasoning with Tongyi DeepResearch 30B A3B")





with st.form("search_form"):
    question = st.text_input("Enter your question:")
    submitted = st.form_submit_button("Search")

    if submitted and question:
        with st.spinner("Researching..."):
            response = client.chat.completions.create(
                                                      model="alibaba/tongyi-deepresearch-30b-a3b:free",
                                                      messages=[
                                                                  {
                                                                    "role": "user",
                                                                    "content": question
                                                                  }
                                                                ],
                                                      extra_body={"reasoning": {"enabled": True}}
                                                      )
            response = response.choices[0].message
            st.markdown(response.content)
            st.write("------------------------------------------------------------")
