import pandas as pd
from PyPDF2 import PdfReader
from fastapi import UploadFile
from io import BytesIO
import requests
from bs4 import BeautifulSoup

def read_file_content(file: UploadFile = None, url: str = None) -> str:
    """
    Reads the content of a file or URL based on its content type.

    Args:
        file (UploadFile, optional): The file to be read.
        url (str, optional): The URL to fetch content from.

    Returns:
        str: The content of the file or URL as a string.

    Raises:
        ValueError: If the file type or URL content type is unsupported.
    """
    if file:
        content_type = file.content_type
        content = file.file.read()
    elif url:
        response = requests.get(url)
        response.raise_for_status()
        content_type = response.headers.get('Content-Type', '')
        content = response.content
    else:
        raise ValueError("Either file or url must be provided")

    if "application/pdf" in content_type:
        return read_pdf_content(BytesIO(content))
    elif "text/csv" in content_type or "application/vnd.ms-excel" in content_type or \
         "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" in content_type:
        return read_csv_or_excel_content(BytesIO(content))
    elif "text/plain" in content_type:
        return read_txt_content(BytesIO(content))
    elif "text/html" in content_type:
        return read_html_content(content)
    else:
        raise ValueError("Unsupported content type")

def read_pdf_content(file: BytesIO) -> str:
    """
    Reads the content of a PDF file.

    Args:
        file (BytesIO): The PDF file to be read.

    Returns:
        str: The content of the PDF file as a string.
    """
    
    # Implement PDF reading logic here
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def read_csv_or_excel_content(file: BytesIO) -> str:
    """
    Reads the content of a CSV or Excel file.

    Args:
        file (BytesIO): The CSV or Excel file to be read.

    Returns:
        str: The content of the CSV or Excel file as a string.
    """
    # Implement CSV or Excel reading logic here
    df = pd.read_csv(file) if "csv" in file.name else pd.read_excel(file)
    return df.to_string()

def read_txt_content(file: BytesIO) -> str:
    """
    Reads the content of a text file.

    Args:
        file (BytesIO): The text file to be read.

    Returns:
        str: The content of the text file as a string.
    """
    # Implement text file reading logic here
    return file.read().decode('utf-8')

def read_html_content(content: bytes) -> str:
    """
    Reads the content of an HTML page.

    Args:
        content (bytes): The HTML content to be read.

    Returns:
        str: The content of the HTML page as a string.
    """
    soup = BeautifulSoup(content, 'html.parser')
    return soup.get_text()