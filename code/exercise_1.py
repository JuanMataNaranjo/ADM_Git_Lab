import numpy as np
import pandas as pd

print('Hello World!')

df = pd.read_csv('../git_test_moved.csv')

print(df.head())

df['Food'] = ['P', 'G', 'F', 'A']

df.to_csv('../git_update.csv')

print(df.head())