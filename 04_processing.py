"""
KMEANS
"""
import pandas as pd
import math
import random
import numpy as np
import copy 



def euclidean(point, data):
    """
    Euclidean distance between point
    """
    return abs(point - data)

def average(lst):
    """
    Average of a clusters
    """
    return sum(lst) / len(lst)

def compare2list(p,old_p):
    return p-old_p

def k_means(stopping_value,cluster_nb):
    df=pd.read_json("../archive/yelp_academic_dataset_review.json",lines=True,nrows=100000)
    df["length_text"]=df["text"].str.len()
    df["text"]=df["text"].astype(str)
    list_review_unc=list(df["length_text"][:])
    
    list_review=[]
    p=[]
    
    for i in range(cluster_nb):
        list_review.append([])
        p.append(random.randint(0,5000))
    list_review.append(list_review_unc)
    list_updated=copy.deepcopy(list_review)
    #print(list_updated)
    stopMoving=False
    counter=0
    while(not stopMoving):
        counter+=1 
        for j in range(len(list_review)):
            for elem in list_review[j]:
                tmp_list=[]
                for indx in range(len(p)):
                    tmp_list.append(euclidean(p[indx],elem))
                tmp_value=elem
                list_updated[j].remove(tmp_value)
                list_updated[tmp_list.index(min(tmp_list))].append(tmp_value)
                
        if counter == 1:
            del list_review[3]
        if counter > 1 : 
            old_p=copy.deepcopy(p)
        else:
            old_p=[]
            for t in range(len(p)):
                old_p.append(0)
        for u in range(len(p)):
            try:
                p[u]=average(list_review[u])
            except:
                continue
        list_review=copy.deepcopy(list_updated)
        comparison_p=[]
        for h in range(len(p)):
            comparison_p.append(compare2list(p[h],old_p[h]))

        if average(comparison_p) < stopping_value :
            stopMoving=True

    print(list_updated)
    print(f"first cluster {list_updated[0]}")
    print(f"second cluster {list_updated[1]}")
    print(f"third cluster {list_updated[2]}")
    for i in range(len(p)):
        print(f"cluster {i} : {p[i]}, number of data inside the cluster {len(list_updated[i])}")
    print(f"Number of iteration : {counter}")
k_means(0.2,15)



