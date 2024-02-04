from PIL import Image
import pytesseract


def perform_ocr(file_path):
    
    try:
        # Use pytesseract to perform OCR on the image
        image = Image.open(file_path)
        text_content = pytesseract.image_to_string(image)
        return text_content
    except Exception as e:
        # Handle OCR processing failure
        print(f"OCR processing failed: {e}")
        return ""


