"""
Retrains the Logistic Regression model using the current scikit-learn version
and saves it as model.joblib. Run this once from the mysite/ directory:

    python retrain_model.py
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'Training.csv')
MODEL_PATH = os.path.join(BASE_DIR, 'model.joblib')

print("Loading training data...")
df = pd.read_csv(CSV_PATH)
print(f"  Shape: {df.shape}")
print(f"  Last 3 columns: {list(df.columns[-3:])}")

# Drop the junk unnamed trailing column if it exists
cols_to_drop = [c for c in df.columns if c.startswith('Unnamed')]
if cols_to_drop:
    df.drop(columns=cols_to_drop, inplace=True)
    print(f"  Dropped junk columns: {cols_to_drop}")

X = df.drop('prognosis', axis=1)
y = df['prognosis']

print(f"  Feature columns: {len(X.columns)}")
print(f"  Target classes: {y.nunique()}")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining Logistic Regression model...")
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"  Test Accuracy: {acc * 100:.2f}%")

joblib.dump(model, MODEL_PATH)
print(f"\nModel saved to: {MODEL_PATH}")
print("Done! You can now run: python manage.py runserver")
