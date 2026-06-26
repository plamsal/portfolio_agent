from dotenv import load_dotenv
load_dotenv()

import gradio as gr
from agents import Runner
from coordinator import coordinator
import asyncio


# ── Project cards data ──────────────────────────────────────────────
PROJECTS = [
    {
        "name": "Laxora AI",
        "tag": "Active · Healthcare AI",
        "desc": "Active healthcare AI project focused on safe scheduling and guided patient intake — helping clinics reduce front-office friction and improve patient experience.",
        "stack": "Agentic AI · AWS · Healthcare Automation",
        "color": "#00FFB2",
        "icon": "🏥",
    },
    {
        "name": "Stock Intelligence",
        "tag": "Brainstorming · Fintech AI",
        "desc": "Brainstorming-stage idea for an AI-powered stock intelligence workflow that discovers market opportunities and monitors signals automatically.",
        "stack": "Lambda · S3 · Telegram",
        "color": "#00B2FF",
        "icon": "📈",
    },
    {
        "name": "Belonging",
        "tag": "Brainstorming · Social AI",
        "desc": "Brainstorming-stage concept for a B2B platform helping universities, therapists, and organizations reduce loneliness at scale.",
        "stack": "Early Stage · B2B · Social Impact",
        "color": "#FF6B6B",
        "icon": "🤝",
    },
]


def build_project_cards():
    cards_html = ""
    for p in PROJECTS:
        cards_html += f"""
        <div class="project-card" onclick="document.querySelector('textarea').value='Tell me about {p['name']}'; document.querySelector('textarea').dispatchEvent(new Event('input'))">
            <div class="card-header">
                <span class="card-icon">{p['icon']}</span>
                <span class="card-tag" style="color:{p['color']}">{p['tag']}</span>
            </div>
            <div class="card-name">{p['name']}</div>
            <div class="card-desc">{p['desc']}</div>
            <div class="card-stack">{p['stack']}</div>
        </div>
        """
    return cards_html

CUSTOM_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;800&display=swap');

:root {
    --bg-primary: #080B0F;
    --bg-secondary: #0D1117;
    --bg-card: #111820;
    --bg-input: #0D1117;
    --border: #1E2D3D;
    --border-bright: #2E4A6A;
    --accent-green: #00FFB2;
    --accent-blue: #00B2FF;
    --accent-red: #FF6B6B;
    --text-primary: #E8EDF3;
    --text-secondary: #6B8A9E;
    --text-muted: #3A5068;
}

* { box-sizing: border-box; }

body, .gradio-container {
    background: var(--bg-primary) !important;
    font-family: 'Syne', sans-serif !important;
    color: var(--text-primary) !important;
}

.main-wrapper {
    display: grid;
    grid-template-columns: 300px 1fr;
    gap: 0;
    height: 100vh;
    max-height: 100vh;
    overflow: hidden;
}

.sidebar {
    background: var(--bg-secondary);
    border-right: 1px solid var(--border);
    padding: 28px 20px;
    display: flex;
    flex-direction: column;
    gap: 20px;
    overflow-y: auto;
}

.profile-section {
    text-align: center;
    padding-bottom: 20px;
    border-bottom: 1px solid var(--border);
}

.profile-name {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 1.3rem;
    color: var(--text-primary);
    margin: 12px 0 4px;
    letter-spacing: -0.5px;
}

.profile-title {
    font-family: 'Space Mono', monospace;
    font-size: 0.65rem;
    color: var(--accent-green);
    letter-spacing: 2px;
    text-transform: uppercase;
}

.status-dot {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 0.7rem;
    color: var(--text-secondary);
    margin-top: 8px;
    font-family: 'Space Mono', monospace;
}

.status-dot::before {
    content: '';
    width: 6px;
    height: 6px;
    background: var(--accent-green);
    border-radius: 50%;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.3; }
}

.section-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.6rem;
    color: var(--text-muted);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.project-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 14px;
    margin-bottom: 10px;
    cursor: pointer;
    transition: all 0.2s ease;
    position: relative;
    overflow: hidden;
}

.project-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--border-bright), transparent);
}

.project-card:hover {
    border-color: var(--border-bright);
    transform: translateY(-1px);
    background: #141D27;
}

.card-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 6px;
}

.card-icon { font-size: 1rem; }

