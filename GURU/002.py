#학생 성적 관리 프로그램
a = input('이름 입력 :')
b = int(input('학번입력:'))
c = int(input('국어점수 입력:'))
d = int(input('수학점수 입력:'))
e = int(input('영어점수 입력:'))
average = (c+d+e)/3


print('이름 : %s' %a)
print('학번 : %d ' %b)
print('국어점수 : %d' %c)
print('수학점수 : %d' %d)
print('영어점수 : %d' %e)
print('평균점수 : %.2f' %average)
