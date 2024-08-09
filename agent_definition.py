from crewai import Agent

new_agent = Agent(
    role='Data Analyst',
    goal='Analyze data and provide insights on {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "You are a skilled data analyst with a knack for uncovering insights "
        "from complex datasets. Your ability to interpret data helps in making "
        "informed decisions."
    ),
    tools=[]
)