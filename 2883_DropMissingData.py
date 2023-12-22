import pandas as pd


# dropMissingData removes the row with entry 'None' in the 'name' column.
# Time Complexity: O(n)
# Space Complexity: O(n)
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students['name'].notnull()]


a = [[1, 40], [None, 50], [101, 50]]
b = pd.DataFrame(a, columns=['name', 'email'])
print(dropMissingData(b))
