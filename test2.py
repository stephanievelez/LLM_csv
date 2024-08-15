import os
import constants
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=constants.OPENAI_API_KEY,
)


def ai_agent(query, temperature=0):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI assistant."},
            {"role": "user", "content": query}
        ],
        temperature=temperature
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = ai_agent(user_input)
        print(f"AI: {response}")
