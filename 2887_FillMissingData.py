import pandas as pd

# fillMissingValues fills None with 0
def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    #products.loc[products['quantity'].isnull(), 'quantity'] = 0
    products['quantity'] = products['quantity'].fillna(0)
    return products


a = [[1, 40, 30], [5, 50, None], [101, 50, None]]
b = pd.DataFrame(a, columns=['id', 'first', 'quantity'])
print(fillMissingValues(b))
