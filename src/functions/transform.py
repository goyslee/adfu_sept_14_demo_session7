import pandas as pd


def merge_data(stock_data: pd.DataFrame, sales_data: pd.DataFrame):
    sales_data = sales_data.drop_duplicates(keep="last")
    merged_data = stock_data.merge(sales_data, how="right", on="product_id")
    return merged_data


def subtract_sales(merged_data):
    merged_data["quantity_in_stock"] = (
        merged_data["quantity_in_stock"] - merged_data["sales"]
    )
    return merged_data
