# 🛍️ E-commerce Return Rate Reduction Analysis

## 📌 Objective
This project aims to analyze and reduce the product return rate in an e-commerce environment. The focus is on identifying key factors behind returns across product categories, regions, and marketing channels and building a predictive model to flag high-risk products.

---

## 🧰 Tools & Technologies
- **Python** (Pandas, NumPy, Scikit-learn)
- **Power BI**
- **SQL**

---

## 📊 Project Pipeline

### 1. Data Cleaning
- Cleaned orders and returns datasets
- Merged relevant tables, removed duplicates, and handled null values

### 2. Exploratory Data Analysis
- Analyzed return rates by:
  - Product Category
  - Supplier
  - Geographic Region
  - Marketing Channel

### 3. Predictive Modeling
- **Logistic Regression** to predict the probability of a product being returned
- Evaluated using Accuracy, Precision, Recall, and AUC-ROC

### 4. Power BI Dashboard
- Interactive dashboard with:
  - Return rate trends
  - High-return categories/suppliers
  - Drill-through filters for deeper insights

### 5. Deliverables
- ✅ Python Codebase for preprocessing and modeling
- ✅ Power BI dashboard for return insights
- ✅ CSV of high-risk products (return probability > 60%)

---

## 📁 Project Structure

📦 E-commerce-Return-Rate-Reduction-Analysis
├── 📂 data/ # Raw and cleaned datasets
├── 📂 models/ # Trained model (joblib)
├── 📂 outputs/ # High-risk products CSV
├── 📂 visuals/ # Screenshots (optional)
├── 📜 analysis_notebook.ipynb
├── 📜 dashboard.pbix
└── 📜 README.md
