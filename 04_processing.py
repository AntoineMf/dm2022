"""
KMEANS
"""
import pandas as pd
import math
import random
import numpy as np


def euclidean(point, data):
    """
    Euclidean distance between point
    """
    return point - data

def average(lst):
    """
    Average of a clusters
    """
    return sum(lst) / len(lst)

def k_means():
    df=pd.read_json("../archive/yelp_academic_dataset_review.json",lines=True,nrows=100000)
    df["length_text"]=df["text"].str.len()
    df["text"]=df["text"].astype(str)
    list_review=list(df["length_text"][:])
    list_review=[[],[],[],list_review]
    p=[df["length_text"].quantile(0.5)-50,df["length_text"].quantile(0.5),df["length_text"].quantile(0.5)+50]
    list_updated=list_review.copy()

    for i in range(5):
        print(list_updated)
        for j in range(len(list_review)):
            for elem in list_review[j]:
                tmp_list=[euclidean(p[0],elem),euclidean(p[1],elem),euclidean(p[2],elem)]
                tmp_value=elem
                list_updated[j].remove(tmp_value)
                list_updated[tmp_list.index(min(tmp_list))].append(tmp_value)
            
        if i == 1:
            del list_review[3]  
        for u in range(len(p)):
            try:
                p[u]=average(list_review[u])
            except:
                continue
        list_review=list_updated
    print(list_updated)
    print(f"first cluster {list_updated[0]}")
    print(f"second cluster {list_updated[1]}")
    print(f"third cluster {list_updated[2]}")
    print(f"first point {p[0]}, number of data inside the cluster {len(list_updated[0])}")
    print(f"second point {p[1]}, number of data inside the cluster {len(list_updated[1])}")
    print(f"third point {p[2]}, number of data inside the cluster {len(list_updated[2])}")

k_means()



