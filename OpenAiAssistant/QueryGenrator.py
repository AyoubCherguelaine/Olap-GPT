"""
This script demonstrates the use of the OpenAI GPT-3 model to extract information from documents, specifically invoices.
The script uses the OpenAIAssistant class to interact with the GPT-3 API and the DocumentsExtractor class to define queries and extract information from the document content.

Requirements:
- openai (OpenAI Python library)
- tiktoken (Library to count tokens in text)
"""

import requests
import os
import openai
import tiktoken
import json

import pandas as pd

from . import config

# OpenAI API key
openai.api_key = config.key

def set_number_of_token(content):
    """
    Returns the number of tokens in the given text.

    Parameters:
    - content (str): The input text.

    Returns:
    - int: The number of tokens in the text.
    """
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(content))

class chat:
    
    def __init__(self):
        dic= {"role":[],"message":[]}
        self.message = pd.DataFrame(dic)
    
    def append(self, role, message):
        new_row = {"role": role, "message": message}
        self.messages = self.messages.append(new_row, ignore_index=True)

    def convert_to_messages(df):
        messages = []
        for _, row in df.iterrows():
            message = {
                "role": row["role"],
                "content": row["message"]
            }
            messages.append(message)
        return messages

    def token_number(self):
        num_token = 0
        for _, row in df.iterrows():
            
            num_token += set_number_of_token(row["message"])
        return num_token  

    def delete_FI(self):
        if len(self.messages) > 0:
            self.messages = self.messages.iloc[1:]
        

class OpenAIAssistant:
    """
    A class representing the OpenAI Assistant.

    This class provides methods to interact with the GPT-3 model for chat-based completion.

    Attributes:
    - api_key (str): The OpenAI API key.
    """

    @classmethod
    def chat_response(cls, system_message, user_message):
        """
        Generates a chat-based response using the OpenAI GPT-3 model.

        Parameters:
        - system_message (str): The system message.
        - user_message (str): The user message.

        Returns:
        - dict: The response from the GPT-3 model.
        """
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]
        model_name = "gpt-3.5-turbo-16k-0613"

        

        response = openai.ChatCompletion.create(
                                                model=model_name,
                                                messages=messages,
                                                temperature=0
                                                )

        return response

    @classmethod
    def longChat(user_message,chat_obj):
        


class DBAnalyzer:

    @staticmethod
    def __convert_response(response):
        pass
    
    @staticmethod
    def AnalyseTables(db_Respresentation:list):
        System_message ="""From this DB Tables representation 
Describtion or Explaine for each table
Response like : {'describe':[{'table1':"description"},{'table1':"description"},...]}
"""
        str_representation = "\n\n".join(db_Respresentation)
        str_representation = '"'+str_representation+'"'
        user_message = f"""Describtion or Explaine for each table:
{str_representation}"""

        print(user_message)
        system_token = set_number_of_token(System_message)
        user_token = set_number_of_token(user_message)
        max_input_token  = system_token + user_token
        print(max_input_token)

        # send request to open ai api 

        return OpenAIAssistant.chat_response(System_message,user_message)

    @staticmethod
    def defineCubes(db_Respresentation,structure_response):
        str_representation = "\n\n".join(db_Respresentation)
      
        Old_user_message = """From this DB Tables representation 
Describe table by table ignoring columns
Response like : {'describe':[{'table1':'description'},{'table1':'description'},...]} :
"""
        Old_user_message += f'"{str_representation})"'
        system_message = """Process the table and Extract some OLAP Cubes for analyse
        """

        user_message ="""From the DB Tables representation and Table Describtion
Propose all OLAP Cubes can get from this 
respect this forma : {'cubes':[{'cube1':'describe'},{'cube2':'describe'}....]}
"""     
        print(user_message)
        
        Old_user_message_token = set_number_of_token(Old_user_message)
        Old_response = set_number_of_token(structure_response)
        system_token = set_number_of_token(system_message)
        user_token = set_number_of_token(user_message)
        print(system_token,user_token,Old_user_message_token,Old_response)
        max_input_token  = system_token + user_token + Old_response +Old_user_message_token
        print(max_input_token)


        # senf request to open ai api

    @staticmethod
    def define_cube_query(describe:str):
        pass
    
class CubeAnalyser:

    def __init__(self):
        pass


    @staticmethod
    def process_query(describe ,query):
        pass