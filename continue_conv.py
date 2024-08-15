import os
import constants
import m0constant
os.environ["OPENAI_API_KEY"] = constants.OPENAI_API_KEY
import constants
import openai
from mem0 import MemoryClient
import panel as pn

#openai.api_key=constants.OPENAI_API_KEY
client = MemoryClient(api_key=m0constant.api_key)


def handle_query(query, user_id=None):
    """
    Handle a customer query and store the relevant information in memory.

    :param query: The customer query to handle.
    :param user_id: Optional user ID to associate with the memory.
    """
    # Start a streaming chat completion request to the AI
    stream = openai.chat.completions.create(
        model="gpt-4",
        # stream=True,
        messages=[
            {"role": "system", "content": """
            You are a customer support AI agent. Greet the user and ask how you can help them today."""},
            {"role": "user", "content": query}
        ]
    )

    return stream.choices[0].message.content


client.add("load number is 134",user_id="Moneiva")
print(client.search("load number", user_id="Moneiva"))
stop = False