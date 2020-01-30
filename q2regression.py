

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

q2df = pd.read_csv('Q2Regression.csv', header=None)
q2df.columns = ['A','B','C']
q2df.head()
q2df.shape
q2df.info()
q2df.describe()

# detect and remove outliers
import seaborn as sns
sns.boxplot(x=q2df['A'])
sns.boxplot(x=q2df['B'])
sns.boxplot(y=q2df['C'])


# remove the row with C = -1000 and the row with A = 20.60000
df = q2df[(q2df['C'] > -1000) & (q2df['A'] < 20)]
sns.boxplot(y=df['C'])
sns.boxplot(x=df['A'])
sns.boxplot(x=df['B'])
sns.scatterplot(x=df['A'], y=df['B'])

df.head()

ax = df.plot(kind='scatter', x='A', y= 'C', color='b', label='A')
df.plot(kind='scatter', x='B', y= 'C', color='red', label='B', ax=ax)

plt.scatter(df['A'],df['C'], label='A')
plt.scatter(df['B'],df['C'], label='B')
plt.legend()
plt.plot()
plt.show

import numpy as np

# Linear regression equation: C = m0*A + m1*B
# least square regression getting the coefficients m0 and m1
result = np.linalg.lstsq(df[['A','B']].values, df['C'])
result
m = result[0]
m0 = m[0]
m1 = m[1]
m0
m1

# The model is C = 0.49144919628470457 * A + (-11.324968654406058 * B)

# predict C with the model
def predict(A,B):
    return m0*A + m1*B

df['pred_c'] = predict(df['A'],df['B'])
df.head()

# plotting C vs. pred_c
plt.scatter(df['C'],df['pred_c'])

