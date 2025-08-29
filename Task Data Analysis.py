# Task: Data Analysis & Visualization Assignment

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# ----------------- Task 1: Load and Explore the Dataset -----------------
try:
    # Load Iris dataset from sklearn
    iris_data = load_iris(as_frame=True)
    df = iris_data.frame

    print("✅ Dataset loaded successfully!\n")

    # Display first few rows
    print("First 5 rows of dataset:")
    print(df.head(), "\n")

    # Check data types and missing values
    print("Dataset Info:")
    print(df.info(), "\n")

    print("Missing values per column:")
    print(df.isnull().sum(), "\n")

    # Clean dataset (fill missing values if any)
    df = df.fillna(df.mean(numeric_only=True))

except FileNotFoundError:
    print("❌ Error: File not found.")
except Exception as e:
    print("❌ An error occurred:", e)

# ----------------- Task 2: Basic Data Analysis -----------------
print("Basic Statistics:")
print(df.describe(), "\n")

# Grouping by species and getting mean
print("Average values by species:")
print(df.groupby("target").mean(), "\n")

# ----------------- Task 3: Data Visualization -----------------
# Set style
sns.set(style="whitegrid")

# 1. Line Chart - Petal length trend (just for demonstration)
plt.plot(df.index, df["petal length (cm)"], label="Petal Length")
plt.title("Line Chart - Petal Length Trend")
plt.xlabel("Index")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart - Average petal length per species
df.groupby("target")["petal length (cm)"].mean().plot(kind="bar", color="skyblue")
plt.title("Bar Chart - Avg Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Avg Petal Length (cm)")
plt.show()

# 3. Histogram - Sepal length distribution
plt.hist(df["sepal length (cm)"], bins=15, color="lightgreen", edgecolor="black")
plt.title("Histogram - Sepal Length Distribution")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot - Sepal length vs Petal length
plt.scatter(df["sepal length (cm)"], df["petal length (cm)"], c=df["target"], cmap="viridis")
plt.title("Scatter Plot - Sepal vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.colorbar(label="Species")
plt.show()
