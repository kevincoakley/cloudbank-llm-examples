from openai import OpenAI

# 1. Initialize the OpenAI client -- reads OPENAI_API_KEY and OPENAI_BASE_URL
#    to point at the AWS Bedrock Mantle endpoint
client = OpenAI()

# 2. Use the OpenAI Chat Completions API to call an xAI Grok model hosted on AWS Bedrock Mantle
completion = client.chat.completions.create(
    model="xai.grok-4.6",
    messages=[
        {"role": "user", "content": "Hello World!"}
    ]
)

print(completion.choices[0].message.content)
