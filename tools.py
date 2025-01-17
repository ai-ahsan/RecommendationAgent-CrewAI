from crewai_tools import JSONSearchTool
from crewai.tools import tool
from tavily import TavilyClient

json_tool_faq = JSONSearchTool(json_path='JSONS/FAQ.json')
json_tool_inventory = JSONSearchTool(json_path='JSONS/Inventory.json')



@tool("Tavily Search")
def tavily_search(query: str) -> str:
    """Perform a search using Tavily API."""
    tavily_client = TavilyClient(api_key="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")
    context = tavily_client.get_search_context(query="What happened during the Burning Man floods?")
    return context