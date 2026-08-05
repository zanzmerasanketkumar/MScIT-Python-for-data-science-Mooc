rollno = int(input("Enter Roll number :-"))
Name = input("Enter your name :- ")
age = int(input("Enter your age :- "))
Pythonmarks = float(input("Enter Python marks :-"))
Cybermarks = float(input("Enter Cyber marks :-"))
Cloudmarks = float(input("Enter Cloud marks :-"))

totalmarks=0
fail=[]

totalmarks = Pythonmarks + Cybermarks + Cloudmarks

percentage = (totalmarks/300)*100

if Pythonmarks < 40:
    fail.append("Python")
if Cybermarks < 40:
    fail.append("Cyber")
if Cloudmarks < 40:
    fail.append("Cloud")


print("\n")

print("=" *50)
print("Information of Student :-")
print(f"Roll Number: {rollno}")
print(f"Name: {Name}")
print(f"Age: {age}")
print("=" *50)

print("\n")

print("=" *50)
print("Marks of Student :-")
print(f"Python Marks: {Pythonmarks}")
print(f"Cyber Marks: {Cybermarks}")
print(f"Cloud Marks: {Cloudmarks}")
print(f"Total Marks: {totalmarks}")
print(f"Percentage: {percentage:.2f}%")
print("=" *50)

print("\n")

print("=" *50)
if len(fail) > 0:
    print("You have failed in the following subjects :-")
    print(.join(fail))
print("=" *50)
