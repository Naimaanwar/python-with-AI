import pandas as pd

# ==========================================
# Task 1: Dataset Loading and Exploration
# ==========================================
print("="*50)
print("TASK 1: DATASET LOADING AND EXPLORATION")
print("="*50)

# Load the CSV file into a Pandas DataFrame
df = df = pd.read_csv('student.csv.csv')

print("1 & 2. Dataset loaded successfully.")
print("\n3. First 5 records:")
print(df.head())

print("\n4. Last 5 records:")
print(df.tail())

print(f"\n5. Total number of rows and columns: {df.shape[0]} rows, {df.shape[1]} columns")

print("\n6. Column names and data types:")
print(df.dtypes)

print("\n7. Statistical summary of the dataset:")
print(df.describe())


# ==========================================
# Task 2: Performance Analysis
# ==========================================
print("\n" + "="*50)
print("TASK 2: PERFORMANCE ANALYSIS")
print("="*50)

avg_marks = df['Marks'].mean()
highest_marks = df['Marks'].max()
lowest_marks = df['Marks'].min()
avg_attendance = df['Attendance'].mean()
top_student_row = df.loc[df['Marks'].idxmax()]

print(f"1. Average marks of all students: {avg_marks:.2f}")
print(f"2. Highest marks obtained: {highest_marks}")
print(f"3. Lowest marks obtained: {lowest_marks}")
print(f"4. Average attendance percentage: {avg_attendance:.2f}%")
print(f"5. Student who obtained the highest marks: {top_student_row['Student_Name']} (ID: {top_student_row['Student_ID']}, Marks: {top_student_row['Marks']})")


# ==========================================
# Task 3: Data Filtering
# ==========================================
print("\n" + "="*50)
print("TASK 3: DATA FILTERING")
print("="*50)

print("1. Students who scored more than 70 marks:")
print(df[df['Marks'] > 70])

print("\n2. Students whose attendance is below 75%:")
print(df[df['Attendance'] < 75])

print("\n3. Students who scored below 50 marks:")
print(df[df['Marks'] < 50])

print("\n4. Students who have attendance above 85% and marks above 80:")
print(df[(df['Attendance'] > 85) & (df['Marks'] > 80)])


# ==========================================
# Task 4: Data Manipulation
# ==========================================
print("\n" + "="*50)
print("TASK 4: DATA MANIPULATION")
print("="*50)

# Create Result column
df['Result'] = df['Marks'].apply(lambda x: 'Pass' if x >= 50 else 'Fail')

# Create Grade column based on criteria
def assign_grade(marks):
    if 90 <= marks <= 100:
        return 'A'
    elif 80 <= marks <= 89:
        return 'B'
    elif 70 <= marks <= 79:
        return 'C'
    elif 50 <= marks <= 69:
        return 'D'
    else:
        return 'F'

df['Grade'] = df['Marks'].apply(assign_grade)
print("New columns 'Result' and 'Grade' created successfully. Preview:")
print(df[['Student_Name', 'Marks', 'Attendance', 'Result', 'Grade']].head())


# ==========================================
# Task 5: Sorting and Grouping
# ==========================================
print("\n" + "="*50)
print("TASK 5: SORTING AND GROUPING")
print("="*50)

# 1. Sort students according to marks in descending order
sorted_df = df.sort_values(by='Marks', ascending=False)
print("1. Students sorted by marks (descending):")
print(sorted_df[['Student_ID', 'Student_Name', 'Marks']])

# 2. Count total number of students who passed and failed
result_counts = df['Result'].value_counts()
print("\n2. Count of students who passed and failed:")
print(result_counts)

# 3. Display the top three performing students
top_three = sorted_df.head(3)
print("\n3. Top three performing students:")
print(top_three[['Student_ID', 'Student_Name', 'Marks', 'Grade']])

# 4. Calculate average marks for each grade
avg_marks_by_grade = df.groupby('Grade')['Marks'].mean().reindex(['A', 'B', 'C', 'D', 'F']).dropna()
print("\n4. Average marks for each grade:")
print(avg_marks_by_grade)


# ==========================================
# Task 6: Final Report Generation
# ==========================================
print("\n" + "="*50)
print("TASK 6: FINAL REPORT GENERATION")
print("="*50)

output_filename = 'student_performance_report.csv'
df.to_csv(output_filename, index=False)
print(f"Final report successfully generated and saved as '{output_filename}' in your project folder.")