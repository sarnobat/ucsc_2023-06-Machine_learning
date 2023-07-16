import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cbook as cbook
import sys
import pandas as pd

##
df = pd.read_csv(sys.argv[1] if len(sys.argv) > 1 else 'housing.csv')
# print(df.columns[1:2].values[:,None])
# print(df)
column_name = 'total_rooms'
column_y_name = 'median_house_value'

print('\n=== Input ===')
print(df[column_name].values)
print(df[column_y_name].values)
plt.scatter(
	df[column_name].values,
	df[column_y_name].values,
	c='r',
	label='data2')

number_of_features = 3
print(df.head(number_of_features)[column_name].values)

df['total_rooms_squared'] = df.total_rooms * df.total_rooms
df['total_rooms_cubed'] = df.total_rooms * df.total_rooms * df.total_rooms

# https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html
# a = np.random.random(5000000)
# b = np.random.random(5000000)
a = np.array([
	[1,1,1],
	[1,2,3],
	[4,5,6],
	[4,5,6]])
# b = np.array([[1,4,5,6]])

x = a

print('\n=== A ===')
print(a)
# print('=== B ===')
# print(b)
# print('=== A x B ===')
# print(np.array(a).dot(np.array(b)))

x = a
xTranspose = np.matrix.transpose(x)

print('\n=== X Transposed ===')
print(xTranspose)

print('\n=== X Transposed dot X ===')
xTransposeDotX = xTranspose.dot(x)
print(xTransposeDotX)

print('\n=== inverse (X Transposed dot X) ===')
xTransposeDotXInverted = np.linalg.inv(xTransposeDotX)
# print('-----------------')
# print(xTransposeDotX)
# print('-----------------')
print(xTransposeDotXInverted)

print('\n=== Y ===')
# y = np.array([7,8,9])
y = np.array(df.head(number_of_features)[column_y_name].values)
print(y)

print('\n=== inverse (X Transposed dot X) dot Y===')

theta = xTransposeDotXInverted.dot(y)
print(theta)

print('\n-----------------')
x = np.linspace(0, 1000, 5000, 20000)
fx = lambda x:  1502560.535 -1927.793779 * x + 0.9177545759 * x**2 -0.00009422419816 * x**3

# median income would be better - "total" is not a good metric

plt.plot(x, fx(x))	
plt.show()