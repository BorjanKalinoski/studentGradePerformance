import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

pink = '#FFC0CB'
blue = '#0000FF'
red = '#ff0000'
green = '#00ff00'

print('Showing graphs')


def show_graphs(df):
    fig = plt.figure(figsize=(18, 6))

    plt.subplot2grid((2, 3), (0, 0))
    df['math score'].value_counts(normalize=True).plot(kind="bar", alpha=0.5)
    plt.title('Math Score')

    plt.subplot2grid((2, 3), (0, 1))
    plt.scatter(df['gender'], df['math score'], alpha=0.2)
    plt.title('Math score wrt gender')

    plt.subplot2grid((2, 3), (0, 2))
    plt.scatter(df['race/ethnicity'], df['math score'], alpha=0.2)
    plt.title('Math score wrt race/ethnicity')

    plt.subplot2grid((2, 3), (1, 0))
    plt.scatter(df['parental level of education'], df['math score'], alpha=0.2)
    plt.title('math score wrt Parental level of education ')

    plt.subplot2grid((2, 3), (1, 1))
    plt.scatter(df['test preparation course'], df['math score'], alpha=0.2)
    plt.title('math score wrt Test preparation course')

    plt.subplot2grid((2, 3), (1, 2))
    plt.scatter(df['lunch'], df['math score'], alpha=0.2)
    plt.title('math score wrt lunch course ')

    plt.show()

    plt.subplot2grid((2, 3), (0, 0))
    df['reading score'].value_counts(normalize=True).plot(kind="bar", alpha=0.5)
    plt.title('Reading Score')

    plt.subplot2grid((2, 3), (0, 1))
    plt.scatter(df['gender'], df['reading score'], alpha=0.2)
    plt.title('Reading score wrt gender')

    plt.subplot2grid((2, 3), (0, 2))
    plt.scatter(df['race/ethnicity'], df['reading score'], alpha=0.2)
    plt.title('reading score wrt race/ethnicity')

    plt.subplot2grid((2, 3), (1, 0))
    plt.scatter(df['parental level of education'], df['reading score'], alpha=0.2)
    plt.title('reading score wrt Parental level of education ')

    plt.subplot2grid((2, 3), (1, 1))
    plt.scatter(df['test preparation course'], df['reading score'], alpha=0.2)
    plt.title('reading score wrt Test preparation course ')

    plt.subplot2grid((2, 3), (1, 2))
    plt.scatter(df['lunch'], df['reading score'], alpha=0.2)
    plt.title('reading score wrt lunch course  ')
    plt.show()


