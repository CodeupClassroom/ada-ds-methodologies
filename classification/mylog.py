# IPython log file


from acquire import get_titanic_data
from prepare import prep_titanic_data
df = prep_titanic_data(get_titanic_data())
df.info()
df.dropna(inplace=True)
df.isnull().sum()
X = df.drop([survived], axis=1)
X = df.drop(['survived'], axis=1)
y = df.survived
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.30, random_state=123))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.30, random_state=123)
X_train.shape
X_test.shape
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
rf = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini', min_samples_leaf=3, n_estimators=100, max_depth=3, random_state=123)
rf.fit(X_train, y_train)
X_train = df[['pclass','age','fare','sibsp','parch']]
X_test = X_test[['pclass','age','fare','sibsp','parch']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.30, random_state=123))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.30, random_state=123)
X_train = X_train[['pclass','age','fare','sibsp','parch']]
X_test = X_test[['pclass','age','fare','sibsp','parch']]
X_train.shape
X_test.shape
rf = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini', min_samples_leaf=3, n_estimators=100, max_depth=3, random_state=123)
rf.fit(X_train, y_train)
rf.feature_importances_
print(rf.feature_importances_)
X_train.columns
print(X_train.columns, rf.feature_importances_)
y_pred = rf.predict(X_train)
y_pred.head()
y_pred[0:10]
y_pred_proba = rf.predict_proba(X_train)
y_pred_proba[0:10]
rf.score(X_train, y_train)
confusion_matrix(y_train, y_pred)
print(classification_report(y_train, y_pred))
rf.score(X_test, y_test)
