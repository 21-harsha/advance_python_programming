import pandas as pd
import numpy as np

numbers = np.random.randint(1, 100, 10)

s = pd.Series(numbers)


print("Pandas Series:")
print(s)