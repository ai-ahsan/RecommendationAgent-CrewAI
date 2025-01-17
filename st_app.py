# FILE: streamlit_app.py

import streamlit as st
from crewai import Crew, Process
from agents import query_responder, blog_writer
from tasks import search_json_faq, search_json_inventory, write_task
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Forming the tech-focused crew with enhanced configurations
crew = Crew(
    agents=[query_responder, blog_writer],
    tasks=[search_json_inventory, search_json_faq, write_task],
    process=Process.sequential,  # Optional: Sequential task execution is default
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

# Streamlit interface
st.title("Crew AI Task Execution")

# Take input from the user
user_input = st.text_input("Enter the topic you want to search:")

if st.button("Submit"):
    # Start the task execution process with enhanced feedback
    result = crew.kickoff(inputs={'topic': user_input})
    
    if hasattr(result, 'token_usage'):
        token_usage = result.token_usage
        prompt_tokens = token_usage.prompt_tokens
        completion_tokens = token_usage.completion_tokens
        total_tokens = token_usage.total_tokens


    st.write(f"Result: {result}\n\nToken Usage:\nPrompt Tokens: {prompt_tokens}\nCompletion Tokens: {completion_tokens}\nTotal Tokens: {total_tokens}")


if __name__ == "__main__":
    st.write("Streamlit app is running")




