import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    "src/agents/researcher_writer.py",
    "src/agents/reporter.py",
    "src/agents/critic.py",
    "src/tasks/researcher_writer_task.py",
    "src/tasks/reporter_task.py",
    "src/tasks/critic_task.py",
    "utils/__init__.py",
    "utils/pdf_generator.py",
    "utils/email_sender.py",
    "utils/search_tool.py",
    "utils/llm.py",
    "config/settings.py",
    "main.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
    "test.py"
   
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")