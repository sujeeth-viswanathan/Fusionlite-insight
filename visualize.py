import pandas as pd
import matplotlib.pyplot as plt

# Load features and predictions
df = pd.read_csv("features.csv", index_col=0)

# Load target column
df["Target"] = df["Return"].shift(-1).apply(lambda x: 1 if x > 0 else 0)
df = df.dropna(subset=["Target"])

# Get predictions from saved model (optional)
# Or re-run predictions inline for quick display
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = df[["MA5", "MA10", "Volatility5"]]
y = df["Target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
df["Predicted"] = model.predict(X)

# Plot actual vs predicted
plt.figure(figsize=(12, 5))
plt.plot(df.index[-50:], df["Target"].tail(50), label="Actual", marker='o')
plt.plot(df.index[-50:], df["Predicted"].tail(50), label="Predicted", marker='x')
plt.title("Actual vs Predicted Direction (Last 50 Days)")
plt.xlabel("Date")
plt.ylabel("Direction")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()
