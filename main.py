from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

prumpt = ChatPromptTemplate.from_template (
    "ansower the following question in one short paragraoph: \n\n Question {question}")

model = ChatOpenAI(model="gpt-4.1-mini")

chain = prumpt | model

response = chain.invoke({"question": "What is langchain?"})

print(response.content)

