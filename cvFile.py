import csv
from datetime import datetime

# List of people with initial attendance status
people = ["Bean", "Ben", "Jacky", "Robert", "Tom"]

# Create or overwrite the CSV file with initial attendance values
with open('attendance.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Attendance', 'Date', 'Time']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for person in people:
        writer.writerow({'Name': person, 'Attendance': 'Absent', 'Date': '-', 'Time': '-'})