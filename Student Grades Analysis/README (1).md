# Lesson 4 – Data Manipulation with Pandas

Exercise focused on manipulating and combining data with **pandas**, using two related datasets about university students and their exam grades.

**Dataset 1 – `students.csv`**: student registry data (StudentID, Name, Degree, Year, EnrollmentDate).

**Dataset 2 – `grades.csv`**: exam records for each student (StudentID, Course, Grade, Date).

The exercise covers initial data exploration, adding and renaming columns, grouping data to compute average grades per course/student, merging the two datasets on `StudentID`, sorting results, creating derived columns (pass/fail result, exam month), and working with dates (enrollment year, years enrolled, days between enrollment and exam, first exam date per student).

## 📁 Folder Structure

```
exercise_04/
├── main.py
├── requirements.txt
└── data/
    ├── students.csv
    └── grades.csv
```

## 🚀 How to Run

1. Navigate to the folder:
   ```bash
   cd exercise_04
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # on Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the script:
   ```bash
   python main.py
   ```

⚠️ **Note:** the script must be run from inside the `exercise_04/` folder, since it references the datasets using the relative path `data/students.csv` and `data/grades.csv`.
