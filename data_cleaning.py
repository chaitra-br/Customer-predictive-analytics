import pandas as pd
import os

# Paths
input_path = 'data/ecommerce_customer_data_large.csv'
output_path = 'data/cleaned_customer_data.csv'

# STEP 1: Load raw data
if not os.path.exists(input_path):
    print(f"❌ File not found: {input_path}")
    exit()

print("📂 Loading data...")
df = pd.read_csv(input_path)
print(f"🔹 Original rows: {len(df)}")

# STEP 2: Clean data
df = df.drop_duplicates()
df = df.dropna()
print(f"✅ Cleaned rows: {len(df)}")

# STEP 3: Save cleaned data
df.to_csv(output_path, index=False)
print(f"📁 Cleaned data saved to: {output_path}")

# STEP 4: Load cleaned data for analysis (optional)
cleaned_data = pd.read_csv(output_path)
print("📊 Ready for analysis!")
print(cleaned_data.head())
