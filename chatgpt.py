import pandas as pd
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.agents.agent_types import AgentType
from langchain_openai import ChatOpenAI
import constants
from openai import OpenAI
import re
import os
os.environ["OPENAI_API_KEY"] = constants.OPENAI_API_KEY
client = OpenAI(api_key=constants.OPENAI_API_KEY)

# user_id = "sergio"
# df = pd.read_csv('Moneiva.csv')
# columns = df.columns
# llm = ChatOpenAI(temperature=0.5)
#agent_executer = create_csv_agent(llm, 'Moneiva.csv', verbose=True, allow_dangerous_code=True, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,)
agent = create_csv_agent(
    ChatOpenAI(temperature=0, model="gpt-4o-mini"),
    "Moneiva.csv",
    verbose=True,
    allow_dangerous_code=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
)

# agent.run("how many indexes are there?")
# def chat_with_gpt(prompt,user_id=user_id):
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {
#                 "role": "user",
#                 "content": prompt
#             },
#         ],
#         user=user_id)
#     return response.choices[0].message.content.strip()
#
# context = [ {'role':'system', 'content':"""
# You are a customer support AI agent. Greet the user and ask how you can help them today."""} ]


if __name__ == "__main__":
    while True:
        client_prompt = input("You: ")
        if client_prompt.lower() in ["quit", "exit", "bye"]:
            break

        answer = agent.invoke(client_prompt)
        print(answer)

        # client_prompt = input("You: ")
        # if client_prompt.lower() in ["quit", "exit", "bye"]:
        #     break
        # elif re.search(r'\baccesorial charges\b', client_prompt.lower()):
        # #elif client_prompt.lower() any ["accessorial charge", "freight charges"]:
        #     query = input("\nwhat is the load number?: ")
        #     if query == "exit":
        #         break
        #     if query.strip() == "":
        #         continue

        # Get the answer
        #     answer = agent_executer.invoke(query)
        #     print(answer)
        #
        #     # agent_executer.get_prompts()
        #     # response = agent_executer.invoke("what is the load number?") #response is a dictionary input, output
        #     # print(f"AI: {response}")
        # else:
        #     response = chat_with_gpt(client_prompt)
        #     print(f"AI: {response}")

