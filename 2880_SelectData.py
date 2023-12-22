import pandas as pd


# selectData selects the row with student_id = 101 and only returns the name and age columns.
# Time Complexity: O(n), where n is the number of row in the DataFrame.
# Space Complexity: O(n)
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == 101, ['name', 'age']]


# test
a = [[1, 40, 70], [2, 50, 80], [101, 60, 90]]
b = pd.DataFrame(a, columns=['student_id', 'name', 'age'])
print(selectData(b))
