import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


api_key = os.getenv("OPENAI_API_KEY")
print(" DEBUG: OPENAI_API_KEY is:", "FOUND" if api_key else "NOT FOUND")


llm = OpenAI(api_key=api_key)

template = """
You are a stock market agent. Given a stock name and price, analyze and return a buy/sell/hold recommendation.
Stock: {stock}
Price: {price}
Response:
"""

prompt = PromptTemplate(input_variables=["stock", "price"], template=template)
chain = LLMChain(llm=llm, prompt=prompt)

def get_stock_analysis(stock, price):
    return chain.run(stock=stock, price=price)

