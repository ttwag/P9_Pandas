import pandas as pd


# dropDuplicateEmails removes the rows with duplicated data in the email column
# Time Complexity: O(n), where n is the number of rows
# Space Complexity: O(n)
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset='email')


# test
a = [[1, 40], [2, 50], [101, 50]]
b = pd.DataFrame(a, columns=['student_id', 'email'])
print(dropDuplicateEmails(b))
