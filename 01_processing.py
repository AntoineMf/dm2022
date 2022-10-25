import pandas as pd
import math

def removingChar(to_be_removed, sentence):
    for c in to_be_removed:
        sentence = sentence.replace(c, '').replace("'"," ")
    return sentence.split()
to_be_removed = ".,:?;\"!"
df=pd.read_json("../archive/yelp_academic_dataset_review.json",lines=True,nrows=100)
df["text"]=df["text"].str.lower()
df["text"]=df["text"].apply(lambda x: removingChar(to_be_removed,x))


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
print(words_tfIdf)