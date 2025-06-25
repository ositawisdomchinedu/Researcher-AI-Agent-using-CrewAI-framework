from crewai import Task
from utils.search_tool import get_search_tool
from ai_research_project.agents.researcher_writer import get_research_writer


def get_researcher_writer_task():
    return Task(
    description=(
    "Conduct web research on the topic: '{topic}'. Gather accurate and up-to-date information from credible sources. "
    "Then, convert the research findings into a professional, well-organized report suitable for PDF format. "
    "Structure the report using clear headings and subheadings for each subtopic. "
    "Use bullet points for clarity where needed, ensure smooth flow of ideas, and include properly formatted in-text citations and a references section."

    ),
    expected_output=(
        "- A polished, print-ready PDF report that includes:\n"
        "- A formal summary of findings\n"
        "- Sections organized by subtopics with clear headings\n"
        "- Bullet points or numbered lists for clarity\n"
        "- Inline hyperlinks to cited sources\n"
        "- A properly formatted references section at the end\n"
        "- Clear, professional, and accessible language throughout"
    ),
    tools=[get_search_tool()], 
    agent=get_research_writer(),
    output_file="final_research_report.pdf"
)
