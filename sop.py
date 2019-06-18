import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
import utils
import visualize

df = pd.read_csv('student-mat.csv')
utils.clean_math_data(df)
# visualize.show_new_graphs(df)
print(df.shape)

features = ['G1', 'G2', 'age','reason','reason','traveltime','studytime','nursery','higher','internet','Dalc','Walc','health','absences']
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
df1 = df.head(25)

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
