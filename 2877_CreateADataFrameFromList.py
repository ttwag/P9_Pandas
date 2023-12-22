from typing import List
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# createDataframe converts a 2-D list into a pandas DataFrame object.
# Time Complexity: O(n * m), where n is the number of rows and m is the number of columns.
# Space Complexity: O(n * m)
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=['student_id', 'age'], index=['a', 'b', 'c'])
    return df


# Test
a = [[919, 12], [939, 19], [929, 20]]
b = createDataframe(a)
print(b)
