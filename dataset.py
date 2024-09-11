import pandas as pd
# Define the data
data = {
    'Student_ID': [f'2100{i}' for i in range(1, 16)],
    'Student_Name': ['Aarav', 'Vihaan', 'Vivaan', 'Aditya', 'Sai', 'Ishaan', 'Kabir', 'Arjun', 'Anaya', 'Dhruv',
                     'Aanya', 'Krishna', 'Manvi', 'Meera', 'Rhea'],
    'Technical_Languages': ['Python, C++', 'Java, Python', 'C, C++', 'Ruby, Java', 'Python, Ruby',
                             'C++, Java', 'Python, C', 'C++, Ruby', 'Java, C++', 'Python, Java',
                             'Ruby, C', 'C++, Python', 'Java, Ruby', 'Python, C++', 'Java, C'],
    'Technical_Performance': ['Good', 'Excellent', 'Average', 'Good', 'Excellent',
                               'Average', 'Good', 'Excellent', 'Good', 'Excellent',
                               'Average', 'Good', 'Excellent', 'Good', 'Average'],
    'Hours_Studied': [10, 20, 15, 12, 25, 18, 22, 14, 17, 19, 16, 21, 23, 13, 24],
    'Marks': [85, 90, 78, 82, 92, 76, 88, 95, 81, 89, 77, 83, 91, 80, 84],
    'Previous_Marks': [80, 85, 75, 78, 90, 70, 85, 90, 80, 85, 70, 75, 88, 78, 82],
    'Attendance': [85, 90, 88, 80, 92, 75, 85, 90, 84, 87, 78, 82, 91, 79, 86],
    'CGPA': [8.5, 9.0, 8.2, 8.7, 9.1, 7.8, 8.8, 9.2, 8.4, 8.9, 7.9, 8.6, 9.0, 8.3, 8.7]
}
# Create a DataFrame
df = pd.DataFrame(data)
# Save the DataFrame to a CSV file
df.to_csv('student_performance.csv', index=False)
print("Dataset created and saved as 'student_performance.csv'")
