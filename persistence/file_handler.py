"""
Author: Felgine Touko Lina
Course: CST8002 - Programming Language Research
Professor: Stanley Pieda
Due Date: 02-22-2026
Description: Persistence layer handling all file I/O operations.

This component is responsible for processing CSV input and ensuring
data persistence through the generation of distinct UUID filenames for each record.

References:
[1] Parks Canada, “Black Oystercatcher Population – Pacific Rim,” open.canada.ca, Oct. 01,
2017. [Online]. Available: https://open.canada.ca/data/en/dataset/d87383f6-5313-430d-8416-
1b6d6e377e02. [Accessed: Dec. 23, 2025].

[2] Python Software Foundation, “csv — CSV File Reading and Writing,” docs.python.org, 2026.
[Online]. Available: https://docs.python.org/3/library/csv.html. [Accessed: Jan. 30, 2026].

[3] Python Software Foundation, “uuid — UUID objects,” docs.python.org, 2026. [Online].
Available: https://docs.python.org/3/library/uuid.html. [Accessed: Feb. 01, 2026].
"""

import csv
import uuid
from model.oystercatcher_record import OystercatcherRecord


class FileHandler:
    """
    Manages the bidirectional flow of data between the application and external storage,
    ensuring consistent file handling and error management.

    Responsible for managing CSV data persistence, this component handles both
    the parsing of input records and the generation of uniquely named UUID files for storage.
    """

    def __init__(self, filename):
        """
        Initialize FileHandler with a dataset filename.

        Args:
            filename (str): Path to the CSV data file
        """
        self.filename = filename

    def load_records(self, num_records=100):
        """
        Load records from CSV file into OystercatcherRecord objects.

        Args:
            num_records (int): Maximum number of records to load (default 100)

        Returns:
            tuple: (success: bool, records: list or error_message: str)
        """
        records = []

        try:
            with open(self.filename, 'r', encoding='latin-1') as file:
                csv_reader = csv.reader(file)

                # Skip English headers
                next(csv_reader)
                # Skip French headers
                next(csv_reader)

                count = 0
                for row in csv_reader:
                    if count >= num_records:
                        break

                    if len(row) >= 4:  # Ensure row has all required fields
                        record = OystercatcherRecord(
                            visit_date=row[0],
                            site_identification=row[1],
                            species=row[2],
                            total_black_oystercatcher_adults=row[3]
                        )
                        records.append(record)
                        count += 1

            return True, records

        except FileNotFoundError:
            return False, f"Error: File '{self.filename}' not found."
        except Exception as e:
            return False, f"Error loading file: {str(e)}"

    def save_records(self, records):

        try:
            # Generate unique filename using UUID
            unique_id = uuid.uuid4()
            output_filename = f"oystercatcher_data_{unique_id}.csv"

            with open(output_filename, 'w', newline='', encoding='utf-8') as file:
                csv_writer = csv.writer(file)

                # Write headers
                csv_writer.writerow([
                    'Visit date',
                    'Site identification',
                    'Species',
                    'Total Black oystercatcher adults'
                ])

                # Write all records
                for record in records:
                    csv_writer.writerow([
                        record.get_visit_date(),
                        record.get_site_identification(),
                        record.get_species(),
                        record.get_total_black_oystercatcher_adults()
                    ])

            return True, output_filename

        except Exception as e:
            return False, f"Error saving file: {str(e)}"