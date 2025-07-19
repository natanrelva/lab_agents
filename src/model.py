import os
from langchain_google_genai import ChatGoogleGenerativeAI

from state import State

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)


def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}
