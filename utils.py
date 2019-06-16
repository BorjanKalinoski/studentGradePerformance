import operator
def clean_data(data):
    # print('before cleaning data')
    # print(data)
    # print("Shape is:")
    # print(data.shape)
    #
    # print("Count is:")
    # print(data.count())
    data.loc[data['gender'] == 'female', 'gender'] = 0
    data.loc[data['gender'] == 'male', 'gender'] = 1

    data.loc[data['test preparation course'] == 'none', 'test preparation course'] = 0
    data.loc[data['test preparation course'] == 'completed', 'test preparation course'] = 1

    data.loc[data['race/ethnicity'] == 'group A', 'race/ethnicity'] = 0
    data.loc[data['race/ethnicity'] == 'group B', 'race/ethnicity'] = 1
    data.loc[data['race/ethnicity'] == 'group C', 'race/ethnicity'] = 2
    data.loc[data['race/ethnicity'] == 'group D', 'race/ethnicity'] = 3
    data.loc[data['race/ethnicity'] == 'group E', 'race/ethnicity'] = 4

    data.loc[data['parental level of education'] == 'master\'s degree', 'parental level of education'] = 0
    data.loc[data['parental level of education'] == 'bachelor\'s degree', 'parental level of education'] = 1
    data.loc[data['parental level of education'] == 'associate\'s degree', 'parental level of education'] = 2
    data.loc[data['parental level of education'] == 'some college', 'parental level of education'] = 3
    data.loc[data['parental level of education'] == 'high school', 'parental level of education'] = 4
    data.loc[data['parental level of education'] == 'some high school', 'parental level of education'] = 5

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
    #
    # print('after cleaning data')
    # print(data)
    # print("Shape is:")
    # print(data.shape)
    #
    # print("Count is:")
    # print(data.count())
