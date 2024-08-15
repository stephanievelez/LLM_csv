import os
import constants
import Qdrant
os.environ["OPENAI_API_KEY"] = constants.OPENAI_API_KEY
from openai import OpenAI
from mem0 import Memory
from mem0 import MemoryClient
#import chromadb works with python version <3.10
from qdrant_client import QdrantClient


#print(qdrant_client.get_collections())
class CustomerSupportAIAgent:
    def __init__(self):
        """
        Initialize the CustomerSupportAIAgent with memory configuration and OpenAI client.
        """
        config = {
            "vector_store": {
                "provider": "qdrant",
                # "provider": qdrant_client,
                "config": {
                    "url": Qdrant.url,
                    "api_key": Qdrant.api_key,
                }
            },
        }
        self.memory = Memory.from_config(config)
        self.client = OpenAI()
        #self.app_id = "customer-support"

    def handle_query(self, query, user_id=None):
        """
        Handle a customer query and store the relevant information in memory.

        :param query: The customer query to handle.
        :param user_id: Optional user ID to associate with the memory.
        """
        # Start a streaming chat completion request to the AI
        stream = self.client.chat.completions.create(
            model="gpt-4",
            stream=True,
            messages=[
                {"role": "system", "content": """
                You are a customer support AI agent for a company called Moneiva. Greet the user and ask how you can help them today.
                Ask for the user's inquiry and any additional information you need to assist them."""},
                {"role": "user", "content": query}
            ])
        # Store the query in memory
        # self.memory.add(query, user_id=user_id, metadata={"category": self.app_id})
        self.memory.add(query, user_id=user_id)

        # Print the response from the AI in real-time
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")

    def get_memories(self, user_id=None):
        """
        Retrieve all memories associated with the given customer ID.

        :param user_id: Optional user ID to filter memories.
        :return: List of memories.
        """
        return self.memory.get_all(user_id=user_id)

# Instantiate the CustomerSupportAIAgent
support_agent = CustomerSupportAIAgent()

# Define a customer ID
customer_id = "Moneiva"

if __name__ == "__main__":
    while True:
        query = input("You: ")
        if query.lower() in ["quit", "exit", "bye"]:
            break
        add_memory = support_agent.handle_query(query, user_id=customer_id)
        response = support_agent.get_memories(user_id=customer_id)

        print(f"AI: {response[0]['memory']}")
# Handle a customer query
# support_agent.handle_query("what's my additional charges?", user_id=customer_id)
