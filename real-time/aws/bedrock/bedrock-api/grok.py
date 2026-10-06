import boto3

# 1. Initialize the Bedrock Runtime client for AWS Bedrock
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# 2. Use Bedrock's Converse API to call an xAI Grok model (Grok is only
#    available through a cross-Region inference profile, hence the "us." prefix)
response = client.converse(
    modelId="us.xai.grok-4.6",
    messages=[
        {"role": "user", "content": [{"text": "Hello World!"}]}
    ]
)

# Grok is a reasoning model, so the first content block may be
# "reasoningContent" rather than "text" -- find the text block instead
# of assuming it's content[0].
for block in response["output"]["message"]["content"]:
    if "text" in block:
        print(block["text"])
        break
