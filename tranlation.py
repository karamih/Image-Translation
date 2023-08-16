from dotenv import find_dotenv, load_dotenv
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI

load_dotenv(find_dotenv())

prompt = """
You are a translator. take the text and translate it to Persian. translated text must be clearly and simple.
INPUT: {text}
OUTPUT: 
"""

template = PromptTemplate(input_variables=['text'],
                          template=prompt)

model = ChatOpenAI(model_name='gpt-3.5-turbo')

translation_chain = LLMChain(llm=model, prompt=template)

