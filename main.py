from dotenv import load_dotenv
import os
from crewai import Crew, Process
from agent_definition import new_agent
from task_definition import new_task
import openai

# Load environment variables from the .env file
#load_dotenv()
#OPENAI_KEY=os.getenv('OPENAI_API_KEY')
OPENAI_API_KEY=''
# Create a crew with the new agent and task
crew = Crew(
    agents=[new_agent],
    tasks=[new_task],
    process=Process.sequential
)

# Run the crew with input data
result = crew.kickoff(inputs={'topic': 'Data Analysis for Sales Data'})
print(result)