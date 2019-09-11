# class UTE:
#     def __init__(self,name,etype):
#         self.name=name
#         self.etype=etype
#     def getAddress():
#         return "Houton,TX"
#     def getSalary(self):
#         return "$32000"
# class Ad(UTE):
#     def __init__(self,dept,join,name,etype):
#         UTE.__init__(self,name,etype)
#         self.dept=dept
#         self.join=join
#     def getDept(self):
#         return self.dept
# new_emp=Ad("OTM","1 sept 2012","john doe","admin")
# # print('1')
#print(new_emp.getDept())
#print(new_emp.getDept())
#print(self.dept)
#print(new_emp.getAddress())
#print(UTE.getSalary())
#print(new_emp.getSalary()) 
# #Ad.getSalary() 
# #Ad.getAddress()
# print(new_emp.getDept())
# import csv

# cfile=open(r'/Users/libingrui/Desktop/Work_file/5007.csv')
# cdata=csv.reader(cfile,delimiter=',',quotechar='"')
# for rows in cdata:
#     print(rows[1])
# cdata=csv.DictReader(cfile)
# i=0
# output=''
# for rows in cdata:
#     output=rows['index']
#     if i>3:
#         break
#     i+=1
# print(int(float(output)))
# A=[5,6,8,9]
# A.push(10)
# print(A)
# import numpy as np
# # a=np.array([[[1],[2],[3],[4]],[[5],[6],[7],[8]]])
# # b=np.array([0,1,2,3])
# # print(b.size)
# c=np.array(
#     [
#         [0,1,2,3,4,5],
#         [10,11,12,13,14,15],
#         [20,21,22,23,24,25]     ] )
# print(c[0:1,2:3])
#test="ATGCATGC"
#new=test[-3]+test[3]
#new1=test.replace("GC","U")
#print(new1)
#a='ABB'
#print(a.lower())
#b=['','a','f','']
#b.remove('')
#print(filter(None,b))
#b='aBB'
#print(a==b)

# class fra:
#     def __init__(self,num,den):
#         self.num=num
#         self.den=den
#     def __add__(self,newFra):
#         new_num=(self.num*newFra.den)+(newFra.num*self.den)
#         new_den=(self.den*newFra.den)
#         return fra(new_num,new_den)
# f1=fra(1,2)
# f2=fra(2,3)
# f3=f1+f2
# print(f3.num)
# A=[6,4,5,2,3,1]
# i=0
# t=0
# while i<len(A):
#     j=len(A)-1
#     while j>i:
#         cnum=A[j]
#         if A[j]<A[j-1]:
#             A[j]=A[j-1]
#             A[j-1]=cnum
#             print(A[j],A[j-1],cnum,'ajc')
#         #print(A)
#         j=j-1
#         t+=1
#         print(t,'t')
#     i=i+1
#     print(i,'i')
# import numpy as np
# a=np.array([0,1,2,3])
# print(a.size)
import re
# regex=r"\d+ days|months|years"
# match=re.search(regex,"Patient has cough for past 10 days")
# #print(match)
# print(match.group(0))
# regex=r"[a-zA-Z]+ \d+"
# matches=re.findall(regex,"June 24, August 9, Dec 12")
# print(matches[1])
#regex=r"([a-zA-Z]+)(\d+)"
#match=re.search(regex,"June 24")
# print(match,"match")
#print(match.group(1))
# text="ttgctagtgtgt"
# regex=r"t[gc]+t"
# pattern=re.compile(regex)
# result=pattern.findall(text)
# print(result)
# for i in [1,2,3]:
#     continue
# print(i)
#print(int(float(0.98)))
#1. The parent nodes is always bigger than children nodes.
#2. The left children node is not always bigger than right children node from same parent.
#We can use the heap tree to sort the blood pressure value of all patients in one hospital and then find the smallest one.

import pandas as pd
df=pd.DataFrame({"A":[1,2,3,4,5,6],"B":[5,10,15,20,25,30],"C":[2,4,6,8,10,12],"D":[10,20,30,40,50,60]})
print(df[(df["B"]/2==0)])