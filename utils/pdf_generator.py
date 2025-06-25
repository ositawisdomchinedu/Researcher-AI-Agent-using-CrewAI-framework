import re
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from datetime import datetime
import os

def markdown_to_plaintext(line):
    # Convert markdown headers
    if line.startswith("## "):
        return f"<b>{line.replace('## ', '').strip().upper()}</b>"
    elif line.startswith("# "):
        return f"<b>{line.replace('# ', '').strip().upper()}</b>"
    # Convert bullets
    line = re.sub(r"^\* ", "• ", line)
    # Convert bold
    line = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", line)
    return line.strip()

def generate_pdf_report(content, filename="final_report.pdf", folder="reports",
                        author_name="Osita Wisdom Chinedu",
                        project_title="AI Research on Food Security in Africa"):

    if not os.path.exists(folder):
        os.makedirs(folder)

    filepath = os.path.join(folder, filename)
    doc = SimpleDocTemplate(filepath, pagesize=A4,
                            rightMargin=50, leftMargin=50,
                            topMargin=50, bottomMargin=50)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=4, leading=14, fontSize=11))
    styles.add(ParagraphStyle(name='CustomTitle', parent=styles['Heading1'], alignment=1, fontSize=16, spaceAfter=12))
    styles.add(ParagraphStyle(name='CustomSubtitle', alignment=1, fontSize=12, spaceAfter=6))

    flowables = []
    flowables.append(Paragraph(project_title, styles['CustomTitle']))
    flowables.append(Paragraph(f"Author: {author_name}", styles['CustomSubtitle']))
    flowables.append(Paragraph(f"Date: {datetime.now().strftime('%B %d, %Y')}", styles['CustomSubtitle']))
    flowables.append(Spacer(1, 12))

    for line in content.strip().split("\n"):
        if line.strip() == "":
            flowables.append(Spacer(1, 10))
        else:
            clean_line = markdown_to_plaintext(line)
            flowables.append(Paragraph(clean_line, styles['Justify']))

    doc.build(flowables)
    print(f"✅ PDF report generated at: {filepath}")
    return filepath
