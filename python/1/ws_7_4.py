
def fee(t,s):

    #주행요금 계산

    if s > 100:

        d = 100*170+(s-100)*85
    
    else:

        d = s*170

    #대여요금 계산

    b = (t//10)*1200

    #보험료 계산

    x,y = divmod(t,30)

    if y == 0: #대여시간이 30분으로 나누어 떨어지면
        
        c = 525 * x
    
    else: #30분으로 나누어 떨어지지 않으면

        c = 525 * (x+1) #30분 단위로 올려서 계산함
    
    return b+c+d

print(fee(600,50))
print(fee(600,110))




    
    
