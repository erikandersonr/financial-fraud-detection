# Financial Fraud Detection Dashboard — Project Guide

## STEP 1 — Get the Data

**Dataset:** Credit Card Fraud Detection (MLG-ULB)  
**Link:** https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud  

- Credit card transactions with a fraud label (Class: 0 = legitimate, 1 = fraud).
- About 284,000 rows; the script samples to 100,000 so it stays manageable.
- CSV, free, and widely used for learning.

**Download:**

1. Sign in to Kaggle (free account).
2. Open the dataset page and click **Download** (or the “Download” button on the right).
3. Unzip the downloaded folder.
4. Find **creditcard.csv** inside.
5. Move **creditcard.csv** into your project folder:  
   `Desktop/financial-fraud-dash/`  
   So the path is:  
   `Desktop/financial-fraud-dash/creditcard.csv`

**File to use:** `creditcard.csv`  
**Save location:** Same folder as `fraud_detection.py` (the project folder above).

---

## STEP 2 — Run the Python Script

In a terminal, from the project folder:

```bash
cd /Users/erikanderson/Desktop/financial-fraud-dash
python fraud_detection.py
```

The script will print columns, first rows, missing values, cleaning steps, summaries, and confirm that **fraud_data_cleaned.csv** was created. Use that CSV in Power BI.

---

## STEP 3 — Power BI Dashboard (Explicit Step-by-Step)

### 3.1 Import the data

1. Open **Power BI Desktop** (don’t use the browser; use the installed app).
2. On the **Home** tab of the ribbon (top), click **Get data**.
3. In the menu that opens, click **Text/CSV** (under “All” or “File”).
4. In the file picker, go to your project folder and select **fraud_data_cleaned.csv**. Click **Open**.
5. A preview window appears. At the bottom, click **Load** (not “Transform Data” unless you want to edit in Power Query).
6. On the **left side** of the window you’ll see three icons: Report, Data, Model. Click the **middle icon (Data)** to open Data view.
7. In the right-hand **Fields** pane, expand the table (click the arrow next to its name). You should see: **amount**, **fraud_flag**, **risk_score**, **timestamp**, **amount_category**. If you see those five columns, the data loaded correctly. Click back to the **Report** view (first icon) to build visuals.

---

### 3.2 Visual A — Card (total fraud %)

1. Click on the **white report canvas** (the big empty area in the middle) so nothing is selected.
2. On the **right**, find the **Visualizations** pane. It shows a grid of visual icons. Click the **Card** icon (a single large number in a rectangle). A blank card appears on the canvas.
3. In the **Fields** pane (right side, under Visualizations), find your table and **drag** the **fraud_flag** field into the **Fields** bucket that says **Value** (under “Build visual” or “Data”). If you don’t see “Value,” the card is selected and the well might be labeled “Value” or “Field.”
4. The card will probably show a number like 0.003. We want **average of fraud_flag** (that’s the fraud rate). Click the **chevron (▼)** or **dropdown** on **fraud_flag** in the Value well → choose **Average** (not Sum, not Count).
5. To show it as a **percentage**: with the card selected, open the **Format** pane (paint roller icon in the Visualizations area, or **Visualizations** → **Format your visual**). Expand **Value** (or “Callout value”). Set **Display units** to **None**, and **Value format** to **Percentage** with 2 decimal places (e.g. 0.35 %).
6. Optional: In Format, expand **Category label**, turn it **On**, and set the label text to **Fraud rate**.
7. Resize the card by dragging its corners so it’s a small rectangle (e.g. top-left of the canvas).

---

### 3.3 Visual B — Bar chart (fraud vs legitimate count)

