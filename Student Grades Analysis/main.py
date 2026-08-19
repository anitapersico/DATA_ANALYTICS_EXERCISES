# -*- coding: utf-8 -*-
"""
Lesson 4 - Data Manipulation with Pandas
Data Analytics with Python - Python Accelerator
"""

import pandas as pd

# --- Initial exploration ---

students = pd.read_csv('data/students.csv')
print(students.head())          # print the first 5 rows of each dataset
print(students.shape)           # check number of rows and columns

grades = pd.read_csv('data/grades.csv')
print(grades.head())
print(grades.shape)

# --- Modifications to the dataframes ---

# Add a 'Passed' column to grades: True if Grade >= 18, False otherwise
grades['Passed'] = (grades['Grade'] >= 18)
print(grades.head())

# Temporarily drop the 'Year' column from students, then reload it
students = students.drop(columns='Year')
print(students.head())

students = pd.read_csv('data/students.csv')  # reload students to restore the original 'Year' column
print(students.head())

# Rename the 'Degree' column to 'Major'
students = students.rename(columns={'Degree': 'Major'})
print(students.head())

# --- Grouping operations ---

print(grades.groupby('Course')['Grade'].mean().reset_index())      # average grade per course
print(grades.groupby('StudentID')['Grade'].mean().reset_index())   # average grade per student

# --- Merging the dataframes ---

df = pd.merge(students, grades, on='StudentID')  # merge students and grades on StudentID
print(df.head())

# Show only the columns: Name, Major, Course, Grade, Date
print(df[['Name', 'Major', 'Course', 'Grade', 'Date']])

# --- Sorting ---

print(df.sort_values('Grade', ascending=False))  # sort students by grade, descending

# Sort courses by average grade (highest to lowest)
print(df.groupby('Course')['Grade'].mean().reset_index().sort_values('Grade', ascending=False))

# --- Derived variables ---

# Create a 'Result' column: "Superato" if Grade >= 18, otherwise "Non Superato"
df['Result'] = 'Non Superato'
df.loc[df['Grade'] >= 18, 'Result'] = 'Superato'
print(df[['Name', 'Course', 'Grade', 'Result']])

# Create an 'ExamMonth' column by extracting the month from the exam Date
df['Date'] = pd.to_datetime(df['Date'])
df['ExamMonth'] = df['Date'].dt.month_name()
print(df[['Name', 'Course', 'Date', 'ExamMonth']])

# --- Date operations ---

df['EnrollmentDate'] = pd.to_datetime(df['EnrollmentDate'])
df['EnrollmentYear'] = df['EnrollmentDate'].dt.year
print(df[['Name', 'EnrollmentYear']])

# Calculate, for each student, how many years they have been enrolled (relative to 2023)
df['YearsEnrolled'] = 2023 - df['EnrollmentYear']
print(df[df['EnrollmentYear'] < 2023])
print(df[['Name', 'EnrollmentYear', 'YearsEnrolled']])

# Calculate the number of days between enrollment date and each exam
df['DaysBetweenEnrollmentAndExam'] = (df['Date'] - df['EnrollmentDate']).dt.days
print(df[['Name', 'EnrollmentDate', 'Course', 'Date', 'DaysBetweenEnrollmentAndExam']])

# Find, for each student, the date of their first exam
first_exam_date = df.groupby(['StudentID', 'Name'])['Date'].min().reset_index()
first_exam_date = first_exam_date.rename(columns={'Date': 'FirstExamDate'})
print(first_exam_date)
