import os
from datetime import datetime


def create_customer_folder(customer_name, dob):
    # Format the customer folder name using name and date of birth
    formatted_dob = datetime.strptime(dob, "%Y-%m-%d").strftime('%Y%m%d')
    folder_name = f"{customer_name}_{formatted_dob}_{datetime.now().strftime('%H%M%S')}"

    # Create the customer folder within the document_folder
    folder_path = os.path.join("document_storage", folder_name)
    os.makedirs(folder_path)

    return folder_path


def save_document(folder_path, document_type, file):
    # Save the document within the document_storage with the provided document type
    document_path = os.path.join(folder_path, f"{document_type.replace(' ', '_')}.pdf")

    with open(document_path, "wb") as f:
        f.write(file.read())
