def row_count_is_zero(row_data):
    row_count = row_data.__len__()
    assert row_count == 0, f'Actual: {row_count} -> Data should be empty'
