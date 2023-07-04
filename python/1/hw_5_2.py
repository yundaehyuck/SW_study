
def leap_year(year):

    cond1 = (year % 4 == 0) and (year % 100 != 0)

    cond2 = year % 400 == 0

    if cond1 or cond2:

        return f'{year}년은 윤년입니다.'
    
    else:

        return f'{year}년은 윤년이 아닙니다.'
    

print(leap_year(2021))
print(leap_year(2020))
