# charitybase_tool.py

import os
import requests
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()

CHARITYBASE_API_KEY = os.getenv("CHARITYBASE_API_KEY")

@tool
def search_charities(query: str) -> str:
    """
    Use this to search for trusts/foundations or charities that match the query.
    The query should mention what you're looking for (e.g., 'foundations funding education in Sierra Leone').
    """
    url = "https://charitybase.uk/api/v0.4/charities"
    params = {
        "apiKey": CHARITYBASE_API_KEY,
        "search": query,
        "incomeRange": "10k-100M",  # Optional: filter large orgs
        "limit": 5
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        results = []
        for c in data.get("charities", []):
            name = c.get("name")
            cause = c.get("causes", [])
            url = c.get("website", "No website")
            results.append(f"{name}\n  Causes: {cause}\n  Website: {url}")
        return "\n\n".join(results) or "No matching charities found."
    else:
        return f"Error: {response.status_code} - {response.text}"
