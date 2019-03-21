# 201504003 구본익
# 2019.03.28 자정까지!!
# Lab : 평균 구하기
kor_score = [51,60,20,50,90]
math_score = [87,57,34,80,67]
eng_score = [99,54,33,56,89]

for i in range(0, 3): # 0 ~ 2 까지 3번 반복
    for n in range(0, 5): # 0 ~ 4 까지 5번 반복
        if i == 0:
            print(n + 1, " 번째 국어 성적 입력")
            kor_score[n] = int(input())
        elif i == 1 :
            print(n + 1, " 번째 수학 성적 입력")
            math_score[n] = int(input())
        elif i == 2 :
            print(n + 1, " 번째 영어 성적 입력")
            eng_score[n] = int(input())

midterm_score = [kor_score, math_score, eng_score]


student_score = [0,0,0,0,0]

i = 0

for subject in midterm_score: # subject 에 국어, 수학 , 영어 차례대로 들어갈 것임
    for score in subject: # subject 만큼 반복하며 차례대로 score에 대입
        student_score[i] += score # 각 0 ~ 4 배열에 있는 값을을 더해준다
        i += 1
    i = 0 # 다시 0을 만들어줘야 돌아가서 처음부터 요소를 넣어줄 수 있음

else:
    a, b, c, d, e = student_score # 알바벳에 각각 풀어서 대입
    student_average = [a/3, b/3, c/3, d/3, e/3]
    print(student_average)