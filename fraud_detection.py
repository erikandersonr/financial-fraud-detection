import pandas as pd
import numpy as np

print("Loading...")
df = pd.read_csv("creditcard.csv")
if len(df) > 100000:
    df = df.sample(n=100000, random_state=42)
    print("Sampled to 100,000 rows for easier analysis")
print(f"Loaded {len(df)} transactions")

print("\nColumn names:")
print(df.columns.tolist())
print("\nFirst few rows:")
print(df.head())

print("\nMissing values per column:")
print(df.isnull().sum())

df = df.dropna(subset=["Amount", "Class"])
print(f"\nAfter dropping rows with missing Amount or Class: {len(df)} rows")

df = df[["Time", "Amount", "Class"]].copy()
df.columns = ["timestamp", "amount", "fraud_flag"]
print("\nKept columns: timestamp, amount, fraud_flag")

amount_pct = (df["amount"] - df["amount"].min()) / (df["amount"].max() - df["amount"].min() + 1e-6)
amount_score = np.clip(amount_pct * 5, 0, 5)
high_amount = (df["amount"] > df["amount"].quantile(0.95)).astype(int) * 3
df["risk_score"] = np.clip(np.round(amount_score + high_amount).astype(int), 0, 10)
print("Created risk_score (0-10): amount contributes 0-5, top 5% amounts add +3")

print("\n--- SUMMARY ---")
print("Fraud vs legitimate count:")
print(df["fraud_flag"].value_counts().to_string())
pct_fraud = 100 * df["fraud_flag"].mean()
print(f"\nFraud rate: {pct_fraud:.2f}%")

df["amount_category"] = pd.cut(df["amount"], bins=[0, 10, 50, 500, 1e6], labels=["low", "medium", "high", "very_high"])
print("\nFraud rate by amount category:")
print(df.groupby("amount_category", observed=True)["fraud_flag"].mean().mul(100).round(2).to_string())

print("\nAverage transaction amount:")
print(df.groupby("fraud_flag")["amount"].mean().to_string())

export_cols = ["amount", "fraud_flag", "risk_score", "timestamp", "amount_category"]
df[export_cols].to_csv("fraud_data_cleaned.csv", index=False)
print(f"\nExported {len(df)} rows to fraud_data_cleaned.csv")
