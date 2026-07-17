from search import web_search 
from rag import search
def router(tool_name, query):
    tools = {
        "web_search": web_search,
        "private_search": search
    }

    return tools[tool_name](query)