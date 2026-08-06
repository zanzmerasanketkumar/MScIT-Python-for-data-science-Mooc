roll=[]
name=[]
Age=[]
python=[]
cyber=[]
cloud=[]
bigdata=[]
internship=[]

def parse_int(s):
    try:
        return int(s.strip())
    except (AttributeError, ValueError):
        return None


def parse_float(s):
    try:
        value = float(s.strip())
        if value == float('inf') or value == float('-inf') or value != value:
            return None
        return value
    except (AttributeError, ValueError):
        return None

subject_names = ('Python', 'Cyber', 'Cloud', 'Big Data', 'Internship')
num_students = 10
print("Student Performance Analytics System")

for i in range(num_students):
    print(f"\nEnter details for student {i + 1}:")
    while True:
        rollno_str = input("Enter Roll number :- ").strip()
        rollno = parse_int(rollno_str)
        if rollno is None or rollno < 1:
            print("Invalid input. Please enter an integer greater than or equal to 1.")
            continue
        break

    Name = input("Enter your name :- ").strip()

    while True:
        age_str = input("Enter your age :- ").strip()
        age = parse_int(age_str)
        if age is None or age < 1 or age > 120:
            print("Invalid input. Please enter an integer between 1 and 120.")
            continue
        break

    while True:
        Pythonmarks_str = input("Enter Python marks :- ").strip()
        Pythonmarks = parse_float(Pythonmarks_str)
        if Pythonmarks is None or Pythonmarks < 0 or Pythonmarks > 100:
            print("Invalid input. Please enter a number between 0 and 100.")
            continue
        break

    while True:
        Cybermarks_str = input("Enter Cyber marks :- ").strip()
        Cybermarks = parse_float(Cybermarks_str)
        if Cybermarks is None or Cybermarks < 0 or Cybermarks > 100:
            print("Invalid input. Please enter a number between 0 and 100.")
            continue
        break

    while True:
        Cloudmarks_str = input("Enter Cloud marks :- ").strip()
        Cloudmarks = parse_float(Cloudmarks_str)
        if Cloudmarks is None or Cloudmarks < 0 or Cloudmarks > 100:
            print("Invalid input. Please enter a number between 0 and 100.")
            continue
        break

    while True:
        Bigdata_str = input("Enter Big Data marks :- ").strip()
        Bigdata = parse_float(Bigdata_str)
        if Bigdata is None or Bigdata < 0 or Bigdata > 100:
            print("Invalid input. Please enter a number between 0 and 100.")
            continue
        break

    while True:
        Internship_str = input("Enter internship marks :- ").strip()
        Internship = parse_float(Internship_str)
        if Internship is None or Internship < 0 or Internship > 100:
            print("Invalid input. Please enter a number between 0 and 100.")
            continue
        break

    roll.append(rollno)
    name.append(Name)
    Age.append(age)
    python.append(Pythonmarks)
    cyber.append(Cybermarks)
    cloud.append(Cloudmarks)
    bigdata.append(Bigdata)
    internship.append(Internship)

student_records = []
students = []
for i in range(num_students):
    marks = {
        subject_names[0]: python[i],
        subject_names[1]: cyber[i],
        subject_names[2]: cloud[i],
        subject_names[3]: bigdata[i],
        subject_names[4]: internship[i]
    }
    total = sum(marks.values())
    percentage = total / len(subject_names)
    if percentage >= 80:
        grade = 'A'
    elif percentage >= 60:
        grade = 'B'
    elif percentage >= 50:
        grade = 'C'
    elif percentage >= 40:
        grade = 'D'
    else:
        grade = 'F'

    student_records.append((roll[i], name[i], Age[i], (python[i], cyber[i], cloud[i], bigdata[i], internship[i])))
    students.append({
        'roll': roll[i],
        'name': name[i],
        'age': Age[i],
        'marks': marks,
        'total': total,
        'percentage': percentage,
        'grade': grade
    })

percentages = [student['percentage'] for student in students]
class_average = sum(percentages) / num_students
max_percent = max(percentages)
min_percent = min(percentages)
highest = [student for student in students if student['percentage'] == max_percent]
lowest = [student for student in students if student['percentage'] == min_percent]
above_average = [student for student in students if student['percentage'] > class_average]
failed = [student for student in students if any(mark < 40 for mark in student['marks'].values())]

grade_dictionary = {}
for student in students:
    grade_dictionary.setdefault(student['grade'], []).append(student['name'])

alphabetical_names = sorted(name)

first = -1
second = -1
for percent in percentages:
    if percent > first:
        second = first
        first = percent
    elif first > percent > second:
        second = percent

second_highest = [student for student in students if student['percentage'] == second] if second != -1 else []

subject_averages = {}
for subject in subject_names:
    subject_averages[subject] = sum(student['marks'][subject] for student in students) / num_students

best_subject = max(subject_averages, key=subject_averages.get)

unique_names = []
duplicate_entries = []
seen_names = set()
for student_name in name:
    if student_name in seen_names:
        if student_name not in duplicate_entries:
            duplicate_entries.append(student_name)
    else:
        seen_names.add(student_name)
        unique_names.append(student_name)

print("\nClass Average Percentage: {:.2f}%".format(class_average))
print("Highest Scorer(s):")
for student in highest:
    print(f"  {student['name']} (Roll {student['roll']}): {student['percentage']:.2f}%")
print("Lowest Scorer(s):")
for student in lowest:
    print(f"  {student['name']} (Roll {student['roll']}): {student['percentage']:.2f}%")
print("\nStudents scoring above class average:")
for student in above_average:
    print(f"  {student['name']} (Roll {student['roll']}): {student['percentage']:.2f}%")
print("\nStudents who failed in one or more subjects:")
for student in failed:
    failing_subjects = [subject for subject, mark in student['marks'].items() if mark < 40]
    print(f"  {student['name']} (Roll {student['roll']}): failed in {', '.join(failing_subjects)}")

print("\nGrade dictionary:")
for grade, students_with_grade in sorted(grade_dictionary.items()):
    print(f"  {grade}: {students_with_grade}")

print("\nStudents in alphabetical order:")
for student_name in alphabetical_names:
    print(f"  {student_name}")

print("\nSecond-highest scorer(s):")
if second_highest:
    for student in second_highest:
        print(f"  {student['name']} (Roll {student['roll']}): {student['percentage']:.2f}%")
else:
    print("  Not enough distinct scores to determine second-highest.")

print(f"\nSubject with highest class average marks: {best_subject} ({subject_averages[best_subject]:.2f})")

print("\nDuplicate student names found:")
if duplicate_entries:
    for duplicate in duplicate_entries:
        print(f"  {duplicate}")
else:
    print("  No duplicate student names detected.")


