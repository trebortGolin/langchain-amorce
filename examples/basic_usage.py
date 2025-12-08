"""
Basic LangChain-Amorce Example

Shows how to secure a LangChain agent with 2 lines of code.
"""

from langchain_amorce import AmorceAgent
from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun

def main():
    print("🔐 LangChain-Amorce Basic Example\n")
    
    # Create tools
    search = DuckDuckGoSearchRun()
    
    # Create secure agent (2 lines!)
    print("Creating secure agent...")
    agent = AmorceAgent(
        llm=ChatOpenAI(model="gpt-4"),
        tools=[search],
        secure=True  # ← Adds Amorce security
    )
    
    print(f"✅ Agent created with ID: {agent.agent_id}\n")
    
    # Use normally - all actions are now signed
    query = "What's the latest AI news?"
    print(f"Query: {query}")
    print("Running...")
    
    result = agent.run(query)
    
    print(f"\nResult: {result['output']}")
    print(f"\nSecurity Metadata:")
    print(f"  Agent ID: {result['agent_id']}")
    print(f"  Signature: {result['signature'][:50]}...")
    print(f"  Protocol: {result['protocol']}")
    print(f"  Security Layer: {result['security_layer']}")

if __name__ == "__main__":
    main()
