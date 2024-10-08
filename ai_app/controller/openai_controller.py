from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import logging
from service.document_search_service import document_search

# Create an instance of APIRouter
router = APIRouter()

@router.post("/document_search")
def chat_completion(file: UploadFile = File(None), url: str = Form(None), question: str = Form(...)):
    """
    Endpoint to handle document search requests.

    Args:
        file (UploadFile): The file to be read and searched.
        question (str): The question to query against the document content.

    Returns:
        dict: A dictionary containing the response from the document search service.

    Raises:
        HTTPException: If there is an error processing the file.
    """
    try:
        # Call the document search service with the provided file and question
        response = document_search(file=file, url=url, question=question)
        return {"response": response}
    except Exception as e:
        # Log the error and raise an HTTPException
        logging.error(f"Error processing file: {e}")
        raise HTTPException(status_code=500, detail=str(e))