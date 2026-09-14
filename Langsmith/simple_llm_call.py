from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(template='Answer the question. {question}', input_variables=['question'])

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,    
    api_key=os.getenv("GROQ_API_KEY"),
)

parser = StrOutputParser()

chain = prompt | llm | parser

question = "What is the capital of spain?"

result = chain.invoke({"question": question})

print(result)
