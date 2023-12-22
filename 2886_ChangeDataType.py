import pandas as pd


# changeDatatype changes the grade column from float to int
# Time Complexity: O(1)
# Space Complexity: O(1)
def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students


# test
a = [[1, 40, 30, 30.00], [5, 50, 20, 30.33], [101, 50, 30, 10.12]]
b = pd.DataFrame(a, columns=['id', 'first', 'last', 'grade'])
print(changeDatatype(b))
