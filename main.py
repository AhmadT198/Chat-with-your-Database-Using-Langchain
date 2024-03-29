from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)
from langchain.schema import SystemMessage
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
from langchain_community.llms import OpenLLM
from tools.sql import run_query_tool, list_tables, describe_tables_tool
from tools.report import write_report_tool
load_dotenv()

tables = list_tables()
chat = ChatOpenAI()

prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(content=
            f"""You are in AI that has access to a SQLite database.\n
            The database has tables of: {tables}\n
            Do not make any assumptions about what tables exist 
            or what comlumns exist. Instead, use the 'describe_tables' function to know the tables schema. """
            ),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True # return_messages(as messagePrompt objects not strings)
) 
tools = [
    run_query_tool,
    describe_tables_tool,
    write_report_tool
]
agent = OpenAIFunctionsAgent(
    llm=chat,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(
    agent=agent,
    # verbose=True,
    tools=tools,
    memory=memory
)


while True:
    message = input(">> ")
    print(agent_executor(message)["output"])
