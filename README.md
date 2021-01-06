# Home Credict Risk Prediction | An end-to-end Machine Learning project

Credit-lending plays a significant role in the banking sector. But the increase in non-performing loans has made the banking sector face huge losses and also has an impact on the economy of the country or the world. Thus an existential problem for any Loan provider today is to find out the Loan applicants who are very likely to repay the loan. This way companies can avoid losses and incur huge profits. 

So in this project, we are going to take the loan applicant data provided by Home Credit and identify the applicants who are most likely to default using both Supervised and Unsupervised techniques.

## About Home Credit 

Home Credit Group is an international consumer finance provider which was founded in 1997 and has operations in 9 countries. Our responsible lending model empowers underserved customers with little or no credit history by enabling them to borrow easily and safely, both online and offline. 

Home Credit offers easy, simple and fast loans for a range of Home Appliances, Mobile Phones, Laptops, Two Wheeler's , and varied personal needs. 

Dataset link: https://www.kaggle.com/c/home-credit-default-risk/data

## Exploratory Data Analysis

Data Exploration is an open-ended process where we calculate statistics and make figures to find trends, anomalies, patterns, or relationships within the data. The goal of Data Exploration is to learn what our data can tell us. It generally starts out with a high level overview, then narrows in to specific areas as we find intriguing areas of the data. The findings may be interesting in their own right, or they can be used to inform our modeling choices, such as by helping us decide which features to use.

We use Label Encoding for any categorical variables with only 2 categories and One-Hot Encoding for any categorical variables with more than 2 categories.

## Supervised Learning Techniques

Algorithms used: <br>
Logistic regression <br>
Random Forest <br>
Extreme Gradient Boost

We have created base models without balancing the target class and then We have used SMOTE and Random OverSampler methods to balance the data.
XGBoost model balanced using Random OverSampler method gave better accuracy and ROC AUC score.

## Unsupervised Learning Technique (Anomaly Detection)

### Anomaly Detection

In data analysis, anomaly detection (also outlier detection) is the identification of rare items, events or observations which raise suspicions by differing significantly from the majority of the data.

Here the defaults being 8.07%, they act as an anomaly.

### Using Scikit-Learn library 

Algorithms used:  <br>
Isolation Forest  <br>
Local Outlier Factor  <br>
Principal Component Analysis (PCA)  <br>
Kernel Principal Component Analysis (Kernel PCA)


### Using Python Outlier Detection (PyOD) Toolkit library 

Algorithms used:<br>
k-nearest neighbors <br>
Isolation Forest<br>
Local Outlier Factor<br>
Clustering-Based Local Outlier Factor<br>
Principal Component Analysis <br>
Histogram-based Outlier Score<br>

### Deployment

Link: https://loan-default-prediction-by-kv.herokuapp.com/

## Built With
•	pandas - Pandas is used for data cleaning and analysis. Its features were used for exploring, cleaning, transforming and visualizing the data. Also Pandas is an open-source python package built on top of Numpy. <br>
•	numpy - Numpy adds support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.<br>
•	Matplotlib - Matplotlib work like MATLAB that helps in data visualization to makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.<br>
•	seaborn - Seaborn is also used for data visualization and it is based on matplotlib. It provides a high-level interface for attractive and informative statistical graphics.<br>
•	imblearn- imbalanced-learn is a python package offering a number of re-sampling techniques.<br>
•	Sklearn - Scikit-learn is a free machine learning library for the Python. It features various classification algorithms including Logistic regression, Random forest and XGBoost which were used in this project. It also helps in calculating the metrics such as classification report, accuracy score, f1 score, roc auc score and confusion matrix.<br>
•	Pyod - PyOD is a comprehensive and scalable toolkit for detecting outlying objects in multivariate data. This field is commonly referred as Outlier Detection or Anomaly Detection. PyOD includes more than 30 detection algorithms.
•	Flask - Flask is a lightweight Web Server Gateway Interface web application framework.<br>
•	sqlalchemy - SQLAlchemy is an open-source SQL toolkit and object-relational mapper for the Python programming language.<br>
•	logging - Python has a built-in logging module which allows writing status messages to a file. The file can contain the information on which part of the code is executed and what problems have been arisen.<br>
•	Jupyter Notebook - Jupyter exists to develop open-source software, open-standards, and services for interactive computing across dozens of programming languages.
