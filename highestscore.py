# .split is to convert it into a stringπ
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# π¨ Don't change the code above π

#Write your code below this row π
highest_score=0
for score in student_scores:
  if score>highest_score:
    highest_score=score
print(highest_score)