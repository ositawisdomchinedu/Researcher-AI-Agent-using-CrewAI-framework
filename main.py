from crewai import Crew, Process
from ai_research_project.agents.researcher_writer import get_research_writer
from ai_research_project.tasks.researcher_writer_task import get_researcher_writer_task
from utils.pdf_generator import generate_pdf_report
from utils.email_sender import send_email_with_attachment
from config.settings import RECIPIENT_EMAIL

def main():
    topic = "The role of AI in improving food security in Africa"

    researcher = get_research_writer()
    task = get_researcher_writer_task()

    crew = Crew(
        agents=[researcher],
        tasks=[task],
        process=Process.sequential
    )

    result = crew.kickoff(inputs={"topic": topic})
    print(result)

    pdf_path = generate_pdf_report(
        content=str(result),
        filename="AI_Research_Report.pdf",
        author_name="Osita Wisdom Chinedu",
        project_title="AI Research on Food Security in Africa"
    )

    send_email_with_attachment(
        receiver_email=RECIPIENT_EMAIL,
        subject="AI Research Report",
        body="Attached is your finalized research report.",
        attachment_path=pdf_path
    )

if __name__ == "__main__":
    main()
