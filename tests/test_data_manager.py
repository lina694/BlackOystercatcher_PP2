"""
Author: Felgine Touko Lina
Course: CST8002 - Programming Language Research
Professor: Stanley Pieda
Due Date: 03-29-2026
Description: Unit tests for DataManager business layer.
             Carried forward from Practical Project Part 2 to verify
             no regression was introduced when adding the GUI layer.

References:
[1] pytest development team. (2026). "pytest: helps you write better programs."
    pytest.org. [Online]. Available: https://docs.pytest.org/en/stable/
    [Accessed: Feb 1, 2026]
"""

from business.data_manager import DataManager


def test_create_record_adds_to_collection():
    """
    Test that create_record() successfully adds a new record to the collection.

    Uses Arrange-Act-Assert pattern.
    """
    # Arrange
    data_manager = DataManager("black_oystercatcher_data.csv")
    initial_count = data_manager.get_record_count()

    test_date    = "01/02/2026"
    test_site    = "99"
    test_species = "Haematopus bachmani"
    test_count   = "42"

    # Act
    success, message = data_manager.create_record(
        test_date, test_site, test_species, test_count
    )

    # Assert
    assert success is True
    assert data_manager.get_record_count() == initial_count + 1

    new_ok, new_record = data_manager.get_record_by_index(initial_count)
    assert new_ok is True
    assert new_record.get_visit_date() == test_date
    assert new_record.get_site_identification() == test_site
    assert new_record.get_species() == test_species
    assert new_record.get_total_black_oystercatcher_adults() == test_count

    print(f"\n✓ Test PASSED: Record created. "
          f"Count: {initial_count} -> {data_manager.get_record_count()}")


def test_delete_record_removes_from_collection():
    """
    Test that delete_record() successfully removes a record by index.
    """
    # Arrange
    data_manager = DataManager("black_oystercatcher_data.csv")
    data_manager.create_record("01/01/2026", "10", "Haematopus bachmani", "5")
    count_before = data_manager.get_record_count()

    # Act
    success, message = data_manager.delete_record(0)

    # Assert
    assert success is True
    assert data_manager.get_record_count() == count_before - 1
    print(f"\n✓ Test PASSED: Record deleted. "
          f"Count: {count_before} -> {data_manager.get_record_count()}")


def test_update_record_changes_values():
    """
    Test that update_record() correctly modifies an existing record's fields.
    """
    # Arrange
    data_manager = DataManager("black_oystercatcher_data.csv")
    data_manager.create_record("01/01/2026", "10", "Haematopus bachmani", "5")
    index = data_manager.get_record_count() - 1

    # Act
    success, message = data_manager.update_record(
        index, "15/03/2026", "55", "Haematopus bachmani", "99"
    )

    # Assert
    assert success is True
    _, updated = data_manager.get_record_by_index(index)
    assert updated.get_visit_date() == "15/03/2026"
    assert updated.get_site_identification() == "55"
    assert updated.get_total_black_oystercatcher_adults() == "99"
    print(f"\n✓ Test PASSED: Record updated correctly.")


def test_zzz_display_completion():
    """Display completion message with student name."""
    print("\n" + "=" * 60)
    print("Unit Testing Complete - Felgine Touko Lina")
    print("=" * 60)
    assert True
