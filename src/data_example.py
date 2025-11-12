import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Load dataset
X, y = load_iris(return_X_y=True)

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Add feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# Train a simple logistic regression model on scaled data
model = LogisticRegression(max_iter=200)
model.fit(X_train_scaled, y_train)

# Predict and evaluate
predictions = model.predict(X_test_scaled)
acc = accuracy_score(y_test, predictions)
print(f"Accuracy: {acc:.2%}")

# Show confusion matrix
cm = confusion_matrix(y_test, predictions)
df_cm = pd.DataFrame(cm, index=load_iris().target_names, columns=load_iris().target_names)
print("\nConfusion Matrix:\n", df_cm)
