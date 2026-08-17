import numpy as np

# Load the CSV data
csv_file = "student_performance_10_students.csv"
data = np.genfromtxt(csv_file, delimiter=',', dtype=str, skip_header=1)

# Batch and basic info
batch_input = "  Batch-2026-Computer_Science  "
batch = batch_input.strip()
dept = batch.split('-')[-1].replace('_', ' ')

# Extract data from CSV
subjects = ("Cyber", "Cloud", "BigData", "Mooc", "Internship")
students = [str(name) for name in data[:, 1]]
marks = data[:, 2:7].astype(float)

print("\n" + "="*60)
print("STUDENT PERFORMANCE REPORT")
print("="*60)

# Display basic info
print(f"\nBatch: {batch}")
print(f"Department: {dept}")
print(f"Total Students: {len(students)}")
print(f"Subjects: {', '.join(subjects)}")

# Roll numbers
print("\n" + "-"*60)
print("STUDENT LIST")
print("-"*60)
for i, name in enumerate(students, 1):
    print(f"{i}. {name}")

# Marks table
print("\n" + "-"*60)
print("MARKS TABLE")
print("-"*60)
print(f"{'Name':<25} {'Cyber':<8} {'Cloud':<8} {'BigData':<8} {'Mooc':<8} {'Intrnship':<8}")
print("-"*60)
for name, row in zip(students, marks):
    marks_str = "  ".join([f"{m:>3.0f}" for m in row])
    print(f"{name:<25} {marks_str}")

# Calculate basic stats
total = marks.sum(axis=1)
total_max = len(subjects) * 100
pct = (total / total_max) * 100
avg_subject = marks.mean(axis=0)

print("\n" + "-"*60)
print("STUDENT PERFORMANCE")
print("-"*60)
print(f"{'Name':<25} {'Total':<15} {'%':<12}")
print("-"*60)
for name, t, p in zip(students, total, pct):
    print(f"{name:<25} {t:>5.0f}/500     {p:>7.2f}%")

# Subject averages
print("\n" + "-"*60)
print("SUBJECT AVERAGES")
print("-"*60)
for subj, avg in zip(subjects, avg_subject):
    print(f"{subj:<18}: {avg:>6.2f}")

# Key metrics
h_mark = marks.max()
l_mark = marks.min()
class_avg = pct.mean()

top_idx = int(np.argmax(total))
bot_idx = int(np.argmin(total))

high_subj_idx = int(np.argmax(avg_subject))
low_subj_idx = int(np.argmin(avg_subject))

print(f"\nHighest Mark: {h_mark:.0f}/100")
print(f"Lowest Mark: {l_mark:.0f}/100")
print(f"Class Avg: {class_avg:.2f}%")
print(f"\nTop Student: {students[top_idx]} ({total[top_idx]:.0f} marks)")
print(f"Bottom Student: {students[bot_idx]} ({total[bot_idx]:.0f} marks)")
print(f"\nBest Subject: {subjects[high_subj_idx]} ({avg_subject[high_subj_idx]:.2f})")
print(f"Worst Subject: {subjects[low_subj_idx]} ({avg_subject[low_subj_idx]:.2f})")


# Slicing
print("\n" + "-"*60)
print("FIRST 3 STUDENTS - LAST 2 SUBJECTS")
print("-"*60)
slice_marks = marks[:3, -2:]
print(f"Subjects: {subjects[-2:]}\n")
for i in range(3):
    marks_str = " | ".join([f"{m:>3.0f}" for m in slice_marks[i]])
    print(f"{students[i]:<25}: {marks_str}")

# Subject search
print("\n" + "-"*60)
print("SUBJECT LOOKUP")
print("-"*60)
search = "Mooc"
if search in subjects:
    idx = subjects.index(search)
    print(f"'{search}' found at index {idx}")
else:
    print(f"'{search}' not found")

# Distinction
print("\n" + "-"*60)
print("DISTINCTION STUDENTS (>= 85%)")
print("-"*60)
dist = [(name, p) for name, p in zip(students, pct) if p >= 85]
if dist:
    for name, p in dist:
        print(f"  {name:<23}  {p:>7.2f}%")
    print(f"\nTotal: {len(dist)}")
else:
    print("No distinction students")

# Failed
print("\n" + "-"*60)
print("FAILED STUDENTS (< 40 in any subject)")
print("-"*60)
failed = []
for i, name in enumerate(students):
    if np.any(marks[i] < 40):
        bad_subj = [subjects[j] for j in range(len(subjects)) if marks[i][j] < 40]
        print(f"  {name:<23}  Failed: {', '.join(bad_subj)}")
        failed.append(name)

if not failed:
    print("No failed students")
else:
    print(f"Total: {len(failed)}")

# Above average
print("\n" + "-"*60)
print(f"ABOVE CLASS AVERAGE ({class_avg:.2f}%)")
print("-"*60)
above = [(name, p) for name, p in zip(students, pct) if p > class_avg]
for name, p in above:
    print(f"  {name:<23}  {p:>7.2f}%")
print(f"Total: {len(above)}")

# Reverse
print("\n" + "-"*60)
print("REVERSED LIST")
print("-"*60)
rev = students[::-1]
print("Reversed:")
for i, name in enumerate(rev, 1):
    print(f"  {i}. {name}")

print("\nOriginal (unchanged):")
for i, name in enumerate(students, 1):
    print(f"  {i}. {name}")

# Sorted
print("\n" + "-"*60)
print("ALPHABETICAL ORDER")
print("-"*60)
sorted_list = sorted(students)
print("Sorted:")
for i, name in enumerate(sorted_list, 1):
    print(f"  {i}. {name}")

print("\nOriginal (unchanged):")
for i, name in enumerate(students, 1):
    print(f"  {i}. {name}")

# Summary
print("\n" + "="*60)
print("SUMMARY")
print("="*60)
print(f"Batch: {batch}")
print(f"Dept: {dept}")
print(f"Students: {len(students)}")
print(f"Class Avg: {class_avg:.2f}%")
print(f"Top: {students[top_idx]}")
print(f"Bottom: {students[bot_idx]}")
print(f"Best Subject: {subjects[high_subj_idx]}")
print(f"Worst Subject: {subjects[low_subj_idx]}")
print(f"Distinction: {len(dist)}")
print(f"Failed: {len(failed)}")
print("="*60 + "\n")
