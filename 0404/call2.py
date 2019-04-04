def spam(eggs):
    eggs.append(1)

    eggs = [2,3] # 얘는 별 상관 없음

ham = [0] # 0 이라는 요소 추가
spam(ham) # 햄에 1 추가
print(ham) # [0,1] 출력될 것임