# -*- coding: utf-8 -*-
"""
Lesson 2 - Pandas Fundamentals
Data Analytics with Python - Python Accelerator
"""

import pandas as pd

# Import dataset
df = pd.read_csv("data/training_data.csv")
df.index = range(1, len(df) + 1)
print(df)

# Explore the dataset
print(df.head(10))      # first 10 rows
print(df.columns)       # column names
print(df.shape)          # number of rows and columns
print(df.dtypes)         # data type of each column

# Check for missing values
print(df.isnull().sum())

# Handle missing values
df['Date'] = df['Date'].fillna('2020-01-01')          # fill missing dates with a default value
df['Calories'] = df['Calories'].fillna(df['Calories'].mean())  # fill missing calories with the column mean
print(df)

# Select specific columns
print(df[['Pulse', 'Calories']])

# Select data using loc
print(df.loc[1:14, ['Date', 'Maxpulse']])

# Select data using iloc
print(df.iloc[9:14, [1, 2, 4]])
