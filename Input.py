from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from langchain.agents import load_tools, AgentType, initialize_agent
from langchain.llms import GooglePalm
from langchain.llms.base import BaseLLM
import os
os.environ['SERPAPI_API_KEY'] = Serp_api_key


llm = GooglePalm(google_api_key=Google_api_key, temperature=0.8)


tools = load_tools(['wikipedia', 'serpapi', 'llm-math'], llm=llm)
memo = ConversationBufferWindowMemory(k=100)
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=memo,

)

convo = ConversationChain(
    memory=memo,
    llm = llm,
)
def question(query):
    response = convo.run(query)
    return response
