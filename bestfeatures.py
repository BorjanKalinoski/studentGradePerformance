#forked and pushed branch
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
import utils
import visualize
import sys
from itertools import combinations

df = pd.read_csv('student-mat.csv')

printed = "unprinted"
if len(sys.argv) > 2: printed=sys.argv[2] #'python sop.py <anything> printed' will print dataset before and after 
utils.clean_math_data(df,printed) 
utils.createAbsenceGroups(df,printed)

if len(sys.argv) > 1 and  sys.argv[1] == "visual": 
    visualize.show_new_graphs(df) # 'python sop.py visual' will show the graphs aswell

print(df.shape)

#FEATURE SELECTION______________________________________
#site featuri se:
allfeatures = ['G1','G2','school', 'sex','age',	'address','Medu','Fedu','reason','traveltime','studytime','failures','schoolsup','famsup','paid','activities','nursery','higher','internet','romantic','famrel','freetime','goout','Dalc','Walc','health','absences']
#features = ['G1','G2','absenceGr','nursery','absences','traveltime','studytime','famsup','romantic','famrel','Walc','Dalc'] #dosega najdobar 83.12
#features = ['G1','G2','absenceGr','nursery','absences','traveltime','studytime','famsup','romantic','famrel','Walc','Dalc']
labels = ['G3']
y = df[labels[0]].values

c=0
maxscore = 0;
for x in range(2,len(allfeatures)):
    comb = combinations(allfeatures,x) #site mozhni kombinacii na featuri
    print("Klasa: ",x)
    for features in list(comb):  #tekovno feature kombinacija
        features=list(features)
       
        X = df[features].values
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        regressor = LinearRegression()
        regressor.fit(X_train, y_train)  # training the algorithm

        y_pred = regressor.predict(X_test)

        score = metrics.r2_score(y_test, y_pred)
        if score > maxscore : 
            maxscore = score
            bestfeatures = features
            xclass=x
            print("__________________________________________________________________NEW MAXSCORE:",maxscore)
            print("__________________________________________________________________NEW BESTFEATURES BELOW")
            print(bestfeatures)
            print("__________________________________________________________________element class:",xclass)

    

print("The best combination of features is: ",bestfeatures)
print("Whith a max score of",maxscore)