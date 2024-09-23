
student_scores = [150, 184, 178, 190, 195, 200, 120, 130, 140, 160, 99, 22, 30, 45, 66, 70]

#adding all scores together
total_student_scores = sum(student_scores)
# print(total_student_scores)

#for loop version of the code above
# sum = 0
# for score in student_scores:
#     sum += score
 
# print(sum)


max_student_scores = max(student_scores)
#print(max_student_scores)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
    
print(max_score)