__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import os
import streamlit as st
from crewai import Crew, Process
from ai_research_project.agents.researcher_writer import get_research_writer
from ai_research_project.tasks.researcher_writer_task import get_researcher_writer_task
from utils.pdf_generator import generate_pdf_report
from utils.email_sender import send_email_with_attachment

# Read secrets from Streamlit's secure storage (no need for dotenv in Streamlit Cloud)
RECIPIENT_EMAIL = st.secrets.get("RECIPIENT_EMAIL", "")
SENDER_EMAIL = st.secrets.get("SENDER_EMAIL", "")
SENDER_PASSWORD = st.secrets.get("SENDER_PASSWORD", "")

# Initialize Streamlit session state
if 'pdf_path' not in st.session_state:
    st.session_state.pdf_path = None

if 'result' not in st.session_state:
    st.session_state.result = None

# App UI
st.set_page_config(page_title="AI Research Assistant", layout="centered")
st.title("📘 AI Research Report Generator")
st.markdown("Generate a research report using CrewAI agents, convert it to PDF, and email it automatically.")

# Input Form
with st.form("research_form"):
    topic = st.text_input("Enter research topic", value="The role of AI in improving food security in Africa")
    author = st.text_input("Your name", value="Osita Wisdom Chinedu")
    email = st.text_input("Recipient Email", value=RECIPIENT_EMAIL)
    submitted = st.form_submit_button("Generate Report")

if submitted:
    with st.spinner("🔎 Researching and writing report..."):
        researcher = get_research_writer()
        task = get_researcher_writer_task()

        crew = Crew(
            agents=[researcher],
            tasks=[task],
            process=Process.sequential
        )

        result = crew.kickoff(inputs={"topic": topic})

    st.success("✅ Report generated!")

    # Show the report
    st.subheader("📄 Report Preview")
    st.text_area("Generated Report", value=result, height=300)

    # Generate PDF
    with st.spinner("📄 Creating PDF..."):
        pdf_path = generate_pdf_report(
            content=str(result),
            filename="AI_Research_Report.pdf",
            author_name=author,
            project_title=f"AI Research on {topic}"
        )

    # ✅ Ensure file path is valid
    if not pdf_path or not os.path.isfile(pdf_path):
        st.error("❌ Failed to generate PDF file. Please check path or permissions.")
        st.stop()

    st.session_state.pdf_path = pdf_path
    st.session_state.result = result
    st.success("✅ PDF Created!")

    # Download Button
    with open(pdf_path, "rb") as f:
        st.download_button(
            label="📥 Download Report as PDF",
            data=f,
            file_name="AI_Research_Report.pdf",
            mime="application/pdf"
        )

# Email Report
if st.button("📧 Send Report to Email"):
    if st.session_state.pdf_path:
        with st.spinner("📤 Sending email..."):
            status = send_email_with_attachment(
                receiver_email=email,
                subject="AI Research Report",
                body="Attached is your finalized AI-generated research report.",
                attachment_path=st.session_state.pdf_path
            )

        # Status display
        st.write(f"📬 Email send status: `{status}`")  # Show raw status

        if status == "SUCCESS":
            st.success(f"📧 Email sent to {email}")
        elif status.startswith("ERROR"):
            st.error(f"❌ Email failed: {status}")
        else:
            st.warning("❓ Unexpected result while trying to send email.")

    
