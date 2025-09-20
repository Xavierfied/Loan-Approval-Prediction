Loan Approval Predictor
This repository contains a machine learning project focused on building and evaluating a predictive model for loan approval. The project's primary goal was to create an accurate and reliable model that could handle the common challenge of class imbalance in financial datasets. The analysis centers on a comparative study between Logistic Regression and Decision Tree Classification.

Key Findings & Model Comparison
The analysis was performed in two main stages, with the F1-Score as the key performance metric, as it is particularly effective for imbalanced datasets.

1. Logistic Regression with SMOTE
```
Initially, the project explored the impact of the SMOTE (Synthetic Minority Over-sampling Technique) on the Logistic Regression model's performance.

Model

F1-Score

Logistic Regression (Normal Data)

0.90

Logistic Regression (SMOTE Data)

0.91
```
The use of SMOTE resulted in a small but positive improvement in the F1-Score, showing its effectiveness in handling imbalanced data even in a relatively simple model.
# ___
2. Final Verdict: Decision Tree vs. Logistic Regression
```
The final stage directly compared the best performing Logistic Regression model (with SMOTE) against a Decision Tree model (also with SMOTE) to determine the optimal solution.

Model

F1-Score

Decision Tree (SMOTE Data)

0.96

Logistic Regression (SMOTE Data)

0.91
```

The Decision Tree model demonstrated significantly better performance, achieving a 0.96 F1-Score. This result proves that it is the superior choice for a real-world application, offering a substantial boost in predictive accuracy for identifying approved and non-approved loan applications.
# ___

