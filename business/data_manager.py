"""
Author: Felgine Touko Lina
Course: CST8002 - Programming Language Research
Professor: Stanley Pieda
Due Date: 03-29-2026
Description: Business layer managing all CRUD operations and business logic.

This module maintains the in-memory data structure and provides methods for
creating, reading, updating, and deleting records.

References:
[1] Parks Canada, “Black Oystercatcher Population – Pacific Rim,”open.canada.ca,
Oct. 01, 2017. [Online].Available: https://open.canada.ca/data/en/dataset/d87383f6-
5313-430d-8416-1b6d6e377e02. [Accessed: Dec. 23, 2025].

[2] Python Software Foundation, “Data Structures,” docs.python.org, 2026. [Online].
Available: https://docs.python.org/3/tutorial/datastructures.html. [Accessed: Jan. 30, 2026].
"""

from model.oystercatcher_record import OystercatcherRecord
from persistence.file_handler import FileHandler


class DataManager:
    """
    Manages the in-memory collection of oystercatcher records.

    This class provides CRUD (Create, Read, Update, Delete) operations
    on the record collection and coordinates with the persistence layer.
    """

    def __init__(self, filename):
        """
        Initialize DataManager with a dataset filename.

        Args:
            filename (str): Path to the CSV data file
        """
        self.file_handler = FileHandler(filename)
        self.records = []  # In-memory data structure

    def load_data(self, num_records=100):
        """
        Load data from file into memory.

        Args:
            num_records (int): Number of records to load

        Returns:
            tuple: (success: bool, message: str)
        """
        success, result = self.file_handler.load_records(num_records)

        if success:
            self.records = result
            return True, f"Successfully loaded {len(self.records)} records."
        else:
            return False, result

    def save_data(self):
        """
        Save current data to file with UUID filename.

        Returns:
            tuple: (success: bool, message: str)
        """
        if not self.records:
            return False, "No data to save."

        success, result = self.file_handler.save_records(self.records)

        if success:
            return True, f"Data saved successfully to: {result}"
        else:
            return False, result

    def get_all_records(self):
        """
        Get all records from memory.

        Returns:
            list: All OystercatcherRecord objects
        """
        return self.records

    def get_record_by_index(self, index):
        """
        Get a single record by its index.

        Args:
            index (int): Zero-based index of the record

        Returns:
            tuple: (success: bool, record or error_message)
        """
        if 0 <= index < len(self.records):
            return True, self.records[index]
        else:
            return False, "Invalid record index."

    def get_record_count(self):
        """
        Get the total number of records.

        Returns:
            int: Number of records in memory
        """
        return len(self.records)

    def create_record(self, visit_date, site_id, species, adult_count):
        """
        Create a new record and add it to the collection.

        Args:
            visit_date (str): Visit date
            site_id (str): Site identification
            species (str): Species name
            adult_count (str): Adult bird count

        Returns:
            tuple: (success: bool, message: str)
        """
        try:
            new_record = OystercatcherRecord(
                visit_date, site_id, species, adult_count
            )
            self.records.append(new_record)
            return True, "Record created successfully."
        except Exception as e:
            return False, f"Error creating record: {str(e)}"

    def update_record(self, index, visit_date, site_id, species, adult_count):
        """
        Update an existing record.

        Args:
            index (int): Index of record to update
            visit_date (str): New visit date
            site_id (str): New site identification
            species (str): New species name
            adult_count (str): New adult count

        Returns:
            tuple: (success: bool, message: str)
        """
        if 0 <= index < len(self.records):
            try:
                self.records[index].set_visit_date(visit_date)
                self.records[index].set_site_identification(site_id)
                self.records[index].set_species(species)
                self.records[index].set_total_black_oystercatcher_adults(adult_count)
                return True, "Record updated successfully."
            except Exception as e:
                return False, f"Error updating record: {str(e)}"
        else:
            return False, "Invalid record index."

    def delete_record(self, index):
        """
        Delete a record from the collection.

        Args:
            index (int): Index of record to delete

        Returns:
            tuple: (success: bool, message: str)
        """
        if 0 <= index < len(self.records):
            try:
                deleted_record = self.records.pop(index)
                return True, f"Record deleted: {deleted_record}"
            except Exception as e:
                return False, f"Error deleting record: {str(e)}"
        else:
            return False, "Invalid record index."