1. Click on empty canvas again. In **Visualizations**, click **Clustered bar chart** (horizontal bars icon).
2. Drag **fraud_flag** from Fields into the **Y-axis** well (sometimes labeled “Axis” for a bar chart—the axis where 0 and 1 will show). If the Y-axis well says “Axis,” put fraud_flag there.
3. Click the **dropdown** on **fraud_flag** in the Y-axis well → select **Don’t summarize** (so you see “0” and “1” as categories, not a continuous axis).
4. Drag **fraud_flag** again from Fields into the **Values** well (or “Value”). In the Values well, click the dropdown on **fraud_flag** → choose **Count** (not Sum, not Average).
5. You should see two horizontal bars: one for 0 (legitimate) and one for 1 (fraud). Optional: In **Data view**, you can set the column to display “Legitimate” and “Fraud” via column formatting, or leave as 0/1.
6. With the visual selected: **Format** (paint roller) → **Title** → turn **On**, set title text to **Fraud vs legitimate transactions**. **Format** → **Data labels** → turn **On** so the count appears on each bar.
7. Place this visual to the right of the card (or below it).

---

### 3.4 Visual C — Line chart (fraud over time)

1. Click on empty canvas. In **Visualizations**, click **Line chart** (line icon).
2. Drag **timestamp** from Fields into **X-axis**.
3. Drag **fraud_flag** into **Y-axis**. In the Y-axis well, set **fraud_flag** to **Average** (so you see fraud rate over time).
4. If the line is too noisy (too many points): In the **Data** view, **Table tools** → **New column**, and create a column that groups time, e.g. `Hour = ROUNDDOWN(fraud_data_cleaned[timestamp] / 3600, 0)`. Then in the report, use **Hour** on the X-axis instead of **timestamp**.
5. **Format** → **Title** → On, title: **Fraud over time**.
6. Place this visual below the card and bar, or in a second row.

---

### 3.5 Visual D — Scatter (amount vs risk score, colored by fraud)

1. Click on empty canvas. In **Visualizations**, click **Scatter chart** (scatter dots icon).
2. Drag **amount** into **X-axis** (or “Details” if the scatter uses that).
3. Drag **risk_score** into **Y-axis**.
4. Drag **fraud_flag** into **Legend** (so points are colored by 0 vs 1).
5. **Format** → **Title** → On, title: **Amount vs risk score by fraud**.
6. Place next to or below the line chart.

---

### 3.6 Visual E — Pie chart (by amount category)

1. Click on empty canvas. In **Visualizations**, click **Pie chart**.
2. Drag **amount_category** into **Legend** (or “Details”).
3. Drag **fraud_flag** into **Values**. In the Values well, set **fraud_flag** to **Count** (count of transactions per category). Alternatively use **Sum of amount** to show total amount by category.
4. **Format** → **Title** → On, title: **Transactions by amount category** (or **Fraud by amount category** if you keep Count of fraud_flag).
5. Place where it fits (e.g. right of scatter or in a second column).

---

### 3.7 Make it look consistent

- **Legend colors (fraud = red, legit = green):** Select any visual that has **fraud_flag** in the Legend (bar, scatter, etc.). **Format** → **Data colors** (or **Legend**) → assign one color to the data value that means fraud (e.g. 1) and one to legitimate (e.g. 0). Use red/orange for fraud and green/blue for legitimate.
- **Dashboard title:** **Insert** tab (ribbon) → **Text box**. Type e.g. **Credit card fraud detection** and place at the top. Format font size (e.g. 18–24) and alignment.
- **Layout:** Drag visuals so they don’t overlap. Resize by selecting a visual and dragging the corners. Suggested layout: row 1 = Card + Bar; row 2 = Line + Scatter; row 3 or side = Pie.
- **Theme:** **View** tab → **Themes** → choose one (e.g. **Executive** or **Innovate**) so all visuals share the same style.

---

## STEP 3b — Prompt to paste into a Power BI helper (Copilot / AI)

Copy the block below and paste it into Power BI’s Copilot, or into any AI assistant that helps with Power BI, after you have loaded **fraud_data_cleaned.csv** into your report.

