Name: Gift Maghanga

Project Title: Supervised and Unsupervised Machine learning.

Project Description;

Supervised Machine Learning – This project uses Linear Regression to predict numerical values from the given data. The model learns from labelled training data to identify patterns, which it uses to make predictions.

Unsupervised Machine Learning - The unsupervised machine learning project uses K-Means Clustering to group unlabeled data into clusters. The algorithm identifies patterns and similarities in the data during training and uses them to group similar data points together.

Instractions for Installating dependencies

#step 1 - install python
#step 2 - use python to create virtual environment (venv)
python -m venv venv - terminal command
#step 3 - activate the venv
venv/Scripts/activate
#step 4 - install required libraries  i.e scikit-learn and matplotlib
pip install scikit-learn - terminal command
pip install matplotlib - terminal command
step 4 - installing requirements.txt and saving all installed packages in it
pip install -r requirements.txt
pip freeze > requirements.txt

RUNNING THE CODE
For supervised and unsupervised machine learning open the terminal and type;
python supervised_ml.py
python unsupervised_ml.py

THEORY QUESTIONS

1. What is supervised machine learning?

It is a type of machine learning where a computer uses given data and learns from training labeled data to do predictions.

2. What is unsupervised machine learning?

It is a type of machine learning where a computer uses given data and groups it into clusters to identify patterns and similarity of data during training and uses it to group similar data points together.

3. What is the difference between supervised and unsupervised learning?

Supervised learning uses labelled data to make predictions, while unsupervised learning uses unlabelled data to find patterns.

4. Why is Linear Regression considered supervised learning?

It learns from examples that contain both input data and known answers, such as study hours and marks.

5. Why is K-Means considered unsupervised learning?

It groups similar data points without needing predefined labels.

6. What is the difference between fit() and predict()?

fit() trains the model using data. predict() uses the trained model to make predictions.

7. Give two real-world applications of supervised learning and two of unsupervised learning.

Supervised learning - Predicting exam scores and Detecting spam emails.

Unsupervised learning - Grouping customers according to shopping habits and Grouping students according to academic performance.