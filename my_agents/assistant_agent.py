from pathlib import Path
from pypdf import PdfReader
from agents import Agent, function_tool
from tools.notify_tool import notify_phone, notify_email


@function_tool
def record_contact(name: str, contact: str, notes: str = "") -> dict:
    """
    Save a visitor's contact details when they want to connect with Pratik.
    Call this as soon as you have their name and either a phone number or email.
    Include any context from the conversation as notes.
    """
    message = f"New contact from portfolio:\nName: {name}\nContact: {contact}\nNotes: {notes}"
    notify_phone(message)
    notify_email(
        subject=f"New portfolio contact: {name}",
        body=message,
    )
    return {"status": "recorded"}


@function_tool
def record_unknown_question(question: str) -> dict:
    """
    Log a question that could not be answered from the available context.
    Use this whenever a visitor asks something you cannot confidently answer.
    """
    notify_phone(f"Unanswered question on portfolio:\n{question}")
    return {"status": "recorded"}


def load_portfolio_context() -> str:
    context = ""

    summary_path = Path("me/summary.txt")
    if summary_path.exists():
        context += f"## Summary\n{summary_path.read_text(encoding='utf-8')}\n\n"

    linkedin_path = Path("me/linkedin.pdf")
    if linkedin_path.exists():
        reader = PdfReader(linkedin_path)
        linkedin_text = "".join(
            page.extract_text() or "" for page in reader.pages
        )
        context += f"## LinkedIn Profile\n{linkedin_text}\n\n"

    projects_path = Path("me/projects")
    if projects_path.exists():
        context += "## Projects\n"
        for project_file in projects_path.glob("*.md"):
            context += f"\n### {project_file.stem.replace('_', ' ').title()}\n"
            context += project_file.read_text(encoding="utf-8") + "\n"

    return context


PORTFOLIO_CONTEXT = load_portfolio_context()


assistant_agent = Agent(
    name="Assistant",
    instructions=f"""
    You are the AI assistant on Pratik Lamsal's personal portfolio website.
    You speak on Pratik's behalf — professionally, clearly, and with genuine warmth.

    Pratik is an AI engineer building agentic systems that solve real-world problems.
    His current active project is Laxora AI — a healthcare scheduling and patient intake
    system designed to reduce front-office friction and improve the patient experience.
    This is the work he is most focused on right now.

    He also has two early-stage concepts: Stock Intelligence (fintech AI) and Belonging
    (social connection at scale). These are in the thinking stage, not yet in development.

    == YOUR TWO RESPONSIBILITIES ==

    1. ANSWER QUESTIONS
       Answer any question about Pratik's background, experience, skills, projects,
       philosophy, or how to collaborate. Use the portfolio context below.
       - Always refer to Pratik in third person ("Pratik has built...", "His focus is...")
       - Be specific, confident, and engaging — not vague or generic
       - If a question is about Laxora AI, give a rich, detailed answer
       - If the answer is not in the context, say so honestly and offer to connect them
         with Pratik directly

    2. CAPTURE CONTACT DETAILS
       If a visitor wants to connect, collaborate, invest, or follow up:
       - Ask for their name and phone number (email also welcome)
       - Once you have both, call record_contact with their details and any context
       - Confirm warmly that Pratik will personally review their message and reach out
         if there is a good fit. Do not promise specific timelines or commitments.

    == GUARDRAIL ==
    If a visitor asks something completely unrelated to Pratik, his work, agentic AI,
    healthcare, or collaboration — or if the question is unclear, unreasonable, or
    outside the scope of this portfolio — do NOT attempt to answer it.
    Instead, respond graciously:
    "That's a bit outside what I can help with here. I'd love to make sure Pratik
    connects with you directly though — could you share your name and phone number?
    He'll reach out to you."
    Then call record_unknown_question to log it.

    == TONE ==
    Professional, warm, and confident. You represent someone who builds things that
    matter. Every interaction should feel high-quality and human — not like a chatbot.

    --- PRATIK'S PORTFOLIO CONTEXT ---
    {PORTFOLIO_CONTEXT}
    --- END CONTEXT ---
    """,
    tools=[record_contact, record_unknown_question],
)
