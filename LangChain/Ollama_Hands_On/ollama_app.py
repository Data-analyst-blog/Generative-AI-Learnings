# Databricks notebook source
#### Simple Gen AI APP Using Langchain
import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama                  # importing ollama essentials
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers  import StrOutputParser

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

## Step1: Designing Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant. please respond to question asked"),
        ("user","Question:{question}")
    ]
)

## Streamlit framework
st.title("Langchain Demo with Gemma 2B")
input_text = st.text_input("What question you have in mind?")


## Calling OLLAMA model
llm = Ollama(model="gemma:2b")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))