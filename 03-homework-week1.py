# 가위 바위 보 게임

import random
selectlist = ["가위", "바위", "보"]
com_count = 0
user_count = 0

while com_count != 3 and user_count != 3 : #다합쳐 3번을 지거나, 3번을 이길때까지 반복!
    # 사용자에게 물어보기
    user_pick = input("가위, 바위, 보 중에 하나를 입력하세요 ")
    # 컴퓨터가 선택하기
    com_pick = selectlist[random.randint(1,3)-1]
    # 컴퓨터에게 가위,바위,보의 승패 가르치기
    if user_pick == "가위":
        if com_pick == "바위":
            print("당신은 {}!, 컴퓨터는 {}! 당신이 졌습니다.".format(user_pick,com_pick))
            com_count = com_count + 1
        elif com_pick == "보":
            print("당신은 {}!, 컴퓨터는 {}! 당신이 이겼습니다.".format(user_pick,com_pick))
            user_count = user_count + 1
        else :
            print("당신은 {}!, 컴퓨터는 {}! 비겼습니다.".format(user_pick,com_pick))
    elif user_pick == "바위":
        if com_pick == "보":
            print("당신은 {}!, 컴퓨터는 {}! 당신이 졌습니다.".format(user_pick,com_pick))
            com_count = com_count + 1
        elif com_pick == "가위":
            print("당신은 {}!, 컴퓨터는 {}! 당신이 이겼습니다.".format(user_pick,com_pick))
            user_count = user_count + 1
        else :
            print("당신은 {}!, 컴퓨터는 {}! 비겼습니다.".format(user_pick,com_pick))
    elif user_pick == "보":
        if com_pick == "가위":
            print("당신은 {}!, 컴퓨터는 {}! 당신이 졌습니다.".format(user_pick,com_pick))
            com_count = com_count + 1
        elif com_pick == "바위":
            print("당신은 {}!, 컴퓨터는 {}! 당신이 이겼습니다.".format(user_pick,com_pick))
            user_count = user_count + 1
        else :
            print("당신은 {}!, 컴퓨터는 {}! 비겼습니다.".format(user_pick,com_pick))
    else :
        print("잘못 입력 하셨습니다.")

# 최종 스코어 보여주기!
print("끝!")
print("최종 스코어는 사용자:컴퓨터 = {}:{} 입니다".format(user_count,com_count))
