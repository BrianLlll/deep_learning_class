import pickle
import xgboost as xgb

import numpy as np
from sklearn.model_selection import KFold, train_test_split, GridSearchCV
from sklearn.metrics import confusion_matrix, mean_squared_error
from sklearn.datasets import load_iris, load_digits, load_boston

dt=np.loadtxt(r'/Users/libingrui/Desktop/Work_file/Data/0610_path_data.txt',dtype=np.float32)
label = np.loadtxt(r'/Users/libingrui/Desktop/Work_file/Data/0610_label.txt',dtype=np.int32)
#rng = np.random.RandomState(31337)
print("Iris: multiclass classification")
iris = load_iris()
#print(iris)
#y = iris['target']
#print(y,'y')
#X = iris['data']
#print(X,'X')
X=dt
y=label
#print(y)
kf = KFold(n_splits=2, shuffle=False)
outfile=open(r'/Users/libingrui/Desktop/Work_file/Results/0610_results_6cla.txt','w')
for train_index, test_index in kf.split(X):
    #print(train_index)
    #print(len(train_index),train_index,'train')
    #print(len(test_index),test_index,'test')
    xgb_model = xgb.XGBClassifier().fit(X[train_index],y[train_index])
    predictions = xgb_model.predict(X[test_index])
    actuals = y[test_index]
    n=0
    for i in range(len(actuals)):
        outfile.write(str(actuals[i])+'\t'+str(predictions[i])+'\n')
        if actuals[i]==predictions[i]:
            n+=1
    print(len(actuals),len(predictions))
    print(n/len(actuals))
    print(actuals,'act')
    print(predictions,'pre')
    #print(confusion_matrix(actuals, predictions))


#xgb()
