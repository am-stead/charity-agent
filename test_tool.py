# test_tool.py

from charitybase_tool import search_charities

if __name__ == "__main__":
    query = "foundations funding education in Sierra Leone"
    result = search_charities(query)
    print("\n🔍 CharityBase Results:\n")
    print(result)
