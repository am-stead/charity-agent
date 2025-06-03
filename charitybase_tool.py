import os
import requests
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()
CHARITYBASE_API_KEY = os.getenv("CHARITYBASE_API_KEY")

@tool
def search_charities(query: str) -> str:
    """
    Search for charities or funders using a natural language query.
    """

    url = "https://charitybase.uk/api/graphql"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Apikey {CHARITYBASE_API_KEY}"
    }

    payload = {
        "query": """
        {
          CHC {
            getCharities(filters: {search: "%s"}) {
              list {
                name
                activities
                website
              }
            }
          }
        }
        """ % query
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        charities = data.get("data", {}).get("CHC", {}).get("getCharities", {}).get("list", [])
        if not charities:
            return "No matching charities found."

        results = []
        for c in charities:
            results.append(f"{c.get('name')}\n  Activities: {c.get('activities')}\n  Website: {c.get('website', 'N/A')}")
        return "\n\n".join(results)
    else:
        return f"Error: {response.status_code} - {response.text}"
