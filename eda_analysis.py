import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned_customer_data.csv")

sns.histplot(data=df, x="Age", bins=15, kde=True)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.savefig("age_distribution.png")
plt.clf()

# Create Age² column
df["Age_Squared"] = df["Age"] ** 2

# Plot setup
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Boxplot: Age vs Churn
sns.boxplot(data=df, x="Churn", y="Age", ax=axes[0])
axes[0].set_title("Age vs Churn")
axes[0].set_xlabel("Churn")
axes[0].set_ylabel("Age")

# Boxplot: Age² vs Churn
sns.boxplot(data=df, x="Churn", y="Age_Squared", ax=axes[1])
axes[1].set_title("Age² vs Churn")
axes[1].set_xlabel("Churn")
axes[1].set_ylabel("Age Squared")

plt.tight_layout()
plt.show()