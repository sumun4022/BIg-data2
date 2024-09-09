import pandas as pd

df = pd.DataFrame(
    {
    "a": [14,51,6],
    "b": [72, 8, 72],
    "c": [100, 11, 12]
    }, index = [1, 2, 3]
)
print(df)