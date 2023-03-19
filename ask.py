from gpt_index import SimpleDirectoryReader,GPTListIndex,GPTSimpleVectorIndex,LLMPredictor,PromptHelper
from langchain import OpenAI
import os

os.environ["OPEN_API_KEY"]='xx-xxxxxxx'# give your openai api key

def construct_index (directory_path):
    max_input_size=4096
    num_outputs = 256
    max_chunk_overlap=20
    chunk_size_limit=600

    prompt_helper = PromptHelper(max_input_size,num_outputs,max_chunk_overlap,chunk_size_limit=chunk_size_limit)
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name='text-ada-001',max_tokens=num_outputs)) #text-davinci-003
    documents = SimpleDirectoryReader(directory_path).load_data()
    #Model usage
    index= GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    index.save_to_disk('index.json') # this will have the trained knowledge
    return index

def ask_bot(input_index='index.json'):
    index = GPTSimpleVectorIndex.load_from_disk(input_index)
    while True:
        query=input('What do you want to ask the bot? \n')
        response = index.query(query,response_mode="compact")
        print('\n Bot says: \n\n'+ response.response + "\n\n\n")


#index=construct_index('/Users/SaiNitesh/Projects/openai-chatbot/content/meditation/');

ask_bot('index.json');
