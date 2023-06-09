# https://python.langchain.com/en/latest/modules/agents/agents/examples/chat_conversation_agent.html

import os
os.environ["LANGCHAIN_HANDLER"] = "langchain"
from langchain.agents import Tool
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent
from langchain.agents import AgentType



"""
search = SerpAPIWrapper()
tools = [
    Tool(
        name = "Current Search",
        func=search.run,
        description="useful for when you need to answer questions about current events or the current state of the world. the input to this should be a single search term."
    ),
]
"""

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
llm=ChatOpenAI(temperature=0)
agent_chain = initialize_agent( [], llm, agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory)
agent_chain.run(input="hi, i am bob")

agent_chain.run(input="what's my name?")

