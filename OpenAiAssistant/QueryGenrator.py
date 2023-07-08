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

# OpenAI API key
key = "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"
openai.api_key = key

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


