import csv
import os

# Set the file path for the CSV
csv_file_path = os.path.join("data", "kyc_data.csv")


def read_csv():
    """
    Read data from the KYC data CSV file.

    Returns:
    - list: List of dictionaries containing the data from the CSV file.
    """
    data = []

    if os.path.exists(csv_file_path):
        with open(csv_file_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)

    return data


def write_csv(fieldnames, data):
    """
    Write data to the KYC data CSV file.

    Parameters:
    - fieldnames (list): List of field names for the CSV.
    - data (list): List of dictionaries containing the data to be written.

    """
    try:
        with open(csv_file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header if the file is empty
            if os.path.getsize(csv_file_path) == 0:
                writer.writeheader()

            # Write data
            writer.writerows(data)

        return True
    except Exception as e:
        print(f"Error writing to CSV: {e}")
        return False
