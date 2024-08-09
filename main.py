#Import Dependencies
from dotenv import load_dotenv
import os
from crewai import Crew, Process
from agent_definition import new_agent
from task_definition import new_task
import openai


# Create a crew with the new agent and task
crew = Crew(
    agents=[new_agent],
    tasks=[new_task],
    process=Process.sequential
)

# Run the crew with input data
result = crew.kickoff(inputs={'topic': 'Data Analysis for Sales Data'})
print(result)