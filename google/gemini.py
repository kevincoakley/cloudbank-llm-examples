from google import genai

# 1. Initialize the client for Google Cloud Agent Platform
client = genai.Client(
    vertexai=True, 
    project="access-sta250002-540342", 
    location="us"
)

# 2. Create a chat session
# Use a Google model ID (e.g., "gemini-3.1-flash-lite") 
chat = client.chats.create(model="gemini-3.1-flash-lite")


# 3. Send the "Hello World" message
response = chat.send_message("Hello World!")

print(response.text)
