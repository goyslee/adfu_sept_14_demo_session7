import pandas as pd
import pytest

from functions.extract import read_csv
from functions.transform import merge_data, subtract_sales

# As a user I want to load in two csv files to be processed
# Using Pandas


def test_read_csv():
    # Arrange - set up input and expected output
    filename = "test_data/test.csv"
    expected_length = 1
    expected_id = 123
    expected_type = pd.DataFrame

    # Act
    stock_data = read_csv(filename)

    # Assert
    assert len(stock_data) == expected_length
    assert stock_data["product_id"][0] == expected_id
    assert type(stock_data) is expected_type


def test_read_csv_error():
    # Arrange - set up input and expected output
    filename = "test_data/test_non_existant.csv"

    with pytest.raises(FileNotFoundError):
        read_csv(filename)


# As a user I want to merge the stock and sales data on the product ID
# and then subtract the sale volume from the stock volume


@pytest.mark.dependency(test_read_csv())
def test_merge_datasets():
    # Arrange
    filename = "test_data/test.csv"
    stock_data = read_csv(filename)
    filename = "test_data/test_sales.csv"
    sales_data = read_csv(filename)
    # 9 col in stock
    # 3 col in sales
    # Therefore 11 col in merged data
    expected_number_cols = 11
    # Act
    merged_data = merge_data(stock_data, sales_data)
    # Assert
    assert len(merged_data.columns) == expected_number_cols


@pytest.mark.dependency(test_read_csv(), test_merge_datasets())
def test_subtract_datasets():
    # Arrange
    filename = "test_data/test.csv"
    stock_data = read_csv(filename)
    filename = "test_data/test_sales.csv"
    sales_data = read_csv(filename)
    merged_data = merge_data(stock_data, sales_data)
    expected_stock = 5

    # Act
    subtracted_data = subtract_sales(merged_data)
    # Assert
    assert subtracted_data["quantity_in_stock"][0] == expected_stock
