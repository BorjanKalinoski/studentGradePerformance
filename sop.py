import pandas as pd
import operator
import matplotlib.pyplot as plt
import numpy as np


def clean_data(data):
    print('before cleaning data')
    print(data)
    print("Shape is:")
    print(data.shape)

    print("Count is:")
    print(data.count())
    data.loc[data['gender'] == 'female', 'gender'] = 0
    data.loc[data['gender'] == 'male', 'gender'] = 1

    data.loc[data['test preparation course'] == 'none', 'test preparation course'] = 0
    data.loc[data['test preparation course'] == 'completed', 'test preparation course'] = 1

    data.loc[data['race/ethnicity'] == 'group A', 'race/ethnicity'] = 0
    data.loc[data['race/ethnicity'] == 'group B', 'race/ethnicity'] = 1
    data.loc[data['race/ethnicity'] == 'group C', 'race/ethnicity'] = 2
    data.loc[data['race/ethnicity'] == 'group D', 'race/ethnicity'] = 3
    data.loc[data['race/ethnicity'] == 'group E', 'race/ethnicity'] = 4

    data.loc[data['math score'] <= 51, 'math score'] = 0
    data.loc[operator.and_(data['math score'] > 51, data['math score'] <= 74), 'math score'] = 1
    data.loc[data['math score'] >= 75, 'math score'] = 2

    data.loc[data['reading score'] <= 51, 'reading score'] = 0
    data.loc[operator.and_(data['reading score'] > 51, data['reading score'] <= 74), 'reading score'] = 1
    data.loc[data['reading score'] >= 75, 'reading score'] = 2

    data.loc[data['writing score'] <= 51, 'writing score'] = 0
    data.loc[operator.and_(data['writing score'] > 51, data['writing score'] <= 74), 'writing score'] = 1
    data.loc[data['writing score'] >= 75, 'writing score'] = 2

    data.loc[data['lunch'] == 'free/reduced', 'lunch'] = 0
    data.loc[data['lunch'] == 'standard', 'lunch'] = 1

    print('after cleaning data')
    print(data)
    print("Shape is:")
    print(data.shape)

    print("Count is:")
    print(data.count())


df = pd.read_csv('studentsperformance.csv', engine='python')
fig = plt.figure(figsize=(18, 6))

clean_data(data=df)

# df['race/ethnicity'].value_counts(normalize=True).plot(kind="bar",alpha=0.5)
# plt.show()
#
# df['gender'].value_counts(normalize=True).plot(kind="bar",alpha=0.5)
# plt.show()
#
# df['parental level of education'].value_counts(normalize=True).plot(kind="bar",alpha=0.5)
# plt.show()
#
# df['lunch'].value_counts(normalize=True).plot(kind="bar",alpha=0.5)
# plt.show()
#
# df['test preparation course'].value_counts(normalize=True).plot(kind="bar",alpha=0.5)
# plt.show()
# leave this commented out


#
# plt.subplot2grid((2, 3), (0, 0))
# df['math score'].value_counts(normalize=True).plot(kind="bar", alpha=0.5)
# plt.title('Math Score')
#
# plt.subplot2grid((2, 3), (0, 1))
# plt.scatter(df['gender'], df['math score'], alpha=0.2)
# plt.title('Math score wrt gender')
#
# plt.subplot2grid((2, 3), (0, 2))
# plt.scatter(df['race/ethnicity'], df['math score'], alpha=0.2)
# plt.title('Math score wrt race/ethnicity')
#
# plt.subplot2grid((2, 3), (1, 0))
# plt.scatter(df['parental level of education'], df['math score'], alpha=0.2)
# plt.title('math score wrt Parental level of education ')
#
# plt.subplot2grid((2, 3), (1, 1))
# plt.scatter(df['test preparation course'], df['math score'], alpha=0.2)
# plt.title('math score wrt Test preparation course')
#
# plt.subplot2grid((2, 3), (1, 2))
# plt.scatter(df['lunch'], df['math score'], alpha=0.2)
# plt.title('math score wrt lunch course ')
#
# plt.show()
#
# plt.subplot2grid((2, 3), (0, 0))
# df['reading score'].value_counts(normalize=True).plot(kind="bar", alpha=0.5)
# plt.title('Reading Score')
#
# plt.subplot2grid((2, 3), (0, 1))
# plt.scatter(df['gender'], df['reading score'], alpha=0.2)
# plt.title('Reading score wrt gender')
#
# plt.subplot2grid((2, 3), (0, 2))
# plt.scatter(df['race/ethnicity'], df['reading score'], alpha=0.2)
# plt.title('reading score wrt race/ethnicity')
#
# plt.subplot2grid((2, 3), (1, 0))
# plt.scatter(df['parental level of education'], df['reading score'], alpha=0.2)
# plt.title('reading score wrt Parental level of education ')
#
# plt.subplot2grid((2, 3), (1, 1))
# plt.scatter(df['test preparation course'], df['reading score'], alpha=0.2)
# plt.title('reading score wrt Test preparation course ')
#
# plt.subplot2grid((2, 3), (1, 2))
# plt.scatter(df['lunch'], df['reading score'], alpha=0.2)
# plt.title('reading score wrt lunch course  ')
# plt.show()

# df.describe()
# print('Describing the data')
# print(df.describe(include='all'))
