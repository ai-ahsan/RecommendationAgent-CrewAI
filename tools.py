from crewai_tools import JSONSearchTool
from crewai.tools import tool
from tavily import TavilyClient
import os


json_tool_faq = JSONSearchTool(json_path='JSONS/FAQ.json')
json_tool_inventory = JSONSearchTool(json_path='JSONS/Inventory.json')



@tool("Tavily Search")
def tavily_search(query: str) -> str:
    """Perform a search using Tavily API."""
    tavily_client = TavilyClient(api_key=os.environ.get('TAVILY_API_KEY'))
    context = tavily_client.get_search_context(query)
    return context