import pandas as pd


# pivotTable pivots the weather dataFrame to have month as the row index and city as the column.
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month', columns='city', values='temperature')
