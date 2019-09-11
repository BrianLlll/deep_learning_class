# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 14:13:53 2018

@author: libingrui
"""
import warnings
warnings.filterwarnings('ignore')
from mlp import BaseMLP,MLP
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler as SS
from sklearn.cross_validation import cross_val_score
from keras.utils import np_utils, generic_utils
from sklearn import preprocessing
def deep_drug():
#    data,label=make_moons(n_samples=500, noise=0.4)
#    data_s = SS().fit_transform(data)
#    print(data[1])
#    print(len(label))
    #print()
    with open (r'D:\work\DL_Predicting_Pharmacological\data\result_file\Paper_result\select_drug_nomesh.txt','r') as mesh_file:
        all_list=[]
        all_data=[]
        for mesh_lines in mesh_file:
            mesh_lines=mesh_lines.strip().split('\t')
            all_list.append(mesh_lines)
#    array_file=np.array(all_list)
    #for i in range(len(all_list)):
        #row_data.append()
    for i in range(1,len(all_list[3])):
        row_data=[float(x[i]) for x in all_list[3:]]
        #aprint(row_data)
        all_data.append(row_data)
    label=[]
    #all_data=pd.DataFrame(all_data)
    #print(all_data,type(all_data))
    #all_data=all_data.fillna(all_data.mean())
    all_data=np.array(all_data)
    #print(all_data,type(all_data))
    all_data=SS().fit_transform(all_data)
    #print(all_data,type(all_data))
    test_data=all_data[:15000]
    #test_data=preprocessing.scale(test_data)
    #print(test_data)
    with open(r'D:\work\DL_Predicting_Pharmacological\data\result_file\Paper_result\label_num.txt','r') as label_file:
        for label_line in label_file:
            label_line=label_line.strip()
            label.append(int(label_line))
    #label=np.array(label)
    outfile=(r'D:\work\DL_Predicting_Pharmacological\data\result_file\gctx\result_test.txt','w')
    non_label=label
    #label=np.squeeze(label)
    #print(len(np.unique(label)))
    label=np_utils.to_categorical(label)
    #data_s=SS().fit_transform(all_data)
#    plt.plot(data_s[np.where(label==2)[0],0],all_data[np.where(label==2)[0],1],'r.', label='Label = 0')
#    plt.plot(data_s[np.where(label==1)[0],0],all_data[np.where(label==1)[0],1],'b.', label='Label = 1')
##
#    plt.title('drugs')
#    plt.xlabel('Feature 1')
#    plt.ylabel('Feature 2')
#    plt.legend()
    #print(all_data)
    vali_data=all_data[15001:17001]
    #print(vali_data)
    test_label=label[:15000]
    #print(test_label)
    model=MLP(n_hidden=60,n_deep=3, l1_norm=0, l2_norm=2, drop=0.2, verbose=1, max_epoch=200,activation='relu',optimizer='Adam')
    
    #print('1')
    model.fit(test_data,test_label)
    #print('2')
    y=model.predict(vali_data)
    #print('3')
    #predict = np.argmax(y,axis=1)  #axis = 1是取行的最大值的索引，0是列的最大值的索引
    #inverted = encoder.inverse_transform([predict])
    #print(y)
    #model.pre
    #print(label[40000:40005])
    pre_label=[]
    for i in y:
        #print(i,type(i))
        i=list(i)
        pre_label.append(i.index(max(i)))
        #print(i.index(max(i)),'index')
        #for t in i:
            #print(t,'t')
        #print('-----')
    #print(pre_label,'predict')
    #print(non_label[10001:11001])
    c=0
    for i in range(len(pre_label)):
        if pre_label[i]==non_label[15001:17001][i]:
            c+=1
    print(c)
    print(c/len(pre_label),'rate')
        
        #print('\n',file=outfile)
    #print(y)
    #test_label=np_utils.to_categorical(test_label,13)
    #train.save(r'D:\work\DL_Predicting_Pharmacological\data\result_file\gctx\train_testout.txt')
    l=[0,1,2,3,4,5,6,7,8,9,10,11,12]
    #np.array(l)
    #print(y)
    #for i in y:
        
        #print(l[np.argmax(i,0)])
        
    #clf = MLP(n_hidden=40, n_deep=3, l1_norm=0, drop=0.1, verbose=1)
    #scores = cross_val_score(clf, all_data, label, cv=10, n_jobs=1, scoring='f1_weighted')
    #print(scores)
#    print(all_data,'  ',type(all_data))
#    print(label,'  ',type(label))
#                
    #n=MLP.
    
    
    
    
    
    
    
    
deep_drug()