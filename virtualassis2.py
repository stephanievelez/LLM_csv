import os
from typing import Dict
import constants

from mem0 import Memory
os.environ["OPENAI_API_KEY"] = constants.OPENAI_API_KEY


m = Memory()

metadata: dict[str, str] = {"category": "hobbies"}
context: str = "sergio"
memory_message: str = "I am working on improving my tennis skills. Suggest some online courses."
# result: str = m.add(memory_message, user_id=context, metadata=metadata)


all_memories: list = m.get_all()
stop = 1

query_or_question = "What are my hobbies?"

# (Output) Retrieve memories related to a specific query or question
related_memories: list = m.search(query=query_or_question, user_id=context)
for item in related_memories:
    print(item['memory'])
    print(item['score'])

stoptwo = 2

# Retrieved memory --> 'Likes to play tennis on weekends'
