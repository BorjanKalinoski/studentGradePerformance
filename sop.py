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
features = ['G1','G2','absenceGr','nursery','absences','traveltime','studytime','famsup','romantic','famrel','Walc','Dalc']
labels = ['G3']

X = df[features].values
y = df[labels[0]].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)  # training the algorithm

coeff_df = pd.DataFrame(regressor.coef_, features, columns=['Coefficient'])

print(coeff_df)

# # To retrieve the intercept:
# print(regressor.intercept_)
# # For retrieving the slope:
# print(regressor.coef_)

y_pred = regressor.predict(X_test)

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df1 = df.head(300)

#score determination_______________________________________________
print("-------Succes rate (R^2 coefficient determination)-------")
print(regressor.score(X_test,y_test)*100,"%")
print( metrics.r2_score(y_test, y_pred)*100,"% (alternate method)")
print("---------------------------------------------------------")

df1.plot(kind='bar', figsize=(10, 8))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

plt.scatter(X_test[:, 0], y_test, color='gray')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.show()

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
