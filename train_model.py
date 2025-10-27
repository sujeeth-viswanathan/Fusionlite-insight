import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load features
df = pd.read_csv("features.csv", index_col=0)

# Target: 1 if next day's return > 0, else 0
df["Target"] = np.where(df["Return"].shift(-1) > 0, 1, 0)

# Drop last row (no label for last day)
df = df.dropna(subset=["Target"])

# Features to use
X = df[["MA5", "MA10", "Volatility5"]]
y = df["Target"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print(" Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
