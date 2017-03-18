# 과제 1 - 맛집 고르기
import random

list_han = ["계절밥상","자연별곡","정원쌈밥"]
list_joong = ["양자강", "홍콩반점", "청룡각"]
list_il = ["니와스시", "칠분도초밥", "카모메식당"]

# 한식, 중식, 일식 중 한 가지 고르시오
right_input = False
while right_input == False :
    menu = input("한식, 중식, 일식 중 한 가지 고르시오 ")

    if menu == "한식":
        right_input = True
        print("{}을 선택하셨습니다. 추천 식당은 {} 입니다.".format(menu,random.choice(list_han)))
    elif menu == "중식":
        right_input = True
        print("{}을 선택하셨습니다. 추천 식당은 {} 입니다.".format(menu,random.choice(list_joong)))
    elif menu == "일식":
        right_input = True
        print("{}을 선택하셨습니다. 추천 식당은 {} 입니다.".format(menu,random.choice(list_il)))
    else:
        right_input = False
        print("다시 입력해주세요")
