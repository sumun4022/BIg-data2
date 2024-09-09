import pandas as pd

# df = pd.DataFrame(
#     {
#     "a": [14,51,6],
#     "b": [72, 8, 72],
#     "c": [100, 11, 12]
#     }, index = [1, 2, 3]
# )
df = pd.DataFrame(
    [
        [14,72,100],
        [51, 8, 11],
        [6, 72, 12]
    ], index = [1, 2, 3], columns=["a", "b","c"]
)
print(df)
print(df.shape)
print(df["b"].value_counts())
print(df["b"].nunique())
print(df.describe())