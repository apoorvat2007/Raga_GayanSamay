# Can a rule-based Hindustani music theory function beat or match ML at predicting raga samay, and where do both fail?

**Exploratory Data Analysis(EDA) to know the effect of each parameter on Gayan Samay:**
 
 *Thaat vs Gayan Samay*

<img width="509" height="131" alt="image" src="https://github.com/user-attachments/assets/15782765-4cdc-4cab-a119-ba91b9e2f19a" />
 
 This is the crosstab evaluation of the raga thaats and their prahars. This was to check and cross-verify how common scales determine any Ragas gayan samay.

**Functions (Algorithm) made by me using rules of Pandit Bhatkahnde's Raga Samay Theory** 

rules.py (version 1): if else logic,has bad accuracy. Accuracy of this ver.= 13.114754098360656 %

<img width="187" height="121" alt="image" src="https://github.com/user-attachments/assets/2b4df89a-43ce-40e9-b44b-df1e3be21ba8" />

rules.py (version 2): tightened the "and" and "or" logic in if else statements. Accuracy increase noted +6.67

<img width="125" height="16" alt="image" src="https://github.com/user-attachments/assets/82835216-6117-4958-896a-ca25c9ae18a1" />

