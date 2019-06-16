import pandas as pd
import utils
from sklearn import linear_model, preprocessing, tree

# import visualize

# df = pd.read_csv('studentsperformance.csv', engine='python')

# utils.clean_data(data=df)



target = df['math score'].values
features = df[['test preparation course', 'lunch', 'gender', 'parental level of education']].values

# solver : str, {‘newton-cg’, ‘lbfgs’, ‘liblinear’, ‘sag’, ‘saga’},
# multi_class : str, {‘ovr’, ‘multinomial’, ‘auto’}, optional (default=’ovr’)

classifier = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg')
classifier_ = classifier.fit(features, target)

print('Logistic Regression!')
print(classifier_.score(features, target))

#
# poly = preprocessing.PolynomialFeatures(degree=2)
# poly_features = poly.fit_transform(features)
#
# classifier_ = classifier.fit(poly_features, target)
# print(classifier_.score(poly_features, target))
#
# decision_tree = tree.DecisionTreeClassifier(random_state=1)
# decision_tree_ = decision_tree.fit(features, target)
# print(decision_tree_.score(features, target))
