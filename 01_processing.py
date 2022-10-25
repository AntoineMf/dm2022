import pandas as pd
import math

def removingChar(to_be_removed, sentence):
    for c in to_be_removed:
        sentence = sentence.replace(c, '').replace("'"," ")
    return sentence.split()
to_be_removed = ".,:?;\"!()"
df=pd.read_json("../archive/yelp_academic_dataset_review.json",lines=True,nrows=10000)
df["text"]=df["text"].str.lower()
df["text"]=df["text"].apply(lambda x: removingChar(to_be_removed,x))

business_id_dict={}
count=0
for i in df["business_id"]:
    print(i)
    if i in business_id_dict:
        pass
    else:
        df_tmp=df[df["business_id"]==i]
        wordCounting = {}
        for j in range(len(df_tmp.index)):
            for elem in df_tmp["text"].iloc[0]:
                if elem in wordCounting:
                    wordCounting[elem]+=1
                else:
                    wordCounting[elem]=1
        for word in wordCounting:
            wordCounting[word]=math.log(len(df_tmp.index)/wordCounting[word])
        business_id_dict[i]=wordCounting
        count+=1
    if count ==-1 : 
        break
    
business_review={}
for i in business_id_dict:
    print(i)
    words_tfIdf=dict(sorted(business_id_dict[i].items(), key=lambda item: item[1],reverse=True))
    business_review[i]=list(words_tfIdf)[0:5]

print(business_review)
print(count)
"""
for i in df["business_id"]:
    if i in business_id_dict:
        pass
    else:
        df_tmp=df[df["business_id"]==i]
        #wordCounting = {}
        for j in range(len(df.index)):
            for elem in df_tmp["text"].loc[j]:
                print(elem)
                #if elem in wordCounting:
                    #wordCounting[elem]+=1
                #else:
                    #wordCounting[elem]=1
        #business_id_dict[i]=wordCounting
#print(business_id_dict)
#print(df["text"].head())

#print(len(df.index))

wordCounting = {}
for j in range(len(df.index)):
    for i in df["text"].loc[j]:
        if i in wordCounting:
            wordCounting[i]+=1
        else:
            wordCounting[i]=1
#print(wordCounting)

for elem in wordCounting:
    wordCounting[elem]=math.log(len(df.index)/wordCounting[elem])
words_tfIdf=dict(sorted(wordCounting.items(), key=lambda item: item[1],reverse=True))
#print(words_tfIdf)"""