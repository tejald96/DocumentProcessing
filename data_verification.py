# data_verification.py

def verify_pan_card_data(pan_data):
    # Check if PAN number follows a valid pattern 
    pan_number = pan_data.get("pan_number")

    if pan_number and len(pan_number) == 10:
        return True
    else:
        return False


def verify_driving_license_data(dl_data):
    # Check if Driving License number and date of birth are present
    dl_number = dl_data.get("dl_number")
    date_of_birth = dl_data.get("date_of_birth")

    if dl_number and date_of_birth:
        return True
    else:
        return False


def verify_data(pan_data, dl_data):
    # Verify PAN Card data
    pan_verification = verify_pan_card_data(pan_data)

    # Verify Driving License data
    dl_verification = verify_driving_license_data(dl_data)

    # Return verification results for both documents
    return {"pan_verification": pan_verification, "dl_verification": dl_verification}
