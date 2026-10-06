from openai import OpenAI

# 1. Initialize the OpenAI client -- reads OPENAI_API_KEY and OPENAI_BASE_URL
#    to point at the AWS Bedrock OpenAI v1 endpoint
client = OpenAI()

# 2. Use the OpenAI Chat Completions API to call an xAI Grok model on AWS Bedrock
#    (Grok is only available through a cross-Region inference profile, hence
#    the "us." prefix).
completion = client.chat.completions.create(
    model="us.xai.grok-4.6",  # your Bedrock cross-Region inference profile ID
    messages=[
        {"role": "user", "content": "Hello World!"}
    ]
)

print(completion.choices[0].message.content)
