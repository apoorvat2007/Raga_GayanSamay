import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

Ragas=pd.read_csv('data/61_Raga_Dataset.csv')
train=Ragas.drop(['Gayan Samay','is_Sandhi_Prakash','Raga'],axis=1)
test=Ragas['Gayan Samay']
train=pd.get_dummies(train,columns=['Thaat','Vadi','Samvadi'])

x_train,x_test,y_train,y_test=train_test_split(train,test,test_size=0.25,random_state=2)

model=RandomForestClassifier(n_estimators=100,random_state=2)
model.fit(x_train,y_train)

from sklearn.metrics import accuracy_score
predictions=model.predict(x_test)
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)
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