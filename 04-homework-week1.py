# 과제 4 - 컴퓨터 공학도 기분을 내보자 2!  다이아몬드 그리기
#
# list = [0,0,0,0,0]
list = [0,0,0,0,0]
for num in range(1,6):
    a = abs(3-num)
    for num2 in range(0,a):
        list[num2] = 0
    for num3 in range(a,5-a):
        list[num3] = 1
    for num4 in range(5-a,5):
        list[num4] = 0
    print("{} {} {} {} {}".format(list[0],list[1],list[2],list[3],list[4]))
   
