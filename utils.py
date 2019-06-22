import operator


def clean_math_data(data):
    print('before cleaning data')
    print(data)
    print("Shape is:")
    print(data.shape)

    print("Count is:")
    print(data.count())
    data.loc[data['sex'] == 'F', 'sex'] = 1
    data.loc[data['sex'] == 'M', 'sex'] = 0

    data.loc[data['school'] == 'GP', 'school'] = 1
    data.loc[data['school'] == 'MS', 'school'] = 0

    data.loc[data['address'] == 'U', 'address'] = 1
    data.loc[data['address'] == 'R', 'address'] = 0

    data.loc[data['reason'] == 'course', 'reason'] = 0
    data.loc[data['reason'] == 'home', 'reason'] = 1
    data.loc[data['reason'] == 'reputation', 'reason'] = 2
    data.loc[data['reason'] == 'other', 'reason'] = 3

    data.loc[data['schoolsup'] == 'yes', 'schoolsup'] = 1
    data.loc[data['schoolsup'] == 'no', 'schoolsup'] = 0

    data.loc[data['famsup'] == 'yes', 'famsup'] = 1
    data.loc[data['famsup'] == 'no', 'famsup'] = 0

    data.loc[data['paid'] == 'no', 'paid'] = 0
    data.loc[data['paid'] == 'yes', 'paid'] = 1

    data.loc[data['activities'] == 'yes', 'activities'] = 1
    data.loc[data['activities'] == 'no', 'activities'] = 0

    data.loc[data['nursery'] == 'no', 'nursery'] = 0
    data.loc[data['nursery'] == 'yes', 'nursery'] = 1

    data.loc[data['higher'] == 'no', 'higher'] = 0
    data.loc[data['higher'] == 'yes', 'higher'] = 1

    data.loc[data['internet'] == 'no', 'internet'] = 0
    data.loc[data['internet'] == 'yes', 'internet'] = 1

    data.loc[data['romantic'] == 'no', 'romantic'] = 0
    data.loc[data['romantic'] == 'yes', 'romantic'] = 1
    print('after cleaning data')
    print(data)
    print("Shape is:")
    print(data.shape)

    print("Count is:")
    print(data.count())


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

def createAbsenceGroups(data):
    print('before grouping absence data')
    print(data)
    print("Shape is:")
    print(data.shape)

    print("Count is:")
    print(data.count())

    gr1Lower = 0
    gr1Upper = 15  #grupa kade imaat najmalce otsustvo e gr1

    gr2Lower = 16
    gr2Upper = 31

    gr3Lower = 32
    gr3Upper = 47

    
    data.loc[operator.and_(data['absences']>=gr1Lower,data['absences']<=gr1Upper),'absenceGr']=1
    data.loc[operator.and_(data['absences']>=gr2Lower,data['absences']<=gr2Upper),'absenceGr']=2
    data.loc[operator.and_(data['absences']>=gr3Lower,data['absences']<=gr3Upper),'absenceGr']=3
    data.loc[data['absences']>gr3Upper,'absenceGr']=4

    print('after grpuping absence data')
    print(data)
    print("Shape is:")
    print(data.shape)

    print("Count is:")
    print(data.count())