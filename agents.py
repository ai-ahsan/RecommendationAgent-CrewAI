from crewai import Agent
from tools import json_tool_inventory, json_tool_faq, tavily_search
from dotenv import load_dotenv

load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"

class CustomAgent(Agent):
    def get_token_usage(self, result):
        token_usage = result.usage if hasattr(result, 'usage') else None
        if token_usage:
            prompt_tokens = token_usage.prompt_tokens
            completion_tokens = token_usage.completion_tokens
            total_tokens = token_usage.total_tokens
            return prompt_tokens, completion_tokens, total_tokens
        return 0, 0, 0

    def execute(self, inputs):
        result = super().execute(inputs)
        prompt_tokens, completion_tokens, total_tokens = self.get_token_usage(result)
        print(f"Token Usage:\nPrompt Tokens: {prompt_tokens}\nCompletion Tokens: {completion_tokens}\nTotal Tokens: {total_tokens}")
        result.token_usage = {
            'prompt_tokens': prompt_tokens,
            'completion_tokens': completion_tokens,
            'total_tokens': total_tokens
        }
        return result

## Create a senior blog content researcher
query_responder = CustomAgent(
    role='You are a comprehensive query responder',
    goal='Retrieve and provide detailed and accurate information from various sources based on the user query.',
    verbose=True,
    memory=True,
    backstory=(
       "You are a comprehensive query responder with the ability to retrieve and provide detailed and accurate information from various sources, including JSON data and Tavily search, based on the user query. Your goal is to bring as relevant context in the output as possible."
    ),
    tools=[json_tool_faq, json_tool_inventory, tavily_search],
    allow_delegation=True
)

## Creating a senior blog writer agent
blog_writer = CustomAgent(
    role='Recommendation Writer',
    goal='Analyze the JSON data and create a compelling blog post with recommendations based on the context of {topic}.',
    verbose=True,
    memory=True,
    backstory=(
       "You are a recommendation writer with the ability to analyze JSON data and create a compelling blog post with recommendations based on the context of {topic}."
    ),
    tools=[json_tool_faq, json_tool_inventory],
    allow_delegation=True
)