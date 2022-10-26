import pandas as pd
import math


df=pd.read_json("../archive/yelp_academic_dataset_review.json",lines=True,nrows=100)
df["length_text"]=df["text"].str.len()
df["text"]=df["text"].astype(str)
list_review=list(df["text"][:])
#print(list_review)
#print(min(list_review,key=len))

clusters=[list_review]
value=0
while len(clusters)!=3:
    
    for i in range(len(clusters[0])):
        for j in range(len(clusters)):
            for k in range(len(clusters[j])):
                if (len(clusters[j][k])-len(clusters[0][i])==value):
                    clusters[0].append(clusters[j][k])
                    del clusters[j][k]
    value+=1