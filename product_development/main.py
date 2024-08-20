# main.py

import sys
import os
import yaml
from crewai import Crew, Process, Agent, Task

# Set the environment variable for the OpenAI API key
os.environ["OPENAI_API_KEY"] = "your_complete_openai_api_key"

# Add the directory containing 'config' to the Python path
current_dir = os.path.dirname(__file__)
config_path = os.path.join(current_dir, 'config')
sys.path.append(config_path)

# Debugging: Print the sys.path
print("Current sys.path:", sys.path)

# Load the agents and tasks from YAML files instead of importing
with open(os.path.join(config_path, 'agents.yaml'), 'r') as file:
    agents_config = yaml.safe_load(file)

with open(os.path.join(config_path, 'tasks.yaml'), 'r') as file:
    tasks_config = yaml.safe_load(file)

# Create agents from the YAML configuration
innovator = Agent(
    role=agents_config['innovator']['role'],
    goal=agents_config['innovator']['goal'],
    backstory=agents_config['innovator']['backstory'],
    memory=agents_config['innovator']['memory']
)

engineer = Agent(
    role=agents_config['engineer']['role'],
    goal=agents_config['engineer']['goal'],
    backstory=agents_config['engineer']['backstory'],
    memory=agents_config['engineer']['memory']
)

market_analyst = Agent(
    role=agents_config['market_analyst']['role'],
    goal=agents_config['market_analyst']['goal'],
    backstory=agents_config['market_analyst']['backstory'],
    memory=agents_config['market_analyst']['memory']
)

# Create tasks from the YAML configuration
idea_generation_task = Task(
    description=tasks_config['idea_generation_task']['description'],
    expected_output=tasks_config['idea_generation_task']['expected_output'],
    agent=innovator
)

technical_development_task = Task(
    description=tasks_config['technical_development_task']['description'],
    expected_output=tasks_config['technical_development_task']['expected_output'],
    agent=engineer
)

market_analysis_task = Task(
    description=tasks_config['market_analysis_task']['description'],
    expected_output=tasks_config['market_analysis_task']['expected_output'],
    agent=market_analyst
)

def main():

    # Create the crew
    product_development_crew = Crew(
        agents=[innovator, engineer, market_analyst],
        tasks=[idea_generation_task, technical_development_task, market_analysis_task],
        process=Process.sequential  # This process ensures tasks are completed in order
    )

    # Kickoff the process
    result = product_development_crew.kickoff(inputs={})
    print(result)

if __name__ == "__main__":
    main()
