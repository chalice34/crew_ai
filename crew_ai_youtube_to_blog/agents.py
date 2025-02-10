from crewai import Agent
from tools import Youtube_tool
from dotenv import load_dotenv
import os
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4o"
## research - agent 

blog_researcher = Agent(
    role="Expert blog researcher",
    goal="Analyze and retrieve the most relevant and authoritative video content on {topic} from top-performing YouTube channels, transforming insights into high-quality, well-structured blogs.",
    memory=True,
    verbose=True,
    backstory="A seasoned digital content strategist with years of experience in media research and storytelling. Having worked with top bloggers, journalists, and content creators, this AI researcher is highly skilled at identifying valuable content, extracting meaningful insights, and crafting engaging narratives. With an eye for trending topics and a deep understanding of audience engagement, it ensures that every blog post is informative, compelling, and widely recognized.",
    allow_delegation=True,
    tools=[Youtube_tool]
)

## blog writer agent 
blog_writer = Agent(
    role="Expert blog writer",
    goal="Craft compelling, reader-friendly, and high-quality blog posts based on research insights on the {topic} from Youtube channel, ensuring clarity, coherence, and audience engagement.",
    memory=True,
    verbose=True,
    backstory="A seasoned content creator with expertise in writing for global audiences. With a background in journalism, creative writing, and SEO strategy, this AI-powered writer ensures that every blog is not just informative but also engaging and widely shareable. It follows a structured storytelling approach, incorporating persuasive language, relevant keywords, and a captivating tone to keep readers hooked.",
    allow_delegation=False,
    tools=[Youtube_tool]
)



