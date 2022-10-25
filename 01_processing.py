import pandas as pd

def removingChar(to_be_removed, sentence):
    for c in to_be_removed:
        sentence = sentence.replace(c, '')
    return sentence.split()
to_be_removed = ".,:!"
df=pd.read_json("../archive/yelp_academic_dataset_review.json",lines=True,nrows=100)
df["text"]=df["text"].apply(lambda x: removingChar(to_be_removed,x))
print(df["text"].head())

