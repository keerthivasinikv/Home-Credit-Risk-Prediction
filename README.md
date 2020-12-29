# Home Credict Risk Prediction | An end-to-end Machine Learning project

Credit-lending plays a significant role in the banking sector. But the increase in non-performing loans has made the banking sector face huge losses and also has an impact on the economy of the country or the world. Thus an existential problem for any Loan provider today is to find out the Loan applicants who are very likely to repay the loan. This way companies can avoid losses and incur huge profits. 

So in this project, we are going to take the loan applicant data provided by Home Credit and identify the applicants who are most likely to default using both Supervised and Unsupervised techniques.

## About Home credit 

Home Credit Group is an international consumer finance provider which was founded in 1997 and has operations in 9 countries. Our responsible lending model empowers underserved customers with little or no credit history by enabling them to borrow easily and safely, both online and offline. 

Home Credit offers easy, simple and fast loans for a range of Home Appliances, Mobile Phones, Laptops, Two Wheeler's , and varied personal needs. 

Dataset link: https://www.kaggle.com/c/home-credit-default-risk/data

## Exploratory Data Analysis

Data Exploration is an open-ended process where we calculate statistics and make figures to find trends, anomalies, patterns, or relationships within the data. The goal of Data Exploration is to learn what our data can tell us. It generally starts out with a high level overview, then narrows in to specific areas as we find intriguing areas of the data. The findings may be interesting in their own right, or they can be used to inform our modeling choices, such as by helping us decide which features to use.

We use Label Encoding for any categorical variables with only 2 categories and One-Hot Encoding for any categorical variables with more than 2 categories.

## Supervided Learning Techniques

Algorithms used: <br>
Logistic regression <br>
Random Forest <br>
Extreme Gradient Boost

I have created base models without balancing the target class and then I have used SMOTE and Random OverSampler methods to balance the target class.

XGBoost model balanced using Random OverSampler method gave better accuracy and ROC AUC score.

## Unsupervised Learning Technique (Anomaly Detection)

### Using Scikit-Learn library 

Algorithms used:  <br>
Isolation Forest  <br>
Local Outlier Factor  <br>
Principal Component Analysis (PCA)  <br>
Kernel Principal Component Analysis (Kernel PCA)

## Built With

Jupyter Notebook - Project Jupyter exists to develop open-source software, open-standards, and services for interactive computing across dozens of programming languages.
