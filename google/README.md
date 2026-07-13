Getting started: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start

Create a new configuration for your profile:

```bash
gcloud config configurations create your-profile-name
```

Set the default configuration for the current session:

```bash
gcloud config configurations activate your-profile-name
```

Login to your Google account from the command line:

```bash
gcloud auth login
```

Set the default project for the current session:

```bash
gcloud config set project your-profile-name-project-id
```

Install python packages:

pip:

```bash
    pip install google-genai "anthropic[vertex]"
```

uv:

```bash
    uv add google-genai "anthropic[vertex]"
```