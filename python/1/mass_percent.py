
cnt = 1

comb_salt = 0

comb_mass = 0

while cnt <= 5: #최대 5개까지 소금물 섞기 가능

    s = input(f'{cnt}.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오:')

    if s == 'Done':

        break
    
    else:
        #농도와 양으로 분리

        percent,mass = s.split()

        #단위를 제거하고 숫자로 변환

        percent = float(percent[:-1])
        mass = float(mass[:-1])

        #소금의 양을 구한다

        salt = (percent*mass)/100

        #혼합시킨다

        comb_salt += salt
        comb_mass += mass

        cnt += 1

if cnt == 6:
    
    s = input('최대 개수를 입력하셨습니다. Done을 입력하면 혼합합니다. :')

comb_percent = round((comb_salt/comb_mass)*100,2)
comb_mass = round(comb_mass,2)

print(s)
print(f"{comb_percent}% {comb_mass}g")


