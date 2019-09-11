from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import numpy as np
from sklearn.preprocessing import StandardScaler as SS
from keras.utils import np_utils, generic_utils
def rf():
    X, y = make_classification(n_samples=1000, n_features=4,n_informative=2, n_redundant=0,random_state=0, shuffle=False)
    with open (r'D:\work\DL_Predicting_Pharmacological\data\result_file\Paper_result\random_data_notd.txt','r') as mesh_file:
        all_list=[]
        all_data=[]
        for mesh_lines in mesh_file:
            mesh_lines=mesh_lines.strip().split('\t')
            all_list.append(mesh_lines)
    label=[]
    all_data=np.array(all_list)
    all_data=SS().fit_transform(all_data)
    test_data=all_data[:16000]
    with open(r'D:\work\DL_Predicting_Pharmacological\data\result_file\Paper_result\random_label.txt','r') as label_file:
        for label_line in label_file:
            label_line=label_line.strip()
            label.append(int(label_line))
    non_label=label
    #label=np_utils.to_categorical(label)
    vali_data=all_data[17001:17368]
    test_label=label[:16000]
    clf = RandomForestClassifier(max_depth=35, random_state=0)
    clf.fit(test_data,test_label)
    y=clf.predict(vali_data)
    pre_label=[]
    #print(y)
    # for i in y:
    #     #i=list(i)
    #     pre_label.append(i.index(max(i)))
    print(y,'predict')
    print(non_label[17001:17368])
    c=0
    for i in range(len(y)):
        if y[i]==non_label[17001:17368][i]:
            c+=1
    print(c)
    print(c/len(y),'rate')



    #print(X,' ',y)





rf()
