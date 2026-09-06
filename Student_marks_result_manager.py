name = input("Enter your name:")

print(name)
name = name.strip()
name = name.upper()
print(f"Welcome,{name}")
subjects = ("python","math","AI","English","DSA")
print(subjects)
print(len(subjects))

python_marks = int(input("Enter python marks:"))
math_marks = int(input("Enter math marks:"))
AI_marks   = int(input("Enter AI marks:"))
English_marks = int(input("Enter English marks:"))
DSA_marks = int(input("Enter DSA marks:"))
# step 5: store marks in a list
marks = [python_marks,math_marks,AI_marks,English_marks,DSA_marks]
# step 6 : calculate total
total = sum(marks)
print(total)
# step 7: average of all subjects
average = total/len(marks)

# step 8: Highest and lowest marks
highest = max(marks)
lowest = min(marks)
print(highest)
print(lowest)

# step 9: pass or fail condition
if min(marks)>= 40:
   result = "PASS"
else:
   result = "FAIL" 

# step 10: display result
print("\n-------------------------") 
print("     STUDENT RESULT")
print("-------------------------")

print(f"Name :{name}")



#subject marks
print("\nsubject Marks")
print("--------------------------")

print(f"{subjects[0]} :{marks[0]}")
print(f"{subjects[1]} :{marks[1]}")
print(f"{subjects[2]} :{marks[2]}")
print(f"{subjects[3]} :{marks[3]}")
print(f"{subjects[4]} :{marks[4]}")


print(f"Total  :{total}/500")
print(f"Average :{average:.2f}")
print(f"Highest : {highest}")
print(f"Lowest  :{lowest}")
print(f"Result  :{result}")

print("--------------------------")

# step 11: add tuple in project
student_info = (name,"B.Tech & AI & ML")
print(student_info)
print(student_info[0])
print(student_info[1])

