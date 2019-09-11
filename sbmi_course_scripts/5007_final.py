import json
import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET

"Q1"
# tree = ET.parse('xml_final_1.xml')
# root = tree.getroot()
# data_id=[]
# days=[]
# cost=[]
# death=[]
# all_data_l=[]
# for data_set in root.iter('dataset'):
#     unit_list=[]
#     unit_list.append(data_set.find('.//DataID').text)
#     if data_set.find('.//Days') !=None:
#         unit_list.append(data_set.find('.//Days').text)
#     if data_set.find('.//Cost')!=None:
#         unit_list.append(data_set.find('.//Cost').text)
#     if data_set.find('.//Death')!=None:
#         unit_list.append(data_set.find('.//Death').text)
#     all_data_l.append(unit_list)
# all_df=pd.DataFrame(all_data_l)
# no_null_df=all_df.dropna()
# print(no_null_df[0])

"Q2"
# in_df=pd.read_csv('csv_final_1.csv')
# sele_rows=in_df.loc[in_df['Glucose']>120]
# print('Data that has glucose value of greater than 120.0')
# print(sele_rows)
# print('Average of glucose values is ',sele_rows['Glucose'].mean())

"Q3"
# in_file_tree=ET.parse('xml_final_2.xml')
# in_root=in_file_tree.getroot()
# all_data_list=[]
# for data_set in in_root.iter('dataset'):
#     each_list=[]
#     each_list.append(data_set.find('.//DataID').text)
#     each_list.append(data_set.find('.//BP_Before').text)
#     each_list.append(data_set.find('.//BP_After').text)
#     all_data_list.append(each_list)
# all_array=np.array(all_data_list)
# for each in all_array:
#     print(each[0],int(each[1])-int(each[2]))

"Q4"

# in_file=np.genfromtxt("csv_final_2.csv",delimiter=",",filling_values=-1,autostrip=True,dtype=np.dtype(str))
# new_list=[]
# for rows in in_file[1:]:
#     if "NA" not in rows:
#         new_list.append(list(rows))
# print(np.array(new_list).size)

"Q5"
j_file=open('json_final_1.json','r').read()
j_data=json.loads(j_file)
Age=[]
BMI=[]
Systolic=[]
Glucose=[]
all_data_list=[]
final_result=[]
for each_data in j_data['Data']['Dataset']:
    Age.append(each_data['Age'])
    BMI.append(each_data['BMI'])
    Systolic.append(each_data['Systolic'])
    Glucose.append(each_data['Glucose'])
cal_array=np.array(all_data_list).astype(np.float)
all_df=pd.DataFrame({"Age":Age,"BMI":BMI,"Systolic":Systolic,"Glucose":Glucose},dtype=float)
mean=all_df.mean(axis=0)
#print(mean)
final_result.append(mean.tolist())
median=all_df.median(axis=0)
#print(median)
final_result.append(median.tolist())
mode=all_df.mode()
#print(mode.dropna().tolist())
mode_list=[]
for each in ['Age','BMI','Systolic','Glucose']:
    outlist=mode[each].dropna().tolist()
    print(each,' : ', ",".join(str(v) for v in outlist))
#     mode_list.append(mode[each].dropna().tolist())
# final_result.append(mode_list)
#final_result.append(all_df.std(axis=0))
print(all_df.std(axis=0))
# print('Age  ','BMI  ','Systolic ','Glucose')
# for result in final_result:
#     for each_result in result:
#         print(each_result,end=' ')
#     print('\n')


