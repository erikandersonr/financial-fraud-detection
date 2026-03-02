# Credit Card Fraud Detection Dashboard

A beginner-friendly data analytics project: clean credit card transaction data in Python and build a fraud detection dashboard in Power BI.

## What this project does

- **Python:** Loads a public fraud dataset, cleans it, builds a simple risk score (0–10) from transaction amount, and exports a CSV ready for visualization.
- **Power BI:** Dashboard with fraud rate (card), fraud vs legitimate counts (bar), fraud over time (line), amount vs risk score (scatter), and breakdown by amount category (pie).

## Tech stack

- **Python 3** — pandas, numpy  
- **Power BI Desktop** — visuals and layout  
- **Data:** [Credit Card Fraud Detection (Kaggle, MLG-ULB)](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

## Quick start

1. **Clone the repo**
   ```bash
   git clone https://github.com/YOUR_USERNAME/financial-fraud-dash.git
   cd financial-fraud-dash
   ```

2. **Get the data**  
   Download [creditcard.csv](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) from Kaggle and place it in the project folder.

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the script**
   ```bash
   python fraud_detection.py
   ```
   This creates `fraud_data_cleaned.csv` in the same folder.

## Project structure

```
financial-fraud-dash/
├── README.md
├── PROJECT_GUIDE.md      # Detailed setup + Power BI steps + interview notes
├── fraud_detection.py    # Data load, clean, risk score, export
├── requirements.txt
└── creditcard.csv        # (you add this after downloading from Kaggle)
```

## Dataset

[Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) — European card transactions with a binary fraud label. The script samples to 100k rows and keeps: amount, fraud flag, timestamp, and adds a simple amount-based risk score and amount category for the dashboard.

## License

MIT. The Kaggle dataset has its own terms; use it according to Kaggle’s rules.
