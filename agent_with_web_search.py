# fixed_agent_example.py
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

# If you use LangSmith manually (optional)
from langsmith import uuid7
# from langsmith import Client  # uncomment if you want to call LangSmith's Client

load_dotenv()


@tool
def search_agent(query: str) -> str:
    """
    Tool that searches the internet (stubbed).
    Replace the body with your tavily/web-search call.
    """
    # TODO: call tavily/web search here and return result text
    return "Hello, world!"


def main():
    # 1) create the llm (use model_name in recent langchain integrations)
    llm = ChatOpenAI(model_name="gpt-4", temperature=0)

    # 2) tools list (functions decorated with @tool)
    tools = [search_agent]

    # 3) create an agent (create_agent accepts the llm as `model` keyword)
    agent = create_agent(model=llm, tools=tools)

    # 4) invoke the agent with a messages list (HumanMessage inside a list)
    messages = [HumanMessage(content="What is the capital of Odisha?")]
    # agent.invoke expects a dict-like input; supply the messages list
    result = agent.invoke({"messages": messages})

    # print or process final result (result is typically a list of messages)
    print(result)


if __name__ == "__main__":
    main()
