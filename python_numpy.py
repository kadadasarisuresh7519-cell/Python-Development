# ==========================================
# PANDAS & NUMPY - BASIC TO ADVANCED
# ==========================================

import pandas as pd
import numpy as np

# ------------------------------------------
# 1. LOAD CSV DATASET
# ------------------------------------------

print("----- LOAD CSV FILE -----")

df = pd.read_csv("students.csv")

print(df)

# ------------------------------------------
# 2. DISPLAY DATASET INFORMATION
# ------------------------------------------

print("\n----- DATASET INFO -----")

print(df.info())

# ------------------------------------------
# 3. CHECK MISSING VALUES
# ------------------------------------------

print("\n----- MISSING VALUES -----")

print(df.isnull().sum())

# ------------------------------------------
# 4. CLEAN MISSING VALUES
# ------------------------------------------

print("\n----- CLEANING DATA -----")

# Fill Age with average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill Marks with average marks
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print(df)

# ------------------------------------------
# 5. SUMMARY STATISTICS
# ------------------------------------------

print("\n----- SUMMARY STATISTICS -----")

print(df.describe())

# ------------------------------------------
# 6. NUMPY OPERATIONS
# ------------------------------------------

print("\n----- NUMPY ANALYSIS -----")

marks = np.array(df["Marks"])

print("Marks Array:", marks)

print("Average Marks:", np.mean(marks))
print("Maximum Marks:", np.max(marks))
print("Minimum Marks:", np.min(marks))
print("Standard Deviation:", np.std(marks))

# ------------------------------------------
# 7. FILTER DATA
# ------------------------------------------

print("\n----- TOP STUDENTS -----")

top_students = df[df["Marks"] >= 85]

print(top_students)

# ------------------------------------------
# 8. ADD NEW COLUMN
# ------------------------------------------

print("\n----- ADD GRADE COLUMN -----")

df["Grade"] = np.where(
    df["Marks"] >= 85,
    "A",
    "B"
)

print(df)

# ------------------------------------------
# 9. SORT DATA
# ------------------------------------------

print("\n----- SORT BY MARKS -----")

sorted_df = df.sort_values(
    by="Marks",
    ascending=False
)

print(sorted_df)

# ------------------------------------------
# 10. GROUP ANALYSIS
# ------------------------------------------

print("\n----- GRADE COUNT -----")

print(df["Grade"].value_counts())

# ------------------------------------------
# 11. ADVANCED ANALYSIS
# ------------------------------------------

print("\n----- PERFORMANCE REPORT -----")

print("Total Students:", len(df))
print("Average Marks:", df["Marks"].mean())

best_student = df.loc[
    df["Marks"].idxmax()
]

print(
    "Top Student:",
    best_student["Name"]
)

print(
    "Highest Marks:",
    best_student["Marks"]
)

# ------------------------------------------
# 12. SAVE CLEANED DATA
# ------------------------------------------

df.to_csv(
    "cleaned_students.csv",
    index=False
)

print(
    "\nCleaned data saved to "
    "'cleaned_students.csv'"
)

print("\nProgram Completed Successfully!")