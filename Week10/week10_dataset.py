import seaborn as sns
import numpy as np

print(sns.get_dataset_names())
# titanic = sns.load_Dateset('titanic')

mpg = sns.load_dataset('mpg')
print(mpg.head().sort_values('mpg'))