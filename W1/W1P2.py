# Student Marks Analysis
names = []
marks = []

print("Enter details of 10 students:\n")

# Input student names and marks
for i in range(10):
    name = input(f"Enter name of Student {i+1}: ")
    mark = float(input(f"Enter marks of {name}: "))

    names.append(name)
    marks.append(mark)

# Convert marks list into tuple
marks_tuple = tuple(marks)

# Store student names and marks in dictionary
student_dict = {}

for i in range(len(names)):
    student_dict[names[i]] = marks[i]

# Find highest, lowest and average marks
highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

# Display results
print("\n----- Student Marks Analysis -----")

print("Marks List :", marks)
print("Marks Tuple :", marks_tuple)
print("Student Dictionary :", student_dict)

print("\nHighest Marks :", highest)
print("Lowest Marks :", lowest)
print("Average Marks : {:.2f}".format(average))

# Students scoring above average
print("\nStudents Scoring Above Average:")

found = False
for name, mark in student_dict.items():
    if mark > average:
        print(f"{name} : {mark}")
        found = True

if not found:
    print("No student scored above average.")

# Remove duplicate marks using set
unique_marks = set(marks)

print("\nUnique Marks (Duplicates Removed):")
print(unique_marks)