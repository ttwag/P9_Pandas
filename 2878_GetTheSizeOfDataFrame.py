from typing import List
import pandas as pd

# getDataframeSize gets the size of the pandas Dataframe object and return it as a list.
# Time Complexity: O(1), .shape is an attribute.
# Space Complexity: O(1)
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0], players.shape[1]]


# test
a = [[1, 40], [2, 50], [3, 60]]
b = pd.DataFrame(a, columns=['Date', 'Num'])
print(getDataframeSize(b))