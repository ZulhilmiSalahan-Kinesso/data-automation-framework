import pytest


def verify_row_data_not_empty(row_data):
    total_row = row_data.__len__()
    assert total_row > 0, f'No Testing Data'


def verify_row_count_is_zero(row_data):
    row_count = row_data.__len__()
    assert row_count == 0, f"Actual: {row_count} -> Data should be empty"


def skip_test(params):
    if params.__len__() == 2:
        pytest.skip()
