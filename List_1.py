# Data Structure: LIST denoted with square brackets
li=[1,'a', 23, 11, 'ank', True]
print (li[3])

# List Slicing
'''Everytime we do slicing, a new list is made in teh memory'''
'''there are few methods like insert, append,extend, remove--> all these methods modfies the list IN PLACE
(which means, no new list is created) '''
'''Adding--> append, insert and extend methods
Removing --> pop, remove and clear'''

# print(li[0:6:3])  # li[start(starts with 0,1,2..) : end(starts with 1,2,3,4...) : skip]

# List is immutable and we can have Methods on lists
#1. List inplace value change
li1=['an','frd',23,11,7]

#adding
li2=li1.append(20)
print(li2) # o/p = None because append fuc. changes the value inplace it doesn't return a value
li1.append(20)
li2=li1
print(li2)
li1.insert(1, 30) #'(a,b)--> a is index and b is the no. inserted at that index'
print(li1)

# Removing
li1.pop(2) # index at which the item is popped
print(li1)
li1.pop() # last item is removed firm the list
print(li1)

li1.remove(2) #item present at that index is removed
print(li1)

li1.clear() # it clears the list
print (li1)
'12-38 remove the comment'

# Index
li=[1,'a', 23, 11, 'ank', True]
print(li.index('ank'))  # (value, start , stop)
#print(li.index('ank',0,3)) # 0,3 gives the range where the index method will look for the value True and this will give an error

# sort method
li3=[99,8,0,33,2,85]
li3.sort()
'sort --> method which sort the list in place it doesnt produce new list'
print(li3.sort()) # o/p--> None
print(li3) # it will give a sorted list

# Sorted function
'this funct. creates a new sorted list'
new_li3=li3.copy()
print(sorted(new_li3))

#nested List
list= [[1,2,'a'], 'a', 'b' , "hi"]
print(a)



import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the training data
train_data = pd.read_csv("train.csv")

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Convert the text data into feature vectors
X_train = vectorizer.fit_transform(train_data['title1 en'] + ' ' + train_data['title2 en'])
y_train = train_data['label']

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Load the validation data
val_data = pd.read_csv("val.csv")

# Convert the validation data into feature vectors
X_val = vectorizer.transform(val_data['title1 en'] + ' ' + val_data['title2 en'])
y_val = val_data['label']

# Evaluate the model on the validation data
y_pred = model.predict(X_val)
accuracy = accuracy_score(y_val, y_pred)

print("Validation accuracy:", accuracy)
