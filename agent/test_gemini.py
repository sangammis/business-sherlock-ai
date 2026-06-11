from agent.gemini_client import model

response = model.generate_content(
    "What is a payment gateway?"
)

print(response.text)