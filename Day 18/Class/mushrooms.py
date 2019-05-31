"""
Import mushrooms.csv file

This dataset includes descriptions of hypothetical samples corresponding to 
23 species of gilled mushrooms in the Agaricus and Lepiota Family Mushroom 
drawn from The Audubon Society Field Guide to North American Mushrooms (1981). 
Each species is identified as definitely edible, definitely poisonous, or of 
unknown edibility and not recommended. This latter class was combined with 
the poisonous one.

 

Attribute Information:

classes: edible=e, poisonous=p (outcome)

cap-shape: bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s

cap-surface: fibrous=f,grooves=g,scaly=y,smooth=s

cap-color: brown=n, buff=b,cinnamon=c,gray=g,green=r,pink=p,purple=u,red=e,
           white=w,yellow=y

bruises: bruises=t, no=f

odor: almond=a,anise=l,creosote=c,fishy=y,foul=f,musty=m,none=n,pungent=p
      ,spicy=s

gill-attachment: attached=a,descending=d,free=f,notched=n

gill-spacing: close=c,crowded=w,distant=d

gill-size: broad=b,narrow=n

gill-color: black=k,brown=n,buff=b,chocolate=h,gray=g,

green=r,orange=o,pink=p,purple=u,red=e,white=w,yellow=y

stalk-shape: enlarging=e,tapering=t

stalk-root: bulbous=b,club=c,cup=u,equal=e,rhizomorphs=z,rooted=r,missing=?

stalk-surface-above-ring: fibrous=f,scaly=y,silky=k,smooth=s

stalk-surface-below-ring: fibrous=f,scaly=y,silky=k,smooth=s

stalk-color-above-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e
                        ,white=w,yellow=y

stalk-color-below-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,
                         red=e,white=w,yellow=y

veil-type: partial=p,universal=u

veil-color: brown=n,orange=o,white=w,yellow=y

ring-number: none=n,one=o,two=t

ring-type: cobwebby=c,evanescent=e,flaring=f,large=l,none=n,pendant=p,
           sheathing=s,zone=z

spore-print-color: black=k,brown=n,buff=b,chocolate=h,green=r,orange=o,
                   purple=u,white=w,yellow=y

population: abundant=a,clustered=c,numerous=n,scattered=s,several=v,solitary=y

habitat: grasses=g,leaves=l,meadows=m,paths=p,urban=u,waste=w,woods=d

    
Perform Classification on the given dataset to predict if the mushroom is 
edible or poisonous w.r.t. it’s different attributes.

(you can perform on habitat, population and odor as the predictors)

Check accuracy of the model.

file_name - "mushrooms.py"

"""

import pandas as pd
import numpy as np
data = pd.read_csv("mushrooms.csv")
x = data.iloc[:,[5,-2,-1]].values
y = data.iloc[:,0].values
             
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
le = LabelEncoder()
y = le.fit_transform(y)
for i in range(len(x[0])):
    x[:,i] = le.fit_transform(x[:,i])

col_to_ohe = [0,1,2]  # Columns to be OneHotEncoded
ohe=OneHotEncoder(categorical_features=[col_to_ohe])
x = ohe.fit_transform(x).toarray()

# Getting indexes for the columns to be dropped, to avoid dummy variable trap
new_cols = [5,-2,-1] # in case the order of column is not same as dataset
total_col, indexes = 0, []
for col in new_cols:
    unique_val_count = len(data.iloc[:,col].value_counts())
    total_col += unique_val_count
    indexes.append(total_col - unique_val_count)

# Dropping the dummy variable trap columns
x = np.delete(x, indexes, axis=1)

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.25,random_state=0)

from sklearn.neighbors import KNeighborsClassifier
clas = KNeighborsClassifier(n_neighbors=5, p=2)
clas.fit(xtrain,ytrain)
pred = clas.predict(xtest)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(ytest,pred)

print ("Model Score : "+str(round(clas.score(xtest,ytest),3)*100)+"%")