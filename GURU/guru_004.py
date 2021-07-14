#구구단

dan = int(input('단을 입력하세요:'))

for i in range(1,10):
    result = dan*i
    print("%d x %d = %d" %(dan, i, result))