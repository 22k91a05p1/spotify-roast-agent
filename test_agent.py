import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM

# 1. Load keys
load_dotenv()

# 2. Setup Groq Model (The New Way)
# We use the native "LLM" class and the prefix "groq/"
my_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

# 3. Define the "Roaster" Agent
roaster = Agent(
    role='Mean Music Critic',
    goal='Roast the user based on their music taste',
    backstory="You are an elitist music snob. You hate mainstream pop and think you are better than everyone.",
    llm=my_llm,  # Pass the new LLM object here
    verbose=True
)

# 4. Define a simple Task
task = Task(
    description="Roast a user who likes 'Justin Bieber' and 'Baby Shark'. Be funny but rude.",
    expected_output="A short paragraph insulting the user's taste.",
    agent=roaster
)

# 5. Run the Crew
crew = Crew(
    agents=[roaster],
    tasks=[task],
    verbose=True
)

print("### STARTING ROAST ###")
result = crew.kickoff()
print("\n\n########################")
print("## FINAL ROAST RESULT ##")
print("########################\n")
print(result)