
s = '@#~I NeVEr DrEamEd AbouT SuCCeSs, i woRkEd foR iT.!>!'

#특수문자 제거

s = s[3:-3]


#첫번째 대문자 I는 그대로 가져오고 나머지는 전부 소문자로 바꿔서
# 둘을 더해 새로운 s로 만든다

s = s[0] + s[1:].lower()

print(s)
