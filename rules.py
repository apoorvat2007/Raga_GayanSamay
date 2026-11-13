import pandas as pd
ragas=pd.read_csv('data/61_Raga_Dataset.csv')
purvanga=['Sa','Re_komal','Re_shuddha','Ga_komal','Ga_shuddha','Ma_shuddha','Sa_taar']
def gayan_samay_predictor(row):
    #dividing into 3 main categories
    category=None
    predicted_prahar=None
    if (row['Re_komal']==1) or (row['Dha_komal']==1) and ((row['Ga_komal']==0) or (row['Ni_komal']==0)) :
        category=1 #sandhiprkash
    elif ((row['Re_shuddha']==1) or (row['Dha_shuddha']==1))and (row['Ga_komal']==0):
        category=2 #7 to 10 pm or am
    elif (row['Ga_komal']==1) and (row['Ni_komal']==1):
        category=3 #10 to 4 am pm

    #checking the 12 hour division using purvanga and uttarangavadi 
   
    if row['Vadi'] in purvanga:
        night_to_noon=1
    else:
        night_to_noon=0

   #categorizing into prahars now
 
    if night_to_noon == 1:#for raga gayan samay falling between 12am to 12pm
        if category== 1 and row['Ma_shuddha'] == 1:
            predicted_prahar = "din_1"
        elif category == 1 and (row['Ma_teevra'] == 1 or row['Ma_shuddha'] == 0):
            predicted_prahar = "ratri_4"
        elif category== 2 and row['Ma_shuddha'] == 1:
            predicted_prahar = "din_2"
        elif category == 3 and row['Ma_shuddha'] == 1:
            predicted_prahar = "ratri_3"
            
    
    elif night_to_noon == 0:#for raga gayan samay falling between 12pm to 12am
        if category == 3 and row['Ma_shuddha'] == 1 and row['Ma_teevra'] == 0:
            predicted_prahar = "din_3"
        elif category== 3 and row['Ma_teevra'] == 1:
            predicted_prahar = "din_4"
        elif category== 1 and row['Ma_teevra'] == 1:
            predicted_prahar = "ratri_1"
        elif category== 2 and row['Ma_teevra'] == 1:
            predicted_prahar = "ratri_2"
            
    return predicted_prahar

ragas['Rule_Prediction']=ragas.apply(gayan_samay_predictor,axis=1)
for i in range(len(ragas)):
    raga=ragas.iloc[i]['Raga']
    actual=ragas.iloc[i]['Gayan Samay']
    prediction=ragas.iloc[i]['Rule_Prediction']
    if actual==prediction:
        result='correct'
    else:
        result='wrong'
    print(raga,actual,prediction,result)


correct = 0

for i in range(len(ragas)):

    if ragas.iloc[i]['Gayan Samay'] == ragas.iloc[i]['Rule_Prediction']:
        correct += 1

accuracy = correct / len(ragas)

print("Accuracy:", accuracy * 100, "%")