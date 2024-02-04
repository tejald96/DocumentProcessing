import re


def extract_pan_card_data(text):
    pan_pattern = re.compile(r'\b([A-Z]{5}[0-9]{4}[A-Z])\b')
    pan_match = pan_pattern.search(text)

    if pan_match:
        pan_number = pan_match.group(1)
        return {"pan_number": pan_number}
    else:
        return None


def extract_driving_license_data(text):
    dl_number_pattern = re.compile(r'\b([A-Z]{2}[0-9]{13})\b')
    dob_pattern = re.compile(r'\b(\d{2}/\d{2}/\d{4})\b')

    dl_number_match = dl_number_pattern.search(text)
    dob_match = dob_pattern.search(text)

    if dl_number_match and dob_match:
        dl_number = dl_number_match.group(1)
        date_of_birth = dob_match.group(1)
        return {"dl_number": dl_number, "date_of_birth": date_of_birth}
    else:
        return None
