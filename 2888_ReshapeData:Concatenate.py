import pandas as pd


# concatenateTables vertically stack df1 and df2 together
# Time Complexity: O(n), where n is the total number of rows in df1 and df2
# Space Complexity: O(n)
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2])
