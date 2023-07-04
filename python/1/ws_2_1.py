
#첨부파일 계수

a = 3

b = 6

c = -5

root1 = (-b + ((b**2) - 4*a*c)**(1/2))/(2*a)
root2 = (-b - ((b**2) - 4*a*c)**(1/2))/(2*a)

#소수점 4번째 자리에서 반올림
root = (round(root1,3),round(root2,3))

print(root)
