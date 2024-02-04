from flask import Flask, render_template, request, flash
# Import your custom modules
from services import document_validation, document_storage, ocr_processing, data_extraction, data_verification, \
    kyc_service_integration, notification_system

app = Flask(__name__, template_folder='app/templates')


@app.route('/')
def upload_page():
    return render_template('upload.html')


@app.route('/process_kyc', methods=['POST'])
def process_kyc():
    # Handle file uploads and form data
    proof_identity = request.files['file-identity']
    proof_address = request.files['file-address']
    name = request.form['name']
    dob = request.form['dob']
    email = request.form['email']

    # Validate documents
    if document_validation.validate_document_type(proof_identity, proof_address):
        # Create a folder for the customer
        customer_folder = document_storage.create_customer_folder(name, dob)

        # Save documents
        document_storage.save_document(customer_folder, 'proof_identity', proof_identity)
        document_storage.save_document(customer_folder, 'proof_address', proof_address)

        return render_template('processing.html')
    else:
        flash('Document validation failed. Please check your documents.')

        # OCR Processing
        extracted_data = ocr_processing.perform_ocr(proof_identity)

        # Data Extraction
        processed_data = data_extraction.extract_pan_card_data(extracted_data)

        # Data Verification
        verification_result = data_verification.verify_data(processed_data)

        # KYC Service Integration
        kyc_service_integration.verify_kyc(verification_result)

        # Notification System
        notification_system.send_notification(email, verification_result)


if __name__ == '__main__':
    app.run(debug=True)
