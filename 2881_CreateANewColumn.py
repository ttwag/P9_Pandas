import pandas as pd


# createBonusColumn creates a new column, bonus, that has twice the value of the salary in each row.
# Time Complexity: O(n), where n is the number of rows.
# Space Complexity: O(n)
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees


# test
a = [[1, 40], [2, 50], [101, 60]]
b = pd.DataFrame(a, columns=['student_id', 'salary'])
print(createBonusColumn(b))
