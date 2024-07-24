from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import openai
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()



st.title("Prompt Revamper ")
openai_api_key = os.getenv('OPENAI_API_KEY')

user_prompt = st.text_input("Enter your prompt :",placeholder="hello write something")

def get_prompt_revamp(user_prompt):
        system_prompt = f"""you are human based expert Prompt engineer.When user gives you any query as prompt you 
                should to analysis it check spelling mistakes and check is user prompt is according to prompt engineering techniques along with explain errors in user query prompt and give user to revamped prompt
                Remember you are here to guide user in the art of prompt engineering.
                Question :{user_prompt} : 
                Instructions :
                1.when you see user query prompt is good understandable then you will appreciate user and acknowledge it.
                3. your have to check explain any mistakes made in user original prompt .
                5. If user prompt is correct, I'll acknowledge it.
                6. Don't answer the user questions just stay with your role .
                """
        # temp_prompt = [{"role": "system", "content": system_prompt},{"role": "user", "content":Instructions}]
        # prompt_str = ' '.join([item["content"] for item in temp_prompt]) 

        model = OpenAI(openai_api_key= openai_api_key )
        prompt = ChatPromptTemplate.from_template(system_prompt)
        output_parser = StrOutputParser()
        chain = prompt | model | output_parser
        res = chain.invoke({"Question":user_prompt})
        return res
if st.button("submit"):
    result = get_prompt_revamp(user_prompt)
    st.write("Here is Revamped prompt : " , result)