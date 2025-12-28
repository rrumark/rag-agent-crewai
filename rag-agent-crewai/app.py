import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

from crewai import Agent, Task, Crew
from crewai_tools import RagTool
from langchain_groq import ChatGroq
from config import *
import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)
warnings.filterwarnings("ignore", category=UserWarning)

llm = ChatGroq(model="llama-3.1-8b-instant", api_key=GROQ_API_KEY, max_tokens=1024)

rag_tool = RagTool(config=config, chunk_size=1200, chunk_overlap=200)
rag_tool.add("RAG_MAS.pdf", data_type="pdf_file")

# Agent:
sow_agent = Agent(
    role="Senior Statement of Work Assistant",
    goal="Assist in drafting, validating, and explaining elements of Statements of Work using retrieved knowledge",
    backstory="You are an expert in contract drafting and SOW compliance, specializing in multi-agent retrieval-augmented systems",
    verbose=True,
    allow_delegation=False,
    llm=llm,
    tools=[rag_tool],
    max_retry_limit=3
)

# Task:
task1 = Task(
    description="What process does the Drafting Agent follow before handing the document to the Compliance Agent?",
    expected_output="A comprehensive explanation of the Drafting Agent’s workflow and how it interacts with the Compliance Agent.",
    agent=sow_agent
)

# Crew:
crew = Crew(agents=[sow_agent], tasks=[task1], verbose=True)
task_output = crew.kickoff()
print(task_output)

from datetime import datetime

# Ensure outputs folder exists
os.makedirs("outputs", exist_ok=True)

# Save output with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
md_file = os.path.join("outputs", f"sow_agent_output_{timestamp}.md")
html_file = os.path.join("outputs", f"sow_agent_output_{timestamp}.html")

# Markdown file
with open(md_file, "w", encoding="utf-8") as f:
    f.write(f"# SOW Agent Output ({timestamp})\n\n")
    f.write(f"### Question:\n{task1.description}\n\n")
    f.write(f"### Answer:\n{str(task_output)}\n")

# HTML file (Medium-like style)
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>SOW Agent Output</title>
  <style>
    body {{
      font-family: Georgia, 'Times New Roman', Times, serif;
      max-width: 750px;
      margin: 40px auto;
      line-height: 1.7;
      font-size: 18px;
      color: #242424;
    }}
    h1, h2, h3 {{
      font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
      margin-top: 28px;
    }}
    h1 {{
      font-size: 32px;
    }}
    h2 {{
      font-size: 24px;
    }}
    h3 {{
      font-size: 20px;
    }}
    p {{
      margin: 16px 0;
    }}
  </style>
</head>
<body>
  <h1>SOW Agent Output ({timestamp})</h1>
  <h3>Question:</h3>
  <p>{task1.description}</p>
  <h3>Answer:</h3>
  <p>{str(task_output).replace('\n', '<br>')}</p>
</body>
</html>
"""

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"\n✅ Outputs saved to:\n- {md_file}\n- {html_file}")
