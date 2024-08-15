import constants
import openai
import panel as pn
import csv
openai.api_key=constants.OPENAI_API_KEY
model = "gpt-4"


#This function will receive the different messages in the conversation,
#and call OpenAI passing the full conversartion.
def continue_conversation(messages, temperature=0):
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message.content #this should be the response of the AI

def add_prompts_conversation(_): #_ means if there is value
    #Get the value introduced by the user
    prompt = client_prompt.value_input
    client_prompt.value = ''

    #Append to the context the User promnopt.
    context.append({'role':'user', 'content':f"{prompt}"})

    #Get the response.
    response = continue_conversation(context)

    #Add the response to the context.
    context.append({'role':'assistant', 'content':f"{response}"})

    with open('data.csv', 'w', newline='') as csvfile:
        fieldnames = ['load', 'phone', 'email']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'load': prompt})
        writer.writerow({'phone': context[0]})
        writer.writerow({"email": context[1]})


    #Update the panels to show the conversation.
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600)))

    return pn.Column(*panels)

#Creating the system part of the prompt
#Read and understand it.

context = [ {'role':'system', 'content':"""
You work collecting data information for a company called Moneiva.
You are in charge of the customer service department.

First welcome the customer, in a very friendly way, then collect their information.

Your instructions are:
-Collect their load number.
-Ask for a phone number
-Ask for an email address

"""} ]

#Creating the panel.
pn.extension()

panels = []

client_prompt = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="talk")

interactive_conversation = pn.bind(add_prompts_conversation, button_conversation)

dashboard = pn.Column(
    client_prompt,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True),
)

#To talk with the chat push the botton: 'talk' after your sentence.
dashboard.show()

# if __name__ == "__main__":
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["quit", "exit", "bye"]:
#             break
#
#         response = chat_with_gpt(user_input)
#         print(f"AI: {response}")