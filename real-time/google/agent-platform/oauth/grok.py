import os

import google.auth
import google.auth.transport.requests
from openai import OpenAI

# 1. Read GOOGLE_CLOUD_PROJECT to build the Google Agent Platform MaaS endpoint
project_id = os.environ["GOOGLE_CLOUD_PROJECT"]  # your Google Cloud project ID

# 2. Fetch GCP OAuth credentials
credentials, _ = google.auth.default(
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)
auth_req = google.auth.transport.requests.Request()
credentials.refresh(auth_req)

# 3. Point the OpenAI SDK to the Google Agent Platform MaaS global endpoint
client = OpenAI(
    base_url=f"https://aiplatform.googleapis.com/v1/projects/{project_id}/locations/global/endpoints/openapi",
    api_key=credentials.token,
)

# 4. Use the managed API ID: "xai/grok-4.6"
response = client.chat.completions.create(
    model="xai/grok-4.6",
    messages=[{"role": "user", "content": "Hello World!"}],
)

print(response.choices[0].message.content)