.card-tag {
    font-family: 'Space Mono', monospace;
    font-size: 0.58rem;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.card-name {
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 0.95rem;
    color: var(--text-primary);
    margin-bottom: 5px;
}

.card-desc {
    font-size: 0.72rem;
    color: var(--text-secondary);
    line-height: 1.5;
    margin-bottom: 8px;
}

.card-stack {
    font-family: 'Space Mono', monospace;
    font-size: 0.6rem;
    color: var(--text-muted);
}

.chat-wrapper {
    display: flex;
    flex-direction: column;
    height: 100vh;
    overflow: hidden;
}

.chat-header {
    padding: 20px 28px;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.chat-title {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 1rem;
    color: var(--text-primary);
}

.chat-subtitle {
    font-family: 'Space Mono', monospace;
    font-size: 0.6rem;
    color: var(--text-muted);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 2px;
}

.gradio-chatbot {
    background: transparent !important;
    border: none !important;
}

.gr-text-input, textarea {
    background: var(--bg-input) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--text-primary) !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 0.88rem !important;
}

button.primary {
    background: linear-gradient(135deg, #00FFB2, #00B2FF) !important;
    border: none !important;
    border-radius: 8px !important;
    color: #080B0F !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.75rem !important;
    font-weight: 700 !important;
    letter-spacing: 1px !important;
    transition: opacity 0.2s !important;
}

button.primary:hover { opacity: 0.85 !important; }

::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border-bright); border-radius: 2px; }

footer { display: none !important; }
.built-with { display: none !important; }
"""

async def chat(message: str, history: list) -> str:
    result = await Runner.run(coordinator, message)
    return result.final_output

def chat_sync(message: str, history: list) -> str:
    return asyncio.run(chat(message, history))

# ── Build UI ────────────────────────────────────────────────────────
with gr.Blocks(title="Pratik Lamsal — AI Engineer") as demo:

    with gr.Row(elem_classes="main-wrapper"):

        # ── Sidebar ──
        with gr.Column(elem_classes="sidebar", scale=0, min_width=300):
            gr.HTML(f"""
            <div class="profile-section">
                <div style="width:64px;height:64px;background:linear-gradient(135deg,#00FFB2,#00B2FF);
                     border-radius:50%;margin:0 auto;display:flex;align-items:center;
                     justify-content:center;font-size:1.6rem;">P</div>
                <div class="profile-name">Pratik Lamsal</div>
                <div class="profile-title">AI · Cloud · Agentic Systems</div>
                <div class="status-dot">Available for collaboration</div>
            </div>
            <div class="section-label">Projects</div>
            {build_project_cards()}
            <div style="margin-top:auto;padding-top:20px;border-top:1px solid var(--border)">
                <div class="section-label">Quick actions</div>
                <div style="display:flex;flex-direction:column;gap:8px;margin-top:8px">
                    <div class="project-card" style="padding:10px 14px;cursor:pointer"
                         onclick="document.querySelector('textarea').value='I would like to get in touch with Pratik'">
                        <span style="font-size:0.75rem;color:var(--accent-green);font-family:Space Mono,monospace">
                            ✉ GET IN TOUCH
                        </span>
                    </div>
                    <div class="project-card" style="padding:10px 14px;cursor:pointer"
                         onclick="document.querySelector('textarea').value='What is Pratik\\'s background in AI?'">
                        <span style="font-size:0.75rem;color:var(--accent-blue);font-family:Space Mono,monospace">
                            ◈ BACKGROUND & SKILLS
                        </span>
                    </div>
                </div>
            </div>
            """)

        # ── Chat ──
        with gr.Column(elem_classes="chat-wrapper", scale=1):
            gr.HTML("""
            <div class="chat-header">
                <div>
                    <div class="chat-title">Ask me anything</div>
                    <div class="chat-subtitle">Powered by multi-agent AI · GPT-4o</div>
                </div>
                <div style="font-family:Space Mono,monospace;font-size:0.6rem;
                     color:var(--accent-green);letter-spacing:2px">● LIVE</div>
            </div>
            """)

            chatbot = gr.Chatbot(
                value=[],
                height=520,
                show_label=False,
                elem_classes="gradio-chatbot",
            )

            with gr.Row():
                msg = gr.Textbox(
                    placeholder="Ask about projects, background, or collaboration...",
                    show_label=False,
                    scale=5,
                    container=False,
                )
                submit = gr.Button("SEND →", scale=1, variant="primary")

            gr.Examples(
                examples=[
                    "What projects are you working on?",
                    "Tell me about the Patient Intake Agent",
                    "How can I collaborate with Pratik?",
                    "What's Pratik's background in agentic AI?",
                ],
                inputs=msg,
                label="",
            )

            def respond(message, history):
                response = chat_sync(message, history)
                history.append((message, response))
                return "", history

            submit.click(respond, [msg, chatbot], [msg, chatbot])
            msg.submit(respond, [msg, chatbot], [msg, chatbot])


if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        css=CUSTOM_CSS,
    )
