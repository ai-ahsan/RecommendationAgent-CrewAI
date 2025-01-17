from crewai import Crew, Process
from agents import query_responder, blog_writer
from tasks import search_json_faq, search_json_inventory, search_tavily, write_task
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

crew = Crew(
  agents=[query_responder, blog_writer],
  tasks=[search_json_inventory, search_json_faq, search_tavily, write_task],
  process=Process.sequential,  
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

user_input = input("Enter the topic you want to search: ")

# Start the task execution process with enhanced feedback
result = crew.kickoff(inputs={'topic': user_input})

# Extract token usage information
if hasattr(result, 'token_usage'):
    token_usage = result.token_usage
    prompt_tokens = token_usage.prompt_tokens
    completion_tokens = token_usage.completion_tokens
    total_tokens = token_usage.total_tokens
else:
    prompt_tokens = 0
    completion_tokens = 0
    total_tokens = 0

# Print the result and token usage information
print(f"Result: {result}\n\nToken Usage:\nPrompt Tokens: {prompt_tokens}\nCompletion Tokens: {completion_tokens}\nTotal Tokens: {total_tokens}")

