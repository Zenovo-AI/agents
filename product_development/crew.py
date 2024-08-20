# crew.py
import os
from crewai import Agent, Task, Crew, Process

# Ensure your API keys and any necessary environment variables are set
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"

# Load the agents and tasks from the YAML files
from config.agents import innovator, engineer, market_analyst
from config.tasks import idea_generation_task, technical_development_task, market_analysis_task


# Create the Crew
product_development_crew = Crew(
    agents=[innovator, engineer, market_analyst],
    tasks=[idea_generation_task, technical_development_task, market_analysis_task],
    process=Process.sequential  # This process ensures tasks are completed in order
)

# Kickoff the process with a specific input if needed
result = product_development_crew.kickoff(inputs={})
print(result)
