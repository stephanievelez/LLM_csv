import m0constant
from typing import Dict, Any, List

from mem0 import MemoryClient
client: MemoryClient = MemoryClient(api_key=m0constant.api_key)

context = "sergio"
# # list_of_messages: list[dict[str, str] | dict[str, str]] = [
# #     {"role": "user", "content": "I Love Basketball"},
# #     {"role": "assistant", "content": "Noted! You Love Basketball."}
# # ]
#
# client.add(list_of_messages, user_id=context)


# Later, retrieve and use the preference
query: str = "What Sports Do I Like?"
related_memories: list = client.search(query, user_id=context)

for item in related_memories:
    print(item['memory'])
    print(item['score'])
