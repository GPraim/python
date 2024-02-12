import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

grouped = data.groupby('whoAmI').size().reset_index(name='count')
one_hot = pd.DataFrame(0, index=range(len(data)), columns=grouped['whoAmI'])

for i, row in data.iterrows():
    one_hot.loc[i, row['whoAmI']] = 1
    
one_hot.head()