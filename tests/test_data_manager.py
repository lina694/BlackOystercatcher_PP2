"""
Author: Felgine Touko Lina
Course: CST8002 - Programming Language Research
Professor: Stanley Pieda
Due Date: 02-22-2026
Description: Unit tests for DataManager business layer.

This test file demonstrates unit testing of the create_record functionality
to verify that new records are properly added to the data structure.

References:
[1] Pytest Development Team, “pytest: helps you write better programs,” pytest.org, 2026. [Online].
Available: https://docs.pytest.org/en/stable/. [Accessed: Feb. 01, 2026].

[2] E. Daedtech, “You Still Don’t Know How to Do Unit Testing,” Stackify.com, May 02, 2023. [Online].
Available: https://stackify.com/unit-testing-basics-best-practices/. [Accessed: Feb. 01, 2026].
"""

from business.data_manager import DataManager


def test_create_record_adds_to_collection():
    """
    Test that create_record() successfully adds a new record to the collection.

    This test verifies the Create operation of CRUD functionality by:
    1. Creating a DataManager instance
    2. Creating a new record with test data
    3. Verifying the record count increased by 1
    4. Verifying the new record contains the correct data

    Uses Arrange-Act-Assert pattern for clear test structure.
    """
    # Arrange - Set up test data and objects
    data_manager = DataManager("black_oystercatcher_data.csv")
    initial_count = data_manager.get_record_count()

    test_date = "01/02/2026"
    test_site = "99"
    test_species = "Haematopus bachmani"
    test_count = "42"

    # Act - Perform the operation being tested
    success, message = data_manager.create_record(
        test_date, test_site, test_species, test_count
    )

    # Assert - Verify the results
    assert success == True, "create_record should return success=True"
    assert data_manager.get_record_count() == initial_count + 1, \
        "Record count should increase by 1"

    # Verify the new record contains correct data
    new_record_success, new_record = data_manager.get_record_by_index(initial_count)
    assert new_record_success == True, "Should be able to retrieve new record"
    assert new_record.get_visit_date() == test_date, "Visit date should match"
    assert new_record.get_site_identification() == test_site, "Site ID should match"
    assert new_record.get_species() == test_species, "Species should match"
    assert new_record.get_total_black_oystercatcher_adults() == test_count, \
        "Adult count should match"

    print(f"\n✓ Test PASSED: Record successfully created and added to collection")
    print(f"  Initial count: {initial_count}, Final count: {data_manager.get_record_count()}")
    print(f"  New record: {new_record}")


# Display student name when tests complete
def test_zzz_display_completion():
    """Display completion message with student name."""
    print("\n" + "=" * 70)
    print("Unit Testing Complete - Felgine Touko Lina")
    print("=" * 70)
    assert True