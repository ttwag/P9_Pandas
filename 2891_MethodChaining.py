import pandas as pd

# findHeavyAnimals sorts the animals based on weight and return the animal name with weight > 100
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    sorted_animals = animals.sort_values(by=['weight'], ascending=False)
    return sorted_animals.loc[sorted_animals['weight'] > 100, ['name']]


a = [[1, 40, 30], [5, 50, 20], [101, 50, 30]]
b = pd.DataFrame(a, columns=['name', 'weight', 'd'])
print(findHeavyAnimals(b))
