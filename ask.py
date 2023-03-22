from gpt_index import SimpleDirectoryReader,GPTListIndex,GPTSimpleVectorIndex,LLMPredictor,PromptHelper
from langchain import OpenAI
import os

os.environ["OPEN_API_KEY"]='xx-xxxxxxx'# give your openai api key

def ask_bot(input_index='index.json'):
    index = GPTSimpleVectorIndex.load_from_disk(input_index)
    while True:
        query=input('What do you want to ask the bot? \n')
        response = index.query(query,response_mode="compact")
        print('\n Bot says: \n\n'+ response.response + "\n\n\n")


ask_bot('index.json');
