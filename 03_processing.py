import pandas as pd
import math
import random


def substract(value1,value2,output):
    return abs(value1-value2) 
        

def createCluster(nb):
    listCluster=[]
    for i in range(nb):
        listCluster.append([])
    return listCluster

df=pd.read_json("../archive/yelp_academic_dataset_review.json",lines=True,nrows=100)
df["length_text"]=df["text"].str.len()
df["text"]=df["text"].astype(str)
list_review=list(df["text"][:])
#print(list_review)
#print(min(list_review,key=len))

clusters=[list_review]
value=0


while len(clusters)!=3:
    min=500
    min1=0
    min2=0
    for i in range(100):
        doubleList1=True
        doubleList2=True
        tmp1_index=random.randint(0,len(clusters)-1)
        tmp2_index=random.randint(0,len(clusters)-1)
        while (tmp2_index==tmp1_index):
            tmp2_index=random.randint(0,len(clusters)-1)
        try:
            tmp1_second_index=random.randint(0,len(clusters[tmp1_index])-1)
            tmp1=clusters[tmp1_index][tmp1_second_index]
        except:
            doubleList1=False    
            tmp1=clusters[tmp1_index]
        else:
            try:
                tmp2_second_index=random.randint(0,len(clusters[tmp2_index])-1)
                tmp2=clusters[tmp2_index][tmp2_second_index]
            except:
                doubleList2=False
                tmp2=clusters[tmp2_index]
            else:
                if(substract(tmp1,tmp2) < min):
                    min=substract(tmp1,tmp2)
                    doubleList1Final=doubleList1
                    doubleList2Final=doubleList2

                    if doubleList1:
                        min1=[tmp1,tmp1_index,tmp1_second_index]
                    else:
                        min1=[tmp1,tmp1_index]
                    if doubleList2:
                        min2=[tmp2,tmp2_index,tmp2_second_index]
                    else:
                        min2=[tmp2,tmp2_index]
    if not doubleList1Final:
        clusters[tmp1_index]=[clusters[tmp1_index]]
    clusters[min1[1]].append(min2[0])
    
    if doubleList2Final:
        del clusters[min2[1]][min[2]]
    else:
        del clusters[min2[1]]
        
    print(clusters)
print(clusters)