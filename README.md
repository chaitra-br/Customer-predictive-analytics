# Predictive Analytics for Customer Behavior

> A data-driven project to understand customer behavior and predict outcomes using machine learning and analytics techniques.

## 📊 Overview

This project focuses on applying **predictive analytics** to an e-commerce customer dataset. It covers the complete data science pipeline—from cleaning and exploration to feature engineering, model building, evaluation, and dashboard creation. The goal is to derive actionable insights and build predictive models that help businesses make informed decisions.

## 🧠 Key Features

* 🧹 **Data Cleaning**: Handles missing values, incorrect data types, and inconsistencies.
* 📊 **Exploratory Data Analysis (EDA)**: Visualizes patterns and distributions using custom plots.
* 🏗️ **Feature Engineering**: Extracts and transforms features to enhance model performance.
* 🤖 **Model Training**: Compares multiple machine learning algorithms.
* ✅ **Model Evaluation**: Assesses model accuracy, precision, recall, and F1-score.
* 📉 **Dashboard**: An interactive Streamlit app for visualizing predictions and insights.

## 📁 Project Structure

```
predictive_analytics_project/
│
├── data/
│   ├── ecommerce_customer_data_large.csv   # Raw dataset
│   └── cleaned_customer_data.csv           # Cleaned dataset
│
├── dashboard_app.py              # Streamlit dashboard script
├── data_cleaning.py              # Preprocessing and cleaning logic
├── eda_analysis.py               # EDA visualization script
├── feature_engineering.py        # Feature extraction and transformation
├── model_training.py             # Model training logic
├── model_evaluation.py           # Model performance metrics
├── model_comparison.py           # Algorithm comparison results
├── age_distribution.png          # Sample output plot
├── requirements.txt              # Dependencies
└── venv/                         # Virtual environment (excluded from version control)
```

## 🚀 How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/predictive_analytics_project.git
   cd predictive_analytics_project
   ```

2. **Set up the environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the dashboard**

   ```bash
   streamlit run dashboard_app.py
   ```

## 📌 Requirements

* Python 3.8+
* pandas, numpy, scikit-learn, matplotlib, seaborn, streamlit, etc.

Install all dependencies via:

```bash
pip install -r requirements.txt
```

## 🔗 Connect with Me

**📧 Email:** [chaitrabr03@gmail.com](mailto:chaitrabr03@gmail.com)

**🔗 LinkedIn:** [B R Chaitra](https://www.linkedin.com/in/br-chaitra/)
