print(0.1, 1e-1)
print(0.01, 1e-2)
print(314.865, 0.341865e3) # e 지수 표현
print(21000, 21_000) # _ 천단위 구분용

univ = "Inha university"
print(univ) # 출력 : Inha university
print(univ[5]) # 출력 : u
# univ[5] = 'U' # 에러발생 : str형태는 immutable이라서 값 변경 불가능

subjects = ['a', 'b', 'c', 'd', 'e']
print(subjects) # 출력 : ['a', 'b', 'c', 'd', 'e']
print(subjects[3]) # 출력 : d
print(subjects[3:4]) # 출력 : ['d']
subjects[3] = 'f'
print(subjects[3]) # 출력 : f # mutable이라서 값 변경 가능

