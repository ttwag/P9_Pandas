import pandas as pd


# modifySalaryColumn multiplies the element in the salary column by 2 and returns the dataFrame
# Time Complexity: O(n), where n is the number of rows.
# Space Complexity: O(1)
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees


# test
a = [[1, 40], [5, 50], [101, 50]]
b = pd.DataFrame(a, columns=['name', 'salary'])
print(modifySalaryColumn(b))
