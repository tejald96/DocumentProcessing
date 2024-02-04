def verify_kyc(name, dob, document_type, document_number):
    """
    Verify KYC information with an external service.

    Parameters:
    - name (str): Full name of the individual.
    - dob (str): Date of birth of the individual.
    - document_type (str): Type of the document (e.g., "PAN Card", "Driving License").
    - document_number (str): Document number for verification.

    """
    # In this example, verification is successful if the document number is even
    is_verification_successful = int(document_number[-1]) % 2 == 0

    return is_verification_successful
