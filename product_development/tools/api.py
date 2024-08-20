import os

# Set the environment variable for the OpenAI API key
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"

print(f"OPENAI_API_KEY is set to: {os.getenv('OPENAI_API_KEY')}")  # Debugging: Verify the key is set

# Rest of your imports and code
import sys
import yaml
from crewai import Crew, Process, Agent, Task