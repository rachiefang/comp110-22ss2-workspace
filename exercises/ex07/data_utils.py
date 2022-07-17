"""Dictionary related utility functions."""
from csv import DictReader
__author__ = "730468022"

# Define your function below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform row-oriented to column-oriented."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)  
    return result


def head(data_cols: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Produce new column-based table with only the first N rows of data."""
    data_cols_head: dict[str, list[str]] = {}
    for column in data_cols:
        count: int = 0
        empty_list: list[str] = []
        if num_rows >= len(data_cols[column]):       
             return data_cols
        while count > num_rows:
            empty_list.append(data_cols[column][count])
            count += 1
        data_cols[column] = empty_list
    return data_cols_head


def select(data_cols: dict[str, list[str]], name: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of original columns."""
    selected_data: dict[str, list[str]] = {}
    for column in name:
        selected_data[column] = data_cols[column]
    return selected_data


def concat(d: dict[str, list[str]], a: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in d:
        result[column] = d[column]
    for column in a:
        if column in result:
            result[column] += a[column]
        else:
           result[column] = a[column]
    return result


def count(given_list: list[str]) -> dict[str, int]:
    """Each value is a count of the number of times the value has appeared in the list."""
    result: dict[str, int] = {}
    for item in given_list:
        if item in result:
            result[item] += 1
        else: 
            result[item] = 1
    return result