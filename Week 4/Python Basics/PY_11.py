import numpy as np
import pandas as pd
# w = np.zeros(5)
# print(w)

df = pd.DataFrame(np.arange(12).reshape(3, 4), columns=['A', 'B', 'C', 'D'])
print(df)
print(df.drop(['B', 'C'], axis=1))

