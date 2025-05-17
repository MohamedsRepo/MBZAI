import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os
print("Current folder:", os.getcwd())
print("Files here:", os.listdir())



#load the dataset
df = pd.read_csv("data\dementia_data.csv")

print(df.head())
print(df.info())

# Drop rows with missing MMSE or SES
df = df.dropna(subset=["MMSE", "SES"])

# Drop irrelevant columns
df = df.drop(columns=["MRI ID", "Visit", "Hand", "Subject ID"], errors='ignore')

# Use CDR to create a binary dementia label
# If CDR >= 0.5, label as demented (1), else non-demented (0)
df = df.dropna(subset=["MMSE", "SES", "CDR"])
df["Dementia"] = df["CDR"].apply(lambda cdr: 1 if cdr >= 0.5 else 0)

#decide which columns are useful to use as features
X = df[["Age", "Educ", "MMSE", "eTIV", "nWBV", "SES"]]
y = df["Dementia"]

#train-test split the data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Report:\n", classification_report(y_test, y_pred))

# Train model
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "dementia_model.pkl")
print("✅ Model saved successfully!")

