import anthropic
import os

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

session = client.beta.managed_sessions.create(
    agent_id="agent_011CaoyQtSVqDWCr12D4KcJS",
    environment_id="env_013xv59MM2UtmLmsQ6S3NDBf",
    vault_ids=["vlt_011CaoZ9snbHpYLFSEZPrsiM"],
    extra_headers={"anthropic-beta": "managed-agents-2026-04-01"}
)

client.beta.managed_sessions.send_message(
    session_id=session.id,
    content="Good morning, run my daily briefing.",
    extra_headers={"anthropic-beta": "managed-agents-2026-04-01"}
)

print(f"Briefing session started: {session.id}")