```
I have a Power BI report with one table loaded: fraud_data_cleaned. It has these columns:
- amount (numeric)
- fraud_flag (0 = legitimate, 1 = fraud)
- risk_score (0–10)
- timestamp (numeric, seconds)
- amount_category (text: low, medium, high, very_high)

I need to build a simple dashboard with exactly these 5 visuals. Give me step-by-step instructions for each, as if I’m a beginner:

1. Card visual: Show the overall fraud rate as a percentage (average of fraud_flag, formatted as percentage, 2 decimals). Label it "Fraud rate".

2. Clustered bar chart: Y-axis = fraud_flag (don’t summarize, so I see 0 and 1). Values = Count of fraud_flag. Title: "Fraud vs legitimate transactions". Data labels on.

3. Line chart: X-axis = timestamp (or a binned time column if needed). Y-axis = Average of fraud_flag. Title: "Fraud over time".

4. Scatter chart: X-axis = amount, Y-axis = risk_score, Legend = fraud_flag (color points by fraud vs legit). Title: "Amount vs risk score by fraud".

5. Pie chart: Legend = amount_category, Values = Count of fraud_flag. Title: "Transactions by amount category".

Use simple formatting only (no DAX). Tell me exactly which pane to use (Visualizations, Fields, Format) and what to drag where. For the card, remind me to set the Value summarization to Average and the value format to Percentage.
```

---

## STEP 4 — Interview Talking Points

- For this project, I took a public credit card dataset, cleaned it in Python with pandas, built a simple risk score from transaction amount, and then built a dashboard in Power BI to show fraud rate, counts, and patterns so I could explain the results clearly.

- I chose financial fraud detection because I wanted something that connects economics and data: real-world impact, clear labels, and a story I could tell in an interview without needing heavy statistics.

- The most challenging part was deciding what to keep in the cleaned dataset and how to define a simple risk score that was easy to explain—I went with amount-based logic so I could describe it in one sentence.

- From the data, I found that [fill with your result: e.g. fraud rate is under 1%, or that higher amount categories had a different fraud rate, or that average fraud transaction size differed from legitimate ones]—I’ll point to the exact numbers from my dashboard.

- This project taught me how to go from raw CSV to a clear story: load and explore, clean and add one feature, summarize, then visualize so someone can see the main message at a glance.

---

## STEP 5 — What the Data Might Show

**Typical fraud rate**  
In this dataset, fraud is usually well under 1% of transactions (often around 0.1–0.3%). That’s normal for real card data and is why we look at rates and patterns, not just counts.

**Patterns to look for**  
- Fraud vs legitimate **counts** (heavily skewed to legitimate).  
- **Average amount** for fraud vs legit (sometimes fraud is smaller and more frequent, or the opposite, depending on the data).  
- **Fraud rate by amount category** (e.g. “very_high” might have a different rate).  
- **Amount vs risk score**: higher amounts and higher risk scores; fraud points may cluster in certain regions of the scatter.

**Simple risk score explanation**  
“I built a 0–10 risk score in Python. Most of the score comes from the transaction amount—higher amounts get a higher score. I also added extra points for transactions in the top 5% by amount, because very large transactions are often worth flagging. So it’s a simple, explainable rule: bigger transactions and unusually large ones get a higher risk number.”

**One insight you can mention**  
“When I broke it down by amount category, I saw that [e.g. very_high amount had a different fraud rate than low], which suggests that amount is a useful signal for prioritization—and I could explain that using the dashboard.”

---

## Deliverables Checklist

1. **fraud_detection.py** — Run with `creditcard.csv` in the same folder; produces `fraud_data_cleaned.csv`.
2. **Power BI** — Import `fraud_data_cleaned.csv` and build the 5 visuals above.
3. **Talking points** — Use the bullets in Step 4 and fill in your actual numbers from the dashboard.
4. **Expected insights** — Use Step 5 to prepare for “what did you learn?” and “how does the risk score work?”.

Keep the story simple: you got data, cleaned it, added one interpretable feature, summarized it, and built a dashboard to communicate the results.
