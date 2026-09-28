from typing import TypedDict

from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
    message: str
    response: str

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
)

def agent_node(state: AgentState):
    response = llm.invoke(state["message"])

    return {
        "response": response.content
    }

builder = StateGraph(AgentState)

builder.add_node("agent", agent_node)

builder.add_edge(START, "agent")
builder.add_edge("agent", END)

graph = builder.compile()

if __name__ == "__main__":
    result = graph.invoke(
        {
            "message": "Saya ingin mengetahui status pesanan saya.",
            "response": "",
        }
    )

print(result["response"])