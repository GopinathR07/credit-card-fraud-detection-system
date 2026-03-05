Machine Learning Algorithm Used
Logistic Regression

Logistic Regression is a supervised machine learning algorithm used for binary classification problems. It predicts the probability that a given input belongs to a particular class.

In this project, the model predicts whether a credit card transaction is:

0 – Legitimate Transaction
1 – Fraudulent Transaction

Unlike linear regression, logistic regression uses the sigmoid function to map predicted values into a probability between 0 and 1.

Sigmoid Function

The sigmoid function converts the linear output into a probability value.

Formula:
p(y=1) = 1 / 1 + e^-z
	​
Where:

P(y=1) = Probability of fraud

z = Linear combination of input features

If the probability is greater than a threshold (usually 0.5), the transaction is classified as fraud.

Otherwise, it is classified as normal.

Why Logistic Regression is Suitable for This Problem

Logistic regression works well when:

The target variable has two classes (fraud / not fraud)

The dataset is structured and numerical

We want probability outputs

Advantages of Logistic Regression:

Easy to interpret

Fast to train

Works well for large datasets

Produces probability scores

Limitations:

Cannot capture very complex relationships

Performance may decrease with highly non-linear data

Real World Use of Logistic Regression

Logistic regression is widely used in many industries.

Common applications include:

Fraud Detection
Spam Email Detection
Medical Disease Prediction
Customer Churn Prediction
Credit Risk Assessment

Companies such as Visa, Mastercard, and PayPal use machine learning models similar to this for fraud monitoring.

Mini Learning Note

Think of Logistic Regression like a probability calculator.

Example:

Transaction → Model analyzes features → Model outputs probability

Example output:

Fraud probability = 0.87

Since 0.87 > 0.5, the model predicts:

Fraudulent Transaction
