import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

Ragas=pd.read_csv('data/61_Raga_Dataset.csv')
X=Ragas.drop(['Gayan Samay','is_Sandhi_Prakash','Raga'],axis=1)
Y=Ragas['Gayan Samay']
X=pd.get_dummies(X,columns=['Thaat','Vadi','Samvadi'])

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.25,random_state=2)

model=RandomForestClassifier(n_estimators=100,random_state=2)
model.fit(x_train,y_train)

from sklearn.metrics import accuracy_score
predictions=model.predict(x_test)
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predictions)

print(Y.value_counts())
print("Accuracy percentage:", accuracy * 100)
results = pd.DataFrame({
    'Actual': y_test,
    'Predicted': predictions
})

print(results)

from sklearn.metrics import accuracy_score

train_predictions = model.predict(x_train)
test_predictions = model.predict(x_test)

print("Training accuracy:",
      accuracy_score(y_train, train_predictions))

print("Testing accuracy:",
      accuracy_score(y_test, test_predictions))

from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import cross_val_score
cv=RepeatedStratifiedKFold(n_splits=3,n_repeats=20,random_state=42)

ref_model=RandomForestClassifier(n_estimators=100,random_state=2)


scores=cross_val_score(ref_model,X,Y,cv=cv,scoring='accuracy')
print(scores)
print(len(scores))
print(scores.mean())
print(scores.std())