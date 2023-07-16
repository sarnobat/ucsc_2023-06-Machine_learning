import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cbook as cbook
import sys
import pandas as pd

##
df = pd.read_csv(sys.argv[1] if len(sys.argv) > 1 else 'housing.csv')
# print(df.columns[1:2].values[:,None])
print(df)
print(df['total_rooms'].values)
print(df['median_house_value'].values)
plt.scatter(df['total_rooms'].values, df['median_house_value'].values, c='r', label='data2')


# https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html
# a = np.random.random(5000000)
# b = np.random.random(5000000)
a = np.array([1,2,3])
b = np.array([4,5,6])

x = a
xTranspose = np.matrix.transpose(x)

xTransposeDotX = xTranspose.dot(x)

print('-----------------')
print(a)
print('-----------------')
print(b)
print('-----------------')
print(np.array(a).dot(np.array(b)))
print('-----------------')
print(xTransposeDotX)
print('-----------------')

x = np.linspace(0, 1000, 5000, 20000)
fx = lambda x:  1502560.535 -1927.793779 * x + 0.9177545759 * x**2 -0.00009422419816 * x**3

# median income would be better - "total" is not a good metric

plt.plot(x, fx(x))	
plt.show()