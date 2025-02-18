from functions.extract import read_csv
from functions.transform import merge_data, subtract_sales
import pandas as pd

def hello():
    print("Hello")

def main():
    stock_data = read_csv("Datasets/stock_data.csv")
    sales_data = read_csv("Datasets/sales_data.csv")
    merged_data = merge_data(stock_data, sales_data)
    subtracted_data = subtract_sales(merged_data)
    print(subtracted_data)
    print("Hello Github")


if __name__ == "__main__":
    main()
