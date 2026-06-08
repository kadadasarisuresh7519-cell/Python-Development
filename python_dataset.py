# ==========================================
# MATPLOTLIB & SEABORN
# BASIC TO ADVANCED VISUALIZATION
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------
# 1. SAMPLE DATASET
# ------------------------------------------

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [15000, 18000, 22000, 25000, 28000]
}

df = pd.DataFrame(data)

print(df)

# Set Seaborn Style
sns.set_style("whitegrid")

# ------------------------------------------
# 2. LINE GRAPH
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Month"],
    df["Sales"],
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)

plt.show()

# ------------------------------------------
# 3. BAR CHART
# ------------------------------------------

plt.figure(figsize=(8,5))

plt.bar(
    df["Month"],
    df["Sales"]
)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()

# ------------------------------------------
# 4. PIE CHART
# ------------------------------------------

plt.figure(figsize=(7,7))

plt.pie(
    df["Sales"],
    labels=df["Month"],
    autopct="%1.1f%%"
)

plt.title("Sales Distribution")

plt.show()

# ------------------------------------------
# 5. SEABORN BARPLOT
# ------------------------------------------

plt.figure(figsize=(8,5))

sns.barplot(
    x="Month",
    y="Sales",
    data=df
)

plt.title("Sales Analysis Using Seaborn")

plt.show()

# ------------------------------------------
# 6. ADVANCED DATASET
# ------------------------------------------

students = {
    "Name": [
        "Suresh",
        "Ravi",
        "Priya",
        "Anu",
        "Kiran"
    ],
    "Marks": [
        85,
        72,
        95,
        88,
        76
    ]
}

student_df = pd.DataFrame(students)

# ------------------------------------------
# 7. STUDENT MARKS BAR CHART
# ------------------------------------------

plt.figure(figsize=(8,5))

sns.barplot(
    x="Name",
    y="Marks",
    data=student_df
)

plt.title("Student Marks")

plt.show()

# ------------------------------------------
# 8. HIGHEST MARKS ANALYSIS
# ------------------------------------------

top_student = student_df.loc[
    student_df["Marks"].idxmax()
]

print("\nTop Student:")
print(top_student)

# ------------------------------------------
# 9. MULTIPLE LINE GRAPH
# ------------------------------------------

performance = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [15000, 18000, 22000, 25000, 28000],
    "Profit": [3000, 4000, 5000, 6000, 7000]
}

performance_df = pd.DataFrame(performance)

plt.figure(figsize=(8,5))

plt.plot(
    performance_df["Month"],
    performance_df["Sales"],
    marker="o",
    label="Sales"
)

plt.plot(
    performance_df["Month"],
    performance_df["Profit"],
    marker="s",
    label="Profit"
)

plt.title("Sales vs Profit")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()

plt.show()

# ------------------------------------------
# 10. ADVANCED SEABORN LINEPLOT
# ------------------------------------------

plt.figure(figsize=(8,5))

sns.lineplot(
    x="Month",
    y="Sales",
    data=performance_df,
    marker="o"
)

plt.title("Seaborn Sales Trend")

plt.show()

print("\nVisualization Completed Successfully!")