import requests
import os

ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]

headers = {
    "x-api-key": ANTHROPIC_API_KEY,
    "anthropic-beta": "managed-agents-2026-04-01",
    "Content-Type": "application/json"
}

# Step 1 - Create session
session_response = requests.post(
    "https://api.anthropic.com/v1/managed-sessions",
    headers=headers,
    json={
        "agent_id": "agent_011CaoyQtSVqDWCr12D4KcJS",
        "environment_id": "env_013xv59MM2UtmLmsQ6S3NDBf",
        "vault_ids": ["vlt_011CaoZ9snbHpYLFSEZPrsiM"]
    }
)

print("Session response:", session_response.status_code, session_response.text)
session = session_response.json()
session_id = session["id"]

# Step 2 - Send message
message_response = requests.post(
    f"https://api.anthropic.com/v1/managed-sessions/{session_id}/events",
    headers=headers,
    json={
        "type": "user_message",
        "content": "Good morning, run my daily briefing."
    }
)

print("Mess
