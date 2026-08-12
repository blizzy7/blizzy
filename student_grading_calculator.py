student_name = input("Enter your name: ")
test_score1 = int(input("Enter your score: "))
test_score2 = int(input("Enter your score: "))
test_score3 = int(input("Enter your score: "))
average = (test_score1 + test_score2 + test_score3 ) / 3
if average >= 70:
    print(average)
    grade = "A" 
elif average >= 60:
    grade = "B" 
elif average >= 50:
    grade = "C"
elif average >= 45:
    grade = "D"
elif average >= 40:
    grade = "E"
else:
    grade = "F"

print("\n=====student report=====")
print(f"name: {student_name}")
print(f"score1: {test_score1}")
print(f"score2: {test_score2}")
print(f"score3: {test_score3}")
print(f"average: {average:.1f}")
print(f"    grade: {grade} ")                        