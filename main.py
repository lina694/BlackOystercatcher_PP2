"""
Author: Felgine Touko Lina
Course: CST8002 - Programming Language Research
Professor: Stanley Pieda
Due Date: 02-22-2026
Description: Main entry point for Black Oystercatcher Data Management System.

This program implements a layered design pattern to organize the processing of Parks Canada ecological data.
By isolating presentation from data handling, the software ensures scalable
Create, Read, Update, and Delete (CRUD) functionality for population observations.

References:
[1] Parks Canada. (Oct 1, 2017). "Black Oystercatcher Population – Pacific Rim."
    open.canada.ca. [Online]. Available at:
    https://open.canada.ca/data/en/dataset/d87383f6-5313-430d-8416-1b6d6e377e02
    [Accessed: Dec 23, 2025]
[2] Government of Canada. (n.d.). "Open Government License - Canada."
    open.canada.ca. [Online]. Available at:
    https://open.canada.ca/en/open-government-licence-canada
    [Accessed: Feb 1, 2026]
"""

from business.data_manager import DataManager
from presentation.menu import Menu

# Constants
STUDENT_NAME = "Felgine Touko Lina"
CSV_FILENAME = "black_oystercatcher_data.csv"


def main():
    """
    Main function to start the Black Oystercatcher Data Management System.

    Initializes the business layer (DataManager) and presentation layer (Menu),
    then starts the interactive menu system.
    """
    print("=" * 80)
    print("Black Oystercatcher Data Management System")
    print(f"Created by {STUDENT_NAME}")
    print("=" * 80)
    print("\nData Source: Parks Canada Open Data Portal")
    print("Dataset: Black Oystercatcher Population – Pacific Rim")
    print("License: Open Government License - Canada")
    print("Species: Haematopus bachmani")
    print("=" * 80)

    # Initialize business layer
    data_manager = DataManager(CSV_FILENAME)

    # Initialize presentation layer
    menu = Menu(data_manager, STUDENT_NAME)

    # Start the application
    menu.run()


if __name__ == "__main__":
    main()