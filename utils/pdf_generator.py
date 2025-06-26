import re
import os
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def markdown_to_plaintext(line):
    if line.startswith("## "):
        return f"<b>{line.replace('## ', '').strip().upper()}</b>"
    elif line.startswith("# "):
        return f"<b>{line.replace('# ', '').strip().upper()}</b>"
    line = re.sub(r"^\* ", "• ", line)
    line = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", line)
    return line.strip()

def generate_pdf_report(content, filename="AI_Research_Report.pdf", author_name="Osita Wisdom Chinedu", project_title="AI Research on Food Security in Africa"):
    folder = "reports"
    os.makedirs(folder, exist_ok=True)

    filepath = os.path.join(folder, filename)
    doc = SimpleDocTemplate(filepath, pagesize=A4, rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=4, leading=14, fontSize=11))
    styles.add(ParagraphStyle(name='CustomTitle', parent=styles['Heading1'], alignment=1, fontSize=16, spaceAfter=12))
    styles.add(ParagraphStyle(name='CustomSubtitle', alignment=1, fontSize=12, spaceAfter=6))

    flowables = [
        Paragraph(project_title, styles['CustomTitle']),
        Paragraph(f"Author: {author_name}", styles['CustomSubtitle']),
        Paragraph(f"Date: {datetime.now().strftime('%B %d, %Y')}", styles['CustomSubtitle']),
        Spacer(1, 12)
    ]

    for line in content.strip().split("\n"):
        if line.strip():
            flowables.append(Paragraph(markdown_to_plaintext(line), styles['Justify']))
        else:
            flowables.append(Spacer(1, 10))

    doc.build(flowables)
    print(f"✅ PDF report generated at: {filepath}")
    return filepath