def show_new_graphs(df):
    fig = plt.figure(figsize=(18, 6))

    plt.subplot2grid((3, 4), (0, 0))
    df['school'].value_counts(normalize=True).plot(kind='bar', alpha=0.5, color=['#f3f300', '#ff9700'])
    one = mpatches.Patch(facecolor='#f3f300', label='GP', linewidth=0.5, edgecolor='black')
    two = mpatches.Patch(facecolor='#ff9700', label='MS', linewidth=0.5, edgecolor='black')
    plt.title('Student School percentage')
    plt.legend(handles=[one, two], fontsize='small', fancybox=True)

    plt.subplot2grid((3, 4), (0, 1))
    df['sex'].value_counts(normalize=True).plot(kind='bar', alpha=0.5, color=[pink, blue])
    one = mpatches.Patch(facecolor=pink, label='F', linewidth=0.5, edgecolor='black')
    two = mpatches.Patch(facecolor=blue, label='M', linewidth=0.5, edgecolor='black')
    plt.title('Student Gender percentage')
    plt.legend(handles=[one, two], fontsize='small', fancybox=True)

    plt.subplot2grid((3, 4), (0, 2))
    df['age'].value_counts(normalize=True).plot(kind='bar', alpha=0.5)
    plt.title('Student age percentage')

    plt.subplot2grid((3, 4), (0, 3))
    df['address'].value_counts(normalize=True).plot(kind='bar', alpha=0.5, color=[blue, pink])
    one = mpatches.Patch(facecolor=blue, label='Urban', linewidth=0.5, edgecolor='black')
    two = mpatches.Patch(facecolor=pink, label='Rural', linewidth=0.5, edgecolor='black')
    plt.title('Student address percentage')
    plt.legend(handles=[one, two], fontsize='small', fancybox=True)

    plt.subplot2grid((3, 4), (1, 0))
    df['reason'].value_counts(normalize=True).plot(kind='bar', alpha=0.5, color=[blue, pink, red, green])
    one = mpatches.Patch(facecolor=blue, label='course', linewidth=0.5, edgecolor='black')
    two = mpatches.Patch(facecolor=pink, label='home', linewidth=0.5, edgecolor='black')
    three = mpatches.Patch(facecolor=red, label='reputation', linewidth=0.5, edgecolor='black')
    four = mpatches.Patch(facecolor=green, label='other', linewidth=0.5, edgecolor='black')

    plt.title('Student\'s reason to go to school')
    plt.legend(handles=[one, two, three, four], fontsize='small', fancybox=True)

    plt.subplot2grid((3, 4), (1, 1))
    df['traveltime'].value_counts(normalize=True).plot(kind='bar', alpha=0.5, color=[blue, pink, red, green])
    one = mpatches.Patch(facecolor=blue, label='<15min', linewidth=0.5, edgecolor='black')
    two = mpatches.Patch(facecolor=pink, label='15<time<30', linewidth=0.5, edgecolor='black')
    three = mpatches.Patch(facecolor=red, label='30<time<60', linewidth=0.5, edgecolor='black')
    four = mpatches.Patch(facecolor=green, label='>60', linewidth=0.5, edgecolor='black')
    plt.title('Student\'s travel time to go to school')
    plt.legend(handles=[one, two, three, four], fontsize='small', fancybox=True)

    plt.subplot2grid((3, 4), (1, 2))
    df['studytime'].value_counts(normalize=True).plot(kind='bar', alpha=0.5, color=[blue, pink, red, green])
    one = mpatches.Patch(facecolor=blue, label='2h<time<5h', linewidth=0.5, edgecolor='black')
    two = mpatches.Patch(facecolor=pink, label='<2h', linewidth=0.5, edgecolor='black')
    three = mpatches.Patch(facecolor=red, label='5h<time<10h', linewidth=0.5, edgecolor='black')
    four = mpatches.Patch(facecolor=green, label='>10h', linewidth=0.5, edgecolor='black')
    plt.title('Student\'s weekly study time ')
    plt.legend(handles=[one, two, three, four], fontsize='small', fancybox=True)

    plt.subplot2grid((3, 4), (1, 3))
    df['failures'].value_counts(normalize=True).plot(kind='bar', alpha=0.5)
    plt.title('Student\'s past class failures')

    plt.subplot2grid((3, 4), (2, 0))
    df['schoolsup'].value_counts(normalize=True).plot(kind='bar', alpha=0.5, color=[pink, blue])
    one = mpatches.Patch(facecolor=pink, label='No', linewidth=0.5, edgecolor='black')
    two = mpatches.Patch(facecolor=blue, label='Yes', linewidth=0.5, edgecolor='black')
    plt.title('Student extra school educational support')
    plt.legend(handles=[one, two], fontsize='small', fancybox=True)

    plt.subplot2grid((3, 4), (2, 1))
    df['famsup'].value_counts(normalize=True).plot(kind='bar', alpha=0.5, color=[blue, pink])
    one = mpatches.Patch(facecolor=pink, label='No', linewidth=0.5, edgecolor='black')
    two = mpatches.Patch(facecolor=blue, label='Yes', linewidth=0.5, edgecolor='black')
    plt.title('Student extra family educational support')
    plt.legend(handles=[one, two], fontsize='small', fancybox=True)

    plt.subplot2grid((3, 4), (2, 2))
    df['paid'].value_counts(normalize=True).plot(kind='bar', alpha=0.5, color=[pink, blue])
    one = mpatches.Patch(facecolor=pink, label='No', linewidth=0.5, edgecolor='black')
    two = mpatches.Patch(facecolor=blue, label='Yes', linewidth=0.5, edgecolor='black')
    plt.title('Student extra paid classes')
    plt.legend(handles=[two, one], fontsize='small', fancybox=True)

    plt.subplot2grid((3, 4), (2, 3))
    df['activities'].value_counts(normalize=True).plot(kind='bar', alpha=0.5, color=[blue, pink])
    one = mpatches.Patch(facecolor=pink, label='No', linewidth=0.5, edgecolor='black')
    two = mpatches.Patch(facecolor=blue, label='Yes', linewidth=0.5, edgecolor='black')
    plt.title('Student extra-curricular activities')
    plt.legend(handles=[one, two], fontsize='small', fancybox=True)

    plt.show()

    plt.subplot2grid((3, 4), (0, 0))
    df['nursery'].value_counts(normalize=True).plot(kind='bar', alpha=0.5, color=[blue, pink])
    one = mpatches.Patch(facecolor=pink, label='No', linewidth=0.5, edgecolor='black')
    two = mpatches.Patch(facecolor=blue, label='Yes', linewidth=0.5, edgecolor='black')
    plt.title('Student attended nursery class')
    plt.legend(handles=[one, two], fontsize='small', fancybox=True)

    plt.subplot2grid((3, 4), (0, 1))
    df['higher'].value_counts(normalize=True).plot(kind='bar', alpha=0.5, color=[blue, pink])
    one = mpatches.Patch(facecolor=pink, label='No', linewidth=0.5, edgecolor='black')
    two = mpatches.Patch(facecolor=blue, label='Yes', linewidth=0.5, edgecolor='black')
    plt.title('Student wants to take higher education')
    plt.legend(handles=[one, two], fontsize='small', fancybox=True)

    plt.subplot2grid((3, 4), (0, 2))
    df['internet'].value_counts(normalize=True).plot(kind='bar', alpha=0.5, color=[blue, pink])
    one = mpatches.Patch(facecolor=pink, label='No', linewidth=0.5, edgecolor='black')
    two = mpatches.Patch(facecolor=blue, label='Yes', linewidth=0.5, edgecolor='black')
    plt.title('Student Internet access at home ')
    plt.legend(handles=[one, two], fontsize='small', fancybox=True)

    plt.subplot2grid((3, 4), (0, 3))
    df['romantic'].value_counts(normalize=True).plot(kind='bar', alpha=0.5, color=[pink, blue])
    one = mpatches.Patch(facecolor=pink, label='No', linewidth=0.5, edgecolor='black')
    two = mpatches.Patch(facecolor=blue, label='Yes', linewidth=0.5, edgecolor='black')
    plt.title('Student with a romantic relationship')
    plt.legend(handles=[one, two], fontsize='small', fancybox=True)

    plt.subplot2grid((3, 4), (1, 0))
    df['famrel'].value_counts(normalize=True).plot(kind='bar', alpha=0.5)
    plt.title('Student  quality of family relationships')

    plt.subplot2grid((3, 4), (1, 1))
    df['freetime'].value_counts(normalize=True).plot(kind='bar', alpha=0.5)
    plt.title('Student free time after school')
    #
    plt.subplot2grid((3, 4), (1, 2))
    df['goout'].value_counts(normalize=True).plot(kind='bar', alpha=0.5)
    plt.title('Student going out with friends ')

    plt.subplot2grid((3, 4), (1, 3))
    df['Dalc'].value_counts(normalize=True).plot(kind='bar', alpha=0.5)
    plt.title('Student workday alcohol consumption')

    plt.subplot2grid((3, 4), (2, 0))
    df['Walc'].value_counts(normalize=True).plot(kind='bar', alpha=0.5)
    plt.title('Student weekend alcohol consumption')

    plt.subplot2grid((3, 4), (2, 1))
    df['health'].value_counts(normalize=True).plot(kind='bar', alpha=0.5)
    plt.title('Student current health status')
    #
    plt.subplot2grid((3, 4), (2, 2))
    df['absences'].value_counts(normalize=True).plot(kind='bar', alpha=0.5)
    plt.title('Student number of school absences')
    
    plt.show()
    
    #semi / FULL ABSENCE GRID
    plt.subplot2grid((3, 4), (0, 0) ,colspan=4)
    df['absences'].value_counts(normalize=False).plot(kind='bar', alpha=0.5)
    plt.title('Student number of school absences')

    plt.subplot2grid((3, 4), (1, 1), colspan=2)
    df['absenceGr'].value_counts(normalize=True).plot(kind='bar', alpha=0.5)
    plt.title('Student number in absence groups')

    plt.subplot2grid((3, 4), (2, 0), colspan=4,rowspan=2)
    for x in [1, 2, 3, 4]:
        df['G3'][df['absenceGr'] == x].plot(kind="kde")
    plt.title('Final grade wrt absence group')
    plt.legend(('1', '2', '3', '4'))
    #semi
    plt.show()

    plt.subplot2grid((3, 4), (0, 0))
    df['G1'].value_counts(normalize=True).plot(kind='bar', alpha=0.5)
    plt.title('Student first period grade')

    plt.subplot2grid((3, 4), (0, 1))
    df['G2'].value_counts(normalize=True).plot(kind='bar', alpha=0.5)
    plt.title('Student second period grade')

    plt.subplot2grid((3, 4), (0, 2))
    df['G3'].value_counts(normalize=True).plot(kind='bar', alpha=0.5)
    plt.title('Student final grade')
    plt.show()

    plt.subplot2grid((3, 4), (0, 0), colspan=4)
    for x in [1, 2, 3, 4]:
        df['G3'][df['studytime'] == x].plot(kind="kde")
    plt.title('Final grade wrt studytime')
    plt.legend(('<2h', '2h<time<5h', '5<time<10', '>10'))

    plt.subplot2grid((3, 4), (1, 0))
    plt.scatter(df['paid'], df['G3'], alpha=0.1)
    plt.title('Final score wrt paid classes')

    plt.subplot2grid((3, 4), (1, 1))
    plt.scatter(df['internet'], df['G3'], alpha=0.1)
    plt.title('Final score wrt internet access')

    plt.subplot2grid((3, 4), (1, 2))
    plt.scatter(df['higher'], df['G3'], alpha=0.1)
    plt.title('Final score wrt wants to continue to higher education')

    plt.subplot2grid((3, 4), (1, 3))
    plt.scatter(df['nursery'], df['G3'], alpha=0.1)
    plt.title('Final score wrt nursery class')
    plt.show()

    plt.subplot2grid((3, 4), (0, 0))
    plt.scatter(df['romantic'], df['G3'], alpha=0.1)
    plt.title('Final score wrt romantic relationship')

    plt.subplot2grid((3, 4), (0, 1))
    plt.scatter(df['schoolsup'], df['G3'], alpha=0.1)
    plt.title('Final score wrt school support')

    plt.subplot2grid((3, 4), (0, 2))
    plt.scatter(df['famsup'], df['G3'], alpha=0.1)
    plt.title('Final score wrt family support')

    plt.subplot2grid((3, 4), (0, 3))
    plt.scatter(df['activities'], df['G3'], alpha=0.1)
    plt.title('Final score wrt extra-activities')

    plt.subplot2grid((3, 4), (1, 0), colspan=2)
    for x in [1, 2, 3, 4, 5]:
        df['G3'][df['famrel'] == x].plot(kind="kde")
    plt.title('Final grade wrt famrel')
    plt.legend(('1', '2', '3', '4', '5'))

    plt.subplot2grid((3, 4), (1, 2), colspan=2)
    for x in [1, 2, 3, 4, 5]:
        df['G3'][df['freetime'] == x].plot(kind="kde")
    plt.title('Final grade wrt freetime')
    plt.legend(('1', '2', '3', '4', '5'))

    plt.subplot2grid((3, 4), (2, 0), colspan=2)
    for x in [1, 2, 3, 4, 5]:
        df['G3'][df['goout'] == x].plot(kind="kde")
    plt.title('Final grade wrt goout')
    plt.legend(('1', '2', '3', '4', '5'))

    plt.subplot2grid((3, 4), (2, 3), colspan=2)
    for x in [1, 2, 3, 4, 5]:
        df['G3'][df['health'] == x].plot(kind="kde")
    plt.title('Final grade wrt health')
    plt.legend(('1', '2', '3', '4', '5'))

    plt.show()
    plt.subplot2grid((3, 4), (0, 0), colspan=2)
    for x in [1, 2, 3, 4, 5]:
        df['G3'][df['Dalc'] == x].plot(kind="kde")
    plt.title('Final grade wrt Daily alcohol')
    plt.legend(('1', '2', '3', '4', '5'))

    plt.subplot2grid((3, 4), (0, 2), colspan=2)
    for x in [1, 2, 3, 4, 5]:
        df['G3'][df['Walc'] == x].plot(kind="kde")
    plt.title('Final grade wrt weekly alcohol')
    plt.legend(('1', '2', '3', '4', '5'))

    plt.subplot2grid((3, 4), (1, 0), colspan=2)
    for x in [0, 1, 2, 3, 4]:
        df['G3'][df['Medu'] == x].plot(kind="kde")
    plt.title('Final grade wrt Mother\'s education')
    plt.legend(('0', '1', '2', '3', '4'))

    plt.subplot2grid((3, 4), (1, 2), colspan=2)
    for x in [0, 1, 2, 3, 4]:
        df['G3'][df['Fedu'] == x].plot(kind="kde")
    plt.title('Final grade wrt Father\'s education')
    plt.legend(('0', '1', '2', '3', '4'))

    plt.subplot2grid((3, 4), (2, 0))
    plt.scatter(df['Pstatus'], df['G3'], alpha=0.1)
    plt.title('Final score wrt Pstatus')

    plt.subplot2grid((3, 4), (2, 1))
    plt.scatter(df['famsize'], df['G3'], alpha=0.1)
    plt.title('Final score wrt famsize')

    plt.show()

    plt.subplot2grid((3, 4), (0, 0))
    plt.scatter((df['G2'] + df['G1']) / 2, df['G3'], alpha=0.1)
    plt.title('Final score wrt previous scores')
    plt.show()
