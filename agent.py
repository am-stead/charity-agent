import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType, Tool
from charitybase_tool import search_charities
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()

# Create the OpenAI model
llm = ChatOpenAI(model="gpt-4", temperature=0)

web_search = DuckDuckGoSearchRun()

# Register your tool with LangChain
tools = [
    Tool(
        name="Charity Search Tool",
        func=search_charities,
        description="Useful for finding charities or funders based on a natural language description. Input should describe what kind of cause or location you're looking for."
    ),
    Tool(
        name="Web Search",
        func=web_search.run,
        description="Useful for answering questions about current events, recent news, or public figures. Input should be a plain English search query."
    )
]

# Initialize the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run a test interaction
while True:
    user_input = input("\nAsk about a charity (or type 'exit'): ")
    if user_input.lower() == 'exit':
        break
    response = agent.run(user_input)
    print("\n🤖 Agent response:\n")
    print(response)
