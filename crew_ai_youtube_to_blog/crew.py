from crewai import Crew,Process
from tools import Youtube_tool
from agents import blog_researcher,blog_writer
from tasks import research_task,reporting_task
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4o"
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, reporting_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    verbose=True,
    share_crew=True
)

result=crew.kickoff(inputs={"topic": "Deepseek Destroys American AI "})