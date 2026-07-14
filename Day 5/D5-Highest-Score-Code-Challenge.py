student_scores = [150, 142, 185, 128, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

print(student_scores)

print(sum(student_scores))
sum = 0
for score in student_scores:
    sum += score
print(sum)


print(max(student_scores))
# Replicate the max function using a for loop
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)

