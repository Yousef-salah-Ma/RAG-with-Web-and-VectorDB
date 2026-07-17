# To install: pip install tavily-python
from tavily import TavilyClient
import os

client = TavilyClient(os.getenv("TAVILY_API_KEY"))
def web_search(query):
    response =  client.search(query=query ,  search_depth="advanced")
    return response["results"]




