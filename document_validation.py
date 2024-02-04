# document_validation_old.py
import cv2
import pytesseract
import logging


def validate_document_type(file_path, document_type):
    """
    Validate the document type based on the file content or format.

    Parameters:
    - file_path (str): Path to the uploaded document.
    - document_type (str): Expected document type (e.g., "PAN card", "Driving Licence").

    """
    try:
        # Use OCR to extract text from the document
        extracted_text = extract_text_from_image(file_path)

        # Placeholder logic, replace with actual validation
        return document_type.lower() in extracted_text.lower()
    except Exception as e:
        # Handle validation failure
        print(f"Document type validation failed: {e}")
        return False

    # Log the detected document type
    logging.info(f"Detected document type: {document_type}")
    return document_type


def check_completeness(file_path):

    try:
        # Use OCR to extract text from the document
        extracted_text = extract_text_from_image(file_path)

        # Placeholder logic, replace with actual completeness checks
        # For example, check if specific fields are present in the extracted text
        required_fields = ["name", "date of birth", "address"]
        return all(field in extracted_text.lower() for field in required_fields)
    except Exception as e:
        # Handle completeness check failure
        print(f"Completeness check failed: {e}")
        return False

    # Log completeness status
    logging.info(f"Document completeness: {is_complete}")
    return is_complete


def extract_text_from_image(file_path):
    """
    Extract text from an image using OCR.

    """
    try:
        # Use pytesseract for OCR text extraction
        image = cv2.imread(file_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray_image)
        return text
    except Exception as e:
        # Handle OCR extraction failure
        print(f"OCR extraction failed: {e}")
        return ""

