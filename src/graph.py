from model import chatbot
from state import State
from langgraph.graph import StateGraph, START, END

graph_builder = StateGraph(State)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge("chatbot", END)

graphChatBot = graph_builder.compile()
