from crewai import Task
from agent_definition import new_agent

new_task = Task(
    description=(
        "Analyze the dataset provided and generate a report with key insights. "
        "Focus on identifying trends, patterns, and anomalies. Your final report "
        "should include visualizations and a summary of your findings."
    ),
    expected_output='A detailed report with visualizations and a summary of key insights.',
    tools=[],
    agent=new_agent
)