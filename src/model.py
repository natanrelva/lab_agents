import os
from langchain_google_genai import ChatGoogleGenerativeAI

from state import State
from tool.searchWebTool import searchWeb

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)


def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}


def chatbotWithSearchWeb(state: State):
    llm_with_tools = llm.bind_tools(searchWeb)
    return {"messages": [llm_with_tools.invoke(state["messages"])]}
