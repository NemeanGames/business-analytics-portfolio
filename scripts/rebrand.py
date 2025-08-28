import requests
import base64
import json

# Configuration
REPO = "NemeanGames/business-analytics-portfolio"  # Update with your GitHub repo
BRANCH = "main"
FILE_PATH = "README.md"
TOKEN = "ghp_your_token_here"  # Replace with your GitHub personal access token or use environment variable

# Load metadata
with open("metadata.json") as f:
    meta = json.load(f)

# Prepare replacements
replacements = {
    "{{PROJECT_TITLE}}": meta["project_title"],
    "{{PROJECT_DESCRIPTION}}": meta["project_description"],
    "{{KEY_SKILLS}}": ", ".join(meta["skills"]),
    "{{DATASETS_USED}}": ", ".join(meta["datasets"]),
    "{{INDUSTRY}}": meta["industry"]
}

# Fetch the current README content
url = f"https://api.github.com/repos/{REPO}/contents/{FILE_PATH}"
headers = {"Authorization": f"token {TOKEN}"}
response = requests.get(url, headers=headers).json()
sha = response["sha"]
content = base64.b64decode(response["content"]).decode("utf-8")

# Replace placeholders
for placeholder, value in replacements.items():
    content = content.replace(placeholder, value)

# Prepare commit data
updated_content = base64.b64encode(content.encode("utf-8")).decode("utf-8")
commit_message = f"Rebrand portfolio for {meta['industry']}"
data = {
    "message": commit_message,
    "content": updated_content,
    "branch": BRANCH,
    "sha": sha
}

# Update the README via GitHub API
r = requests.put(url, headers=headers, data=json.dumps(data))
print("Rebrand complete:", r.status_code)
