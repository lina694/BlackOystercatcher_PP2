"""
Author: Felgine Touko Lina
Course: CST8002 - Programming Language Research
Professor: Stanley Pieda
Due Date: 03-29-2026

This module handles all user interaction including menu display, input collection,
and output formatting. NO business logic or file I/O is performed here.

References:
[1] Parks Canada, “Black Oystercatcher Population – Pacific Rim,”open.canada.ca,
Oct. 01, 2017. [Online].Available: https://open.canada.ca/data/en/dataset/d87383f6-
5313-430d-8416-1b6d6e377e02. [Accessed: Dec. 23, 2025].
"""


class Menu:
    """
    Handles all user interface operations for the application.

    This class is responsible for displaying menus, collecting user input,
    and formatting output. It coordinates with the business layer for operations.
    """

    def __init__(self, data_manager, student_name):
        """
        Initialize Menu with a data manager and student name.

        Args:
            data_manager (DataManager): Business layer object
            student_name (str): Full name of the student
        """
        self.data_manager = data_manager
        self.student_name = student_name

    def display_header(self):
        """Display program header with student name."""
        print("\n" + "=" * 80)
        print(f"Black Oystercatcher Data Management System - by {self.student_name}")
        print("=" * 80)

    def display_menu(self):
        """Display main menu options."""
        print("\n" + "-" * 80)
        print(f"Main Menu - Program by {self.student_name}")
        print("-" * 80)
        print("1. Display all records")
        print("2. Display single record")
        print("3. Create new record")
        print("4. Edit existing record")
        print("5. Delete record")
        print("6. Reload data from file")
        print("7. Save data to file (UUID filename)")
        print("8. Exit")
        print("-" * 80)

    def get_menu_choice(self):
        """
        Get and validate menu choice from user.

        Returns:
            str: User's menu choice
        """
        choice = input(f"\n{self.student_name}, enter your choice (1-8): ").strip()
        return choice

    def display_all_records(self):
        """Display all records from the data manager."""
        records = self.data_manager.get_all_records()

        if not records:
            print("\nNo records to display.")
            return

        print("\n" + "=" * 80)
        print(f"All Black Oystercatcher Records - Program by {self.student_name}")
        print("=" * 80)

        for index, record in enumerate(records):
            print(f"\n[Record {index}]  {record}")

            # Display student name every 10 records
            if (index + 1) % 10 == 0:
                print(f"\n--- Program by {self.student_name} ---")

        print("\n" + "=" * 80)
        print(f"Total: {len(records)} records - Program by {self.student_name}")
        print("=" * 80)

    def display_single_record(self):
        """Display a single record selected by user."""
        try:
            total = self.data_manager.get_record_count()
            print(f"\nTotal records available: {total}")

            index = int(input(f"Enter record index (0 to {total - 1}): "))

            success, result = self.data_manager.get_record_by_index(index)

            if success:
                print("\n" + "-" * 80)
                print(f"Record {index} - Program by {self.student_name}")
                print("-" * 80)
                print(result)
                print("-" * 80)
            else:
                print(f"\nError: {result}")

        except ValueError:
            print("\nError: Please enter a valid number.")
        except Exception as e:
            print(f"\nError: {str(e)}")

    def create_new_record(self):
        """Create a new record with user input."""
        print("\n" + "-" * 80)
        print(f"Create New Record - Program by {self.student_name}")
        print("-" * 80)

        try:
            visit_date = input("Enter visit date (DD/MM/YYYY): ").strip()
            site_id = input("Enter site identification: ").strip()
            species = input("Enter species name: ").strip()
            adult_count = input("Enter adult count: ").strip()

            if not all([visit_date, site_id, species, adult_count]):
                print("\nError: All fields are required.")
                return

            success, message = self.data_manager.create_record(
                visit_date, site_id, species, adult_count
            )

            print(f"\n{message}")

        except Exception as e:
            print(f"\nError creating record: {str(e)}")

    def edit_record(self):
        """Edit an existing record."""
        try:
            total = self.data_manager.get_record_count()
            print(f"\nTotal records: {total}")

            index = int(input(f"Enter record index to edit (0 to {total - 1}): "))

            # Show current record
            success, current_record = self.data_manager.get_record_by_index(index)

            if not success:
                print(f"\nError: {current_record}")
                return

            print(f"\nCurrent record: {current_record}")
            print("\nEnter new values (press Enter to keep current value):")

            # Get new values
            visit_date = input(f"Visit date [{current_record.get_visit_date()}]: ").strip()
            site_id = input(f"Site ID [{current_record.get_site_identification()}]: ").strip()
            species = input(f"Species [{current_record.get_species()}]: ").strip()
            adult_count = input(f"Adult count [{current_record.get_total_black_oystercatcher_adults()}]: ").strip()

            # Use current values if no new value entered
            visit_date = visit_date if visit_date else current_record.get_visit_date()
            site_id = site_id if site_id else current_record.get_site_identification()
            species = species if species else current_record.get_species()
            adult_count = adult_count if adult_count else current_record.get_total_black_oystercatcher_adults()

            success, message = self.data_manager.update_record(
                index, visit_date, site_id, species, adult_count
            )

            print(f"\n{message}")

        except ValueError:
            print("\nError: Please enter a valid number.")
        except Exception as e:
            print(f"\nError: {str(e)}")

    def delete_record(self):
        """Delete a record."""
        try:
            total = self.data_manager.get_record_count()
            print(f"\nTotal records: {total}")

            index = int(input(f"Enter record index to delete (0 to {total - 1}): "))

            # Show record to be deleted
            success, record = self.data_manager.get_record_by_index(index)

            if not success:
                print(f"\nError: {record}")
                return

            print(f"\nRecord to delete: {record}")
            confirm = input("Are you sure you want to delete this record? (yes/no): ").strip().lower()

            if confirm == 'yes':
                success, message = self.data_manager.delete_record(index)
                print(f"\n{message}")
            else:
                print("\nDeletion cancelled.")

        except ValueError:
            print("\nError: Please enter a valid number.")
        except Exception as e:
            print(f"\nError: {str(e)}")

    def reload_data(self):
        """Reload data from the original CSV file."""
        print("\n" + "-" * 80)
        print("Reloading data from file...")
        print("-" * 80)

        success, message = self.data_manager.load_data(num_records=100)
        print(f"\n{message}")

    def save_data(self):
        """Save current data to a new file with UUID filename."""
        print("\n" + "-" * 80)
        print(f"Saving data - Program by {self.student_name}")
        print("-" * 80)

        success, message = self.data_manager.save_data()
        print(f"\n{message}")

    def run(self):
        """
        Main menu loop for the application.

        Coordinates all user interactions and delegates operations
        to the appropriate methods.
        """
        # Initial data load
        self.display_header()
        print("\nLoading initial data...")
        success, message = self.data_manager.load_data(num_records=100)
        print(message)

        # Main loop
        while True:
            self.display_menu()
            choice = self.get_menu_choice()

            if choice == '1':
                self.display_all_records()
            elif choice == '2':
                self.display_single_record()
            elif choice == '3':
                self.create_new_record()
            elif choice == '4':
                self.edit_record()
            elif choice == '5':
                self.delete_record()
            elif choice == '6':
                self.reload_data()
            elif choice == '7':
                self.save_data()
            elif choice == '8':
                print(f"\nThank you for using the Black Oystercatcher Data Management System!")
                print(f"Program by {self.student_name}")
                print("\nGoodbye!\n")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1 and 8.")

            # Pause before showing menu again
            input("\nPress Enter to continue...")