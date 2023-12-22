import pandas as pd


# selectFirstRows takes the DataFrame object and returns the first 3 rows.
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # return employees[0:3][:]
    return employees.head(3)


# test
a = [[1, 40], [2, 50], [3, 60]]
b = pd.DataFrame(a, columns=['Date', 'Num'])
print(selectFirstRows(b))
