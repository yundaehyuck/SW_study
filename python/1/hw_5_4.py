
def fn_d(n):

    return n + sum(map(int,str(n)))


print(fn_d(91))

"""def fn_d(n):

    number = str(n)

    for i in number:

        n += int(i)
    
    return n"""

def is_selfnumber(n):

    for i in range(1,n+1):

        if fn_d(i) == n:

            return False
    return True

#여러개를 검사하고 싶을때 할때마다 완전 탐색하면 비효율적이니까
#한번에 여러개를 찾아놓는 전략?
"""
def is_selfnumber(n):

    number_set = set(range(1,10001))
    gen_set = set()

    for i in range(1,10001):

        gen_set.add(fn_d(i))

    self_set = set()
    self_set = number_set - gen_set

    return n in self_set
"""

#비슷한 논리로 짜본?
"""
self_set = set()

def is_selfnumber(n,self_set):

    if n in self_set:

        return True
    
    else:

        for i in range(1,n+1):

            if fn_d(i) == n:

                return False,self_set
        
        self_set.add(n)

        return True
"""

print(is_selfnumber(1))
print(is_selfnumber(6))
print(is_selfnumber(15))
print(is_selfnumber(31))
