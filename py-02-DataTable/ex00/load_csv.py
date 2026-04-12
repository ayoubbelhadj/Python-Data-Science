import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a CSV file and return it as a DataFrame.

    Args:
        path: The path to the CSV file.

    Returns:
        A pandas DataFrame, or None if an error occurs.
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None
