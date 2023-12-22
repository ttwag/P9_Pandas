import pandas as pd


# meltTable melts the long table to a short vertical table dataFrame
def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report, id_vars='product', var_name='quarter', value_name='sales')
