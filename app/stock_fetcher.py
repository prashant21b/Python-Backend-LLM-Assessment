from duckduckgo_search import DDGS
import re

def fetch_stock_price(stock):
    query = f"{stock} stock price"
    print(f"Searching: {query}")
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=5)
        for result in results:
            print(f" Result: {result}")
            body = result.get("body", "")
            match = re.search(r'\$?([0-9]+(?:\.[0-9]+)?)', body)
            if match:
                print(f" Price found: {match.group(1)}")
                return float(match.group(1))
    print(" No match found")
    return None
