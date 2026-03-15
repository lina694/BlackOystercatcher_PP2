"""
Author: Felgine Touko Lina
Course: CST8002 - Programming Language Research
Professor: Stanley Pieda
Due Date: 03-29-2026
Description: Record object class for Black Oystercatcher population data.

This class represents a single record from the Parks Canada Black Oystercatcher
dataset with fields matching the CSV column names.

References:
[1] Parks Canada, “Black Oystercatcher Population – Pacific Rim,” open.canada.ca, Oct. 01,
2017. [Online]. Available: https://open.canada.ca/data/en/dataset/d87383f6-5313-430d-8416-
1b6d6e377e02. [Accessed: Dec. 23, 2025].

[2] Python Software Foundation, “Classes,” Python.org, 2026. [Online].
Available: https://docs.python.org/3/tutorial/classes.html. [Accessed: Jan. 30, 2026].
"""


class OystercatcherRecord:
    """
    Captures a specific instance of a Black Oystercatcher population observation from the dataset.

    Attributes:
        visit_date (str): Date of observation (DD/MM/YYYY)
        site_identification (str): Site ID number
        species (str): Scientific species name (Haematopus bachmani)
        total_black_oystercatcher_adults (str): Count of adult birds
    """

    def __init__(self, visit_date, site_identification, species,
                 total_black_oystercatcher_adults):
        """
        Initialize a new OystercatcherRecord object.

        Args:
            visit_date (str): Date of observation
            site_identification (str): Site ID
            species (str): Species name
            total_black_oystercatcher_adults (str): Adult count
        """
        self.visit_date = visit_date
        self.site_identification = site_identification
        self.species = species
        self.total_black_oystercatcher_adults = total_black_oystercatcher_adults

    def get_visit_date(self):
        """Get the visit date."""
        return self.visit_date

    def set_visit_date(self, visit_date):
        """Set the visit date."""
        self.visit_date = visit_date

    def get_site_identification(self):
        """Get the site identification."""
        return self.site_identification

    def set_site_identification(self, site_identification):
        """Set the site identification."""
        self.site_identification = site_identification

    def get_species(self):
        """Get the species name."""
        return self.species

    def set_species(self, species):
        """Set the species name."""
        self.species = species

    def get_total_black_oystercatcher_adults(self):
        """Get the adult count."""
        return self.total_black_oystercatcher_adults

    def set_total_black_oystercatcher_adults(self, count):
        """Set the adult count."""
        self.total_black_oystercatcher_adults = count

    def __str__(self):
        """
        Return string representation of the record.

        Returns:
            str: Formatted record display
        """
        return (f"Date: {self.visit_date}, Site: {self.site_identification}, "
                f"Species: {self.species}, Adults: {self.total_black_oystercatcher_adults}")

    def to_csv_row(self):
        """
        Convert record to CSV row format.

        Returns:
            str: Comma-separated values
        """
        return f"{self.visit_date},{self.site_identification},{self.species},{self.total_black_oystercatcher_adults}"