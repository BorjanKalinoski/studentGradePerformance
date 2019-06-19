import operator


def createAbsenceGroups(data):
    print('before grouping absence data')
    print(data)
    print("Shape is:")
    print(data.shape)

    print("Count is:")
    print(data.count())

    gr1Lower = 0
    gr1Upper = 3  #grupa kade imaat najmalce otsustvo e gr1

    gr2Lower = 4
    gr2Upper = 7

    gr3Lower = 8
    gr3Upper = 11 #grupa kaj ima najvekej otsustvo e gr3

    
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



