# Charity funding agent

## :construction: Under construction :construction:

## Overview
Charity funding agent is a Python-based application designed to assist users in finding charities and funders based on natural language queries. It leverages the LangChain framework to integrate tools for charity searches and web searches, enabling users to interact with an AI agent for information retrieval.

The project includes:
* A tool for searching charities using the CharityBase API.
* A web search tool powered by DuckDuckGo.
* An AI agent initialized with these tools to handle user queries.

### Features
* Charity Search Tool: Find charities or funders based on causes or locations using natural language descriptions.
* Web Search Tool: Retrieve information about current events, news, or public figures using plain English queries.
* Interactive Agent: Engage with the AI agent in real-time via a command-line interface.

### Technologies Used
* Programming Language: Python
* APIs: CharityBase API, OpenAI API
* Frameworks: LangChain
* Environment Management: dotenv for loading API keys securely

### How to run

* Install dependencies:

  ```pip copy
  pip install -r requirements.txt
  ```
* Add your API keys to the `.env` file.
* Run the `agent.py` script:

  ```pip copy
  python agent.py
  ```
