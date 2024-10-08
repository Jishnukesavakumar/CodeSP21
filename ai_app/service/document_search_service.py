from service.openai_service import OpenAIService
from io import BytesIO
from utils.file_reader import read_file_content
from fastapi import UploadFile
import requests

def fetch_url_content(url: str) -> str:
    """
    Fetches the content from a given URL.

    Args:
        url (str): The URL to fetch content from.

    Returns:
        str: The content fetched from the URL.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.text

def document_search(file: UploadFile =  None, url: str = None, question: str = None) -> str:
    """
    Searches the content of a document for answers to a given question.

    Args:
        file (UploadFile): The file to be read and searched.
        question (str): The question to query against the document content.

    Returns:
        str: The response from the OpenAI service based on the document content and question.
    """
    if file:
        # Read the content of the file
        content = read_file_content(file=file)
    elif url:
        # Fetch the content from the URL
        content = fetch_url_content(url=url)
    else:
        raise ValueError("Either file or url must be provided")
    # Read the content of the file
    #content = read_file_content(file)

    # Prepare messages for OpenAI
    messages = [
        {"role": "system", "content": "You are an AI assistant created to help users query data from documents."},
        {"role": "user", "content": f"This is the document data: {content}"},
        {"role": "user", "content": question}
    ]

    # Initialize the OpenAI service
    openai_service = OpenAIService()

    # Get the chat completion response from OpenAI
    return openai_service.get_chat_completion(messages)
