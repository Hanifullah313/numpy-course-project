import pandas as pd
import numpy as np

# loading dataset
df = pd.read_csv(
    r"C:\Users\Laptop Valley\Desktop\Numpy\Project\student_admission_record_dirty.csv",
    encoding="utf-8"
)


# printing the first few rows and shape of the dataframe
print("First few rows of the dataset:\n")
print(df.head())

# printing the shape of the dataframe
print("\nShape of the dataset:")
print(df.shape)


#checking missing values 
print("\nbefore not removing Missing Values :\n\n", df.isnull().sum())

#Filling missing values 
df = df.dropna(subset=['Name', 'Gender'])
df = df[(df['Admission Test Score'] > 0) & 
        (df['Age'] >= 0) & 
        (df['High School Percentage'] > 0)]
df["City"]=df["City"].fillna("Unkown")
df["Admission Test Score"]=df["Admission Test Score"].fillna(df["Admission Test Score"].mean())
df["High School Percentage"]=df["High School Percentage"].fillna(df["High School Percentage"].mean())
df["Age"]=df["Age"].fillna(df["Age"].mean())
df['Admission Status'] = df['Admission Status'].fillna(
    df.apply(lambda row: "Accepted" if row['Admission Test Score'] > 60 and row['High School Percentage'] > 70 else "Rejected", axis=1)
)

# printing the missing values after removing
print("\n\nafter Removing Missing Values :\n\n", df.isnull().sum())

# Describing the data
print("\n\nDescribing the data\n\n", df.describe())

#saving new cleaned dataset
df.to_csv(r"C:\Users\Laptop Valley\Desktop\Numpy\Project\student_admission_record_cleaned.csv", index=False)
print("\n\nNew cleaned dataset saved successfully.")
print("\n\nProject completed successfully.")