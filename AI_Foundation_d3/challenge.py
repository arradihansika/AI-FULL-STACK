from ollama import chat

prompt = """
User: nice haircut
AI: That haircut is so good, barbers are going to study it in textbooks.

User: good game
AI: That game was so good, sports analysts are going to study it in textbooks.

User: you did a good job
AI: You didn't just do a good job, you basically redefined what good means for the rest of us.

User: you have a beautiful smile
AI:
"""

response = chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)
print(response.message.content)