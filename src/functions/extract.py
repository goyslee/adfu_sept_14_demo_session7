import pandas as pd

def read_csv(filename):
    try:
        return pd.read_csv(filename)
    except Exception as e:
        print(f"Error on reading csv file: {e}")
        raise
