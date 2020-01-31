

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

q2df = pd.read_csv('Q2Regression.csv', header=None)
df_cp = q2df.copy()
df_cp.insert(0, 'Ones', 1)
df_cp.head()

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

# Linear regression equation: C = c + m1*A + m2*B
# manually calculating m1 and m2 using formula found online
# denominator
dn = np.sum(np.square(df['A']))*np.sum(df['B']*df['B']) - np.square(np.sum(df['A']*df['B']))

m1 = (np.sum(np.square(df['B']))*np.sum(df['A']*df['C']) - np.sum(df['A']*df['B'])* np.sum(df['B']*df['C']))/dn
m2 = (np.sum(np.square(df['A']))*np.sum(df['B']*df['C']) - np.sum(df['A']*df['B'])* np.sum(df['A']*df['C']))/dn

# Linear regression equation: C = c + b1*A + b2*B
# using np.linalg.lstqq

result = np.linalg.lstsq(df[['A','B']], df['C'])
b =result[0]
b1 = b[0]
b2 = b[1]
b1
b2
m1
m2

# b1 = m1 & b2 = m2

# calculate c with m1 and m2
c = df['C'].mean() - df['A'].mean() - m2*df['B'].mean()
c

# The model is C = 0.49144919628470457 * A + (-11.324968654406058 * B)

# predict C with the model
def predict(A,B):
    return m1*A + m2*B + c

df['pred_c'] = predict(df['A'],df['B'])
df.head()

# plotting C vs. pred_c
plt.scatter(df['C'],df['pred_c'])

