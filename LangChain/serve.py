from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langserve import add_routes
import uvicorn
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

## Step 1: Initiate model
model = ChatGroq(model="llama-3.1-8b-instant",groq_api_key=groq_api_key)

## Step 2: Create Prompt Template
prompt_template = ChatPromptTemplate([
    ("system","Translate the following into {language}"),
    ("user","{text}")
])

## Step 3: Creating output parser
parser = StrOutputParser()

## Step 4: Create Chain
chain = prompt_template|model|parser

## App definition
app = FastAPI(title ="Langchain Server",
              version="1.0",
              Description = "A simple API server using Lanchain runnable interfaces")

## Adding chain routes
add_routes(
    app,
    chain,
    path ="/chain"
)

if __name__ == "__main__":
    uvicorn.run(app,
                host="localhost",
                port =8000)

