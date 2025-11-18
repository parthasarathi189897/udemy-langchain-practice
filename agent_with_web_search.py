from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
# from langchain_tavility import

load_dotenv()

@tool
def search_agent(query: str) -> str:
    """
    Tool that search over internet using tavily
    """
    return "Hello, world!"

def main():
    # create the llm first
    llm = ChatOpenAI(model="gpt-4", temperature=0)
    tools = [search_agent]
    agent = create_agent(llm=llm, tools=tools)
    agent.invoke(HumanMessage(content="What is the capital of Odisha?"))

if __name__ == "__main__":
    main()
