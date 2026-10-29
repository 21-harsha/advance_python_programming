
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# 1. Load the dataset
df = pd.read_csv("customer_churn.csv")

# 2. Display dataset information
print("First five records:")
print(df.head())

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

# 3. Descriptive Statistics
print("\nDescriptive Statistics:")
print(df.describe())

num = df.select_dtypes(include=np.number)

print("\nMean:")
print(num.mean())

print("\nMedian:")
print(num.median())

print("\nMode:")
print(df.mode().iloc[0])

print("\nStandard Deviation:")
print(num.std())

print("\nVariance:")
print(num.var())

print("\nMinimum Values:")
print(num.min())

print("\nMaximum Values:")
print(num.max())

print("\nPercentiles:")
print(num.quantile([0.25, 0.50, 0.75]))

# 4. Data Visualization
# Histogram
num.hist(figsize=(10, 8))
plt.tight_layout()
plt.show()

# Boxplot
for col in num.columns:
    sns.boxplot(x=df[col])
    plt.title("Boxplot of " + col)
    plt.show()

# Scatter plot (first two numerical columns)
if len(num.columns) >= 2:
    sns.scatterplot(x=num.columns[0], y=num.columns[1], data=df)
    plt.show()

# Correlation heatmap
if len(num.columns) >= 2:
    sns.heatmap(num.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()

# 5. Handle Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing numerical values with their mean
for col in num.columns:
    df[col] = df[col].fillna(df[col].mean())

# Remove rows with remaining missing values
df = df.dropna()

print("\nDataset after handling missing values:")
print(df.isnull().sum())

# 6. Detect and Handle Outliers using Z-score
num_cols = df.select_dtypes(include=np.number).columns

if len(num_cols) > 0:
    z = df[num_cols].apply(
        lambda col: zscore(col, nan_policy="omit")
    )

    outliers = (z.abs() > 3)

    print("\nDetected Outliers:")
    print(df[outliers.any(axis=1)])

    # Cap outliers using the 3-standard-deviation limits
    for col in num_cols:
        mean = df[col].mean()
        std = df[col].std()

        lower = mean - 3 * std
        upper = mean + 3 * std

        df[col] = df[col].clip(lower, upper)

# 7. Verify cleaned dataset
print("\nRemaining Missing Values:")
print(df.isnull().sum())

print("\nFinal Dataset:")
print(df.head())

# 8. Save cleaned dataset
df.to_csv("cleaned_customer_churn.csv", index=False)

print("\nCleaned dataset saved successfully!")
