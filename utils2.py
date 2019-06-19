import operator


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



