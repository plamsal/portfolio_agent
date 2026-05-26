import os
from pathlib import Path
from pypdf import PdfReader
from agents import Agent


def load_portfolio_context() -> str:
    """Load all context from me/ folder including summary, linkedin, and projects."""
    context = ""

    # Load summary.txt
    summary_path = Path("me/summary.txt")
    if summary_path.exists():
        context += f"## Summary\n{summary_path.read_text(encoding='utf-8')}\n\n"

    # Load linkedin.pdf
    linkedin_path = Path("me/linkedin.pdf")
    if linkedin_path.exists():
        reader = PdfReader(linkedin_path)
        linkedin_text = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                linkedin_text += text
        context += f"## LinkedIn Profile\n{linkedin_text}\n\n"

    # Load all project markdown files
    projects_path = Path("me/projects")
    if projects_path.exists():
        context += "## Projects\n"
        for project_file in projects_path.glob("*.md"):
            context += f"\n### {project_file.stem.replace('_', ' ').title()}\n"
            context += project_file.read_text(encoding="utf-8") + "\n"

    return context


# Load context once at startup
PORTFOLIO_CONTEXT = load_portfolio_context()


portfolio_agent = Agent(
    name="Portfolio Agent",
    instructions=f"""
    You are Pratik Lamsal's portfolio assistant. You represent Pratik professionally 
    on his personal website.

    You have full context about Pratik's background, experience, and projects below.
    Use this to answer any questions visitors ask — about his work, skills, projects, 
    background, or how to collaborate.

    Guidelines:
    - Always speak about Pratik in third person ("Pratik has worked on...", "His projects include...")
    - Be engaging, warm, and professional — like a knowledgeable colleague speaking on his behalf
    - For project questions, go deep — explain the problem, the solution, and the tech stack
    - If asked about something not covered in the context, be honest and suggest the visitor 
      reach out directly via email
    - Never make up information not present in the context

    --- PRATIK'S PORTFOLIO CONTEXT ---
    {PORTFOLIO_CONTEXT}
    --- END CONTEXT ---
    """,
    tools=[],
)