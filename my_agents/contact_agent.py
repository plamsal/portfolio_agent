import os
from agents import Agent, function_tool
from tools.notify_tool import notify_phone, notify_email


@function_tool
def record_user_details(email: str, name: str = "Name not provided", notes: str = "not provided") -> dict:
    """
    Record that a user is interested in getting in touch and provided their email address.
    Always use this when a user shares their email. Capture their name and any context from
    the conversation as notes.
    """
    message = f"New contact from portfolio:\nName: {name}\nEmail: {email}\nNotes: {notes}"
    notify_phone(message)
    notify_email(
        subject=f"New portfolio contact: {name}",
        body=message
    )
    return {"recorded": "ok"}


@function_tool
def record_unknown_question(question: str) -> dict:
    """
    Record any question that couldn't be answered. Always use this when you don't know
    the answer to something — even if it seems trivial or unrelated to Pratik's career.
    """
    notify_phone(f"Unanswered question on portfolio:\n{question}")
    return {"recorded": "ok"}


contact_agent = Agent(
    name="Contact Agent",
    instructions="""
    You are a professional contact assistant on Pratik Lamsal's portfolio website.
    
    Your two jobs:
    
    1. CAPTURE LEADS
       - If a user expresses interest in working together, collaborating, or getting in touch,
         ask for their email address naturally and warmly.
       - Once you have their email, use record_user_details to save it along with their name
         and a brief note about what they're interested in.
       - Confirm to the user that Pratik will be in touch.
    
    2. RECORD UNKNOWN QUESTIONS
       - If a question comes up that you cannot answer confidently, use record_unknown_question
         to log it so Pratik can follow up or improve his portfolio.
       - Never make up answers. If unsure, record it and let the user know Pratik will follow up.
    
    Tone: warm, professional, concise. You represent Pratik — make a great first impression.
    """,
    tools=[record_user_details, record_unknown_question],
)