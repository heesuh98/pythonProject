coffee = 0

coffee = int(input("커피종류?(1.블랙, 2. 설탕, 3.일반: "))


def coffee_machine(num_1):
    print()
    print("뜨거운물을 준비")
    print("종이컵 준비")

    if num_1 == 1:
        print("자동으로 블랙커피 탄다")
    elif num_1 == 2:
        print("설탕커피를 준비한다")
    elif num_1 == 3:
        print("일반커피를 준비한다")
    else:
        print("아무거나 준비")

    print("손님 커피 여기있습니다")


coffee_machine(coffee)
