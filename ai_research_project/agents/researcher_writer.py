from crewai import Agent
from utils.llm import get_llm
from utils.search_tool import get_search_tool



def get_research_writer(): 
    return Agent(
    role="Researcher & Writer",
    goal=(
        "Research cutting-edge developments in {topic}, write insightful reports, "
        "and ensure content quality by performing a thorough critique before delivery."
    ),
    verbose=True,
    memory=True,
    backstory="An expert who researches, writes, and ensures reports are accurate, clear, and ethically sound.",
    tools=[get_search_tool()],
    allow_delegation=False,
    llm=get_llm()
)
