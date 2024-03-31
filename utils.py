import pandas as pd


def load_data(name, column1, column2) -> pd.DataFrame:
    """secures the read data fits the requirements"""
    df = pd.DataFrame({column1: ["0.0"], column2: ["0.0"]})
    try:
        df = pd.read_csv(name)
    except FileNotFoundError:
        print("Read CSV: File not found.")
    except pd.errors.EmptyDataError:
        print("Read CSV: No data")
    except pd.errors.ParserError:
        print("Read CSV: Parse error")
    except BaseException:
        print("Read CSV: unexpected error")
    headers = list(df)
    if headers[0] != column1 or headers[1] != column2:
        return pd.DataFrame({column1: ["0.0"], column2: ["0.0"]})
    return df
