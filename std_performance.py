import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('student_performance.csv')

# Encode technical performance as numeric values
performance_mapping = {'Average': 1, 'Good': 2, 'Excellent': 3}
df['Technical_Performance_Numeric'] = df['Technical_Performance'].map(performance_mapping)

# Pie chart for Attendance
plt.figure(figsize=(8, 8))
plt.pie(df['Attendance'], labels=df['Student_Name'], autopct='%1.1f%%', colors=sns.color_palette('Set2', len(df)))
plt.title('Student Attendance Distribution')
plt.tight_layout()
plt.savefig('student_performance_attendance.png')
plt.show()

# Bar chart for Hours Studied
plt.figure(figsize=(12, 8))
sns.barplot(x='Student_Name', y='Hours_Studied', palette='Oranges_d', data=df)
plt.title('Student Performance Based on Hours Studied')
plt.xlabel('Student Names')
plt.ylabel('Hours Studied')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('student_performance_hours_studied.png')
plt.show()

# Scatter plot for Marks
plt.figure(figsize=(12, 8))
plt.scatter(df['Student_Name'], df['Marks'], color='blue', alpha=0.7)
plt.title('Student Performance Based on Marks')
plt.xlabel('Student Names')
plt.ylabel('Marks')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('student_performance_marks_scatter.png')
plt.show()

# Pie chart for CGPA
plt.figure(figsize=(10, 10))
plt.pie(df['CGPA'], labels=df['Student_Name'], autopct='%1.1f%%', colors=sns.color_palette('Greens_d', len(df)))
plt.title('Distribution of CGPA by Students')
plt.tight_layout()
plt.savefig('student_performance_cgpa_pie.png')
plt.show()

# Bar chart for Technical Performance
plt.figure(figsize=(12, 8))
sns.barplot(x='Student_Name', y='Technical_Performance_Numeric', data=df, palette='Blues_d')
plt.title('Technical Performance of Students')
plt.xlabel('Student Names')
plt.ylabel('Technical Performance (Numeric)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('student_performance_technical_performance.png')
plt.show()
