from sklearn.datasets import load_iris
import xgboost as xgb
from xgboost import plot_importance
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score   # 准确率
import numpy as np
from sklearn.preprocessing import StandardScaler as SS
#from keras.utils import np_utils, generic_utils
# 加载样本数据集
# iris = load_iris()
# X,y = iris.data,iris.target
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234565) # 数据集分割
# print(y_train,'2222')
# dt=np.loadtxt(r'/Users/libingrui/Desktop/Work_file/Data/0610_path_data.txt',dtype=np.float32)
# label = np.loadtxt(r'/Users/libingrui/Desktop/Work_file/Data/0610_label.txt',dtype=np.int32)
label=[]
with open (r'/Users/libingrui/Desktop/Work_file/Data/0610_path_data.txt','r') as mesh_file:
        all_list=[]
        all_data=[]
        for mesh_lines in mesh_file:
            mesh_lines=mesh_lines.strip().split('\t')
            all_list.append(mesh_lines)
with open(r'/Users/libingrui/Desktop/Work_file/Data/0610_label.txt','r') as label_file:
        for label_line in label_file:
            label_line=label_line.strip()
            label.append(int(label_line))
# X=dt
# y=label
all_data=np.array(all_list)
all_data=SS().fit_transform(all_data)
#label=np_utils.to_categorical(label)
X_train=all_data[:3000]
X_test=all_data[30001:3985]
y_train=label[:3000]
y_test=label[3001:3985]
#print(y_train)
# 算法参数
params = {
    'booster': 'gbtree',
    'objective': 'multi:softmax',
    'num_class': 6,
    'gamma': 0.1,
    'max_depth': 6,
    'lambda': 2,
    'subsample': 0.7,
    'colsample_bytree': 0.7,
    'min_child_weight': 3,
    'silent': 1,
    'eta': 0.1,
    'seed': 1000,
    'nthread': 4,
}

plst = params.items()


dtrain = xgb.DMatrix(X_train, y_train) # 生成数据集格式
# print('11111111')
num_rounds = 500
model = xgb.train(plst, dtrain, num_rounds) # xgboost模型训练

# 对测试集进行预测
dtest = xgb.DMatrix(X_test)
y_pred = model.predict(dtest)

# 计算准确率
accuracy = accuracy_score(y_test,y_pred)
print("accuarcy: %.2f%%" % (accuracy*100.0))
