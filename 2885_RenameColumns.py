import pandas as pd


# renameColumns renames the id, first, last, and age columns
# Time Complexity: O(1)
# Space Complexity: O(1)
def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.rename(columns={'id': 'student_id', 'first': 'first_name', 'last': 'last_name', 'age': 'age_in_years'},
                    inplace=True)
    return students


# test
a = [[1, 40, 30, 30], [5, 50, 20, 30], [101, 50, 30, 10]]
b = pd.DataFrame(a, columns=['id', 'first', 'last', 'age'])
print(renameColumns(b))
