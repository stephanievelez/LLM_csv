import openai
import constants

openai.api_key=constants.OPENAI_API_KEY
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=
            #{"role": "system", "content": "You are an AI assistant."},
            {"role": "user", "content": prompt}
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print(f"AI: {response}")