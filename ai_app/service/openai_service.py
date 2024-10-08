from openai import AzureOpenAI
from typing import List
import httpx
import logging
from config.config import AZURE_API_KEY, AZURE_ENDPOINT, AZURE_API_VERSION, DEPLOYMENT_NAME


class OpenAIService:
    def __init__(self):
        """
        Initializes the OpenAIService with an HTTP client and Azure OpenAI client.
        """
        self.http_client = httpx.Client(verify=False)
        self.client = AzureOpenAI(
            api_key=AZURE_API_KEY,
            azure_endpoint=AZURE_ENDPOINT,
            api_version=AZURE_API_VERSION,
            http_client=self.http_client,
        )
        self.deployment_name = 'gpt-4'  # Use the appropriate deployment name

    def get_chat_completion(self, messages: List[dict]) -> str:
        """
        Sends a chat completion request to the Azure OpenAI service.

        Args:
            messages (List[dict]): A list of message dictionaries to be sent to the OpenAI service.

        Returns:
            str: The content of the response message from the OpenAI service.
        """
        logging.info('Sending a test completion job')
        response = self.client.chat.completions.create(
            model=self.deployment_name,
            messages=messages,
            max_tokens=1000
        )
        logging.info(response.choices[0].message.content)
        return response.choices[0].message.content