kor_score = [51,60,20,50,90]
math_score = [87,57,34,80,67]
eng_score = [99,54,33,56,89]

midterm_score = [kor_score, math_score, eng_score]


student_score = [0,0,0,0,0]

i = 0

for subject in midterm_score:
    for score in subject:
        student_score[i] += score
        i += 1
    i = 0

else:
    a, b, c, d, e = student_score
    student_average = [a/3, b/3, c/3, d/3, e/3]
    print(student_average)