from model import chatbot, chatbotWithSearchWeb
from state import State
from langgraph.graph import StateGraph, START, END

graph_builder = StateGraph(State)

graph_builder.add_node("chatbotWithSearchWeb", chatbotWithSearchWeb)
graph_builder.add_edge(START, "chatbotWithSearchWeb")

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge("chatbotWithSearchWeb", "chatbot")

graph_builder.add_edge("chatbot", END)

graphChatBot = graph_builder.compile()
