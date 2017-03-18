#과제 5 - 에러 나지 않는 구구단
# 구구단이라는 함수를 만들자!
    
def gogodan():
    num = input("몇 단을 출력하시겠습니까? ")
    try :
        if int(num) >=2 and int(num)<=9 :
            for a in range(1,10):
                print("{} * {} = {}".format(num,a,int(num)*a))
        else :
            print("2에서 9사이 숫자만 입력해주세요.")
            return(gogodan())
    except :
        print ("2에서 9사이 숫자만 입력해주세요.")
        return gogodan()
#구구단 실행!
gogodan()
