from crewai import Task
from tools import Youtube_tool
from agents import blog_researcher,blog_writer


# research task

research_task = Task(
    description="""
        Identify and analyze the most relevant and authoritative YouTube videos on {topic}.
        Extract key insights, trends, and expert opinions from these videos.
        Structure the findings into a well-formatted blog with clear headings, bullet points, and proper spacing for readability.
    """,
    expected_output="""
        - A well-structured blog post with:
            - An engaging introduction summarizing the key takeaways.
            - Clearly formatted headings and subheadings for readability.
            - Bullet points highlighting important insights.
            - Proper white space and paragraph structuring for a smooth reading experience.
            - A conclusion summarizing the insights and providing actionable takeaways.
    """,
    tools=[Youtube_tool],
    agent=blog_researcher
)


reporting_task = Task(
    description="""
        Expand the extracted insights into a comprehensive, well-structured report.
        Ensure each section is detailed, informative, and formatted for clarity.
        Use markdown formatting for structured presentation.
    """,
    expected_output="""
        - A fully detailed and structured report with:
            - A well-written introduction providing context and objectives.
            - Clearly defined main topics, each expanded into in-depth sections.
            - Bullet points, subheadings, and key takeaways for readability.
            - Relevant examples, data points, or expert insights where applicable.
            - A conclusion summarizing findings and key insights.
        - Formatted for easy readability.
    """,
    agent=blog_writer,
    output_file="report_desh.txt"
)



