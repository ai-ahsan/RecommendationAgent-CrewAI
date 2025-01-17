from crewai import Task
from tools import tavily_search,json_tool_faq, json_tool_inventory
from agents import query_responder, blog_writer

## Research Task
search_json_faq = Task(
  description=(
    "Identify and extract relevant JSON fields related to {topic}."
    "Provide detailed and accurate information about {topic}."
  ),
  expected_output='A comprehensive and detailed context for {topic} based on the user query.',
  tools=[json_tool_faq],
  agent=query_responder,
)

search_json_inventory = Task(
  description=(
    "Identify and extract relevant JSON fields related to {topic}."
    "Provide detailed and accurate information about {topic}."
  ),
  expected_output='A comprehensive and detailed context for {topic} based on the user query.',
  tools=[json_tool_inventory],
  agent=query_responder,
)
search_tavily = Task(
  description=(
    "Perform a search using Tavily API."
  ),
  expected_output='A detailed context based on the user query.',
  tools=[tavily_search],
  agent=query_responder,
)

# Writing task with strict language model configuration
write_task = Task(
  description=(
    "Analyze the provided JSON data on the topic {topic}."
    "Summarize the information and create a detailed blog post."
  ),
  expected_output='A well-structured and informative blog post on the topic {topic}.',
  tools=[json_tool_faq, json_tool_inventory],
  agent=blog_writer,
  async_execution=False,
  output_file='Blog report on {topic}.md'  # Example of output customization
)