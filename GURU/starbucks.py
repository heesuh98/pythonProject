def showMenu():
    print("=====2021 Starbucks Menu====")
    print("0. 주문종료")
    print(f"1.{menu1} : {price1}원")
    print(f"2.{menu2} : {price2}원")
    print(f"사이즈 : Tall +{tall}원 , Grande +{grande}원, Venti +{venti}원")
    print("==============================")
def selectMenu():
    global coffee
    global breakFlag
    global continueFlag
    menu = int(input("메뉴를 선택하세요: "))

    if menu == 1:
        print("%s를 선택하셨습니다." % menu1)
        coffee += price1
    elif menu == 2:
        print("%s를 선택하셨습니다." % menu2)
        breakFlag = True
    elif menu == 0:
        print("주문을 종료합니다.")
        breakFlag = True
    else:  # 잘못입력시
        print("잘못입력하였습니다")
        continueFlag = True

def selectSize():
    global total_price
    global coffee
    size = int(input("사이즈를 선택해주세요(1.tall, 2. grande, 3. venti :"))
    if size == 1:
        coffee += tall
        total_price += coffee
    elif size == 2:
        coffee += grande
        total_price += coffee
    elif size == 3:
        coffee += venti
        total_price += coffee
    else:
        print("잘못입력하였습니다.")
    print("현재 주문 금액 :%d\n" % total_price)

def payment():
    cash = int(input("현금을 넣어주세요: "))
    change = cash - total_price

    print("잔돈 %d 원입니다. 안녕히가십시오." % change)

if __name__ == "__main__":
    menu1 = "아메리카노"
    menu2 = "카페라떼"

    price1 = 4100
    price2 = 4600

    tall = 0
    grande = 500
    venti = 1000

    total_price = 0

    breakFlag = False

while True:
    continueFlag = False
    coffee = 0

    showMenu()
    selectMenu()

    if breakFlag == True:
        break
    if continueFlag == True:
        continue
    selectSize()
payment()



    # print("=====2021 Starbucks Menu====")
    # print(f"1.{menu1} : {price1}원")
    # print(f"2.{menu2} : {price2}원")
    # print(f"사이즈 : Tall +{tall}원 , Grande +{grande}원, Venti +{venti}원: ")
    # print("==============================")
    #
    # menu = int(input("메뉴를 선택하세요:"))
    #
    # if menu == 1:
    #     print("%s를 선택하셨습니다." %menu1)
    #     total_price += price1
    # elif menu ==2:
    #     print("%s를 선택하셨습니다." % menu2)
    #     total_price += price2
    # else: #잘못입력시
    #     print("잘못입력하였습니다")
    #
    # size = int(input("사이즈를 선택해주세요(1.tall, 2. grande, 3. venti"))
    # if size == 1:
    #     total_price += tall
    # elif size == 2:
    #     total_price += grande
    # elif size == 3:
    #     total_price += venti
    # else:
    #     print("잘못입력하였습니다.")
    # print("현재 주문 금액 :%d\n" % total_price)
    #
    # cash = int(input("현금을 넣어주세요: "))
    # change = cash - total_price
    #
    # print("잔돈 %d 원입니다. 안녕히가십시오." %change)