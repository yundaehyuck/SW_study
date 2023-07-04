
salt_list = []
salt_list = []

count = 0

while count < 5:

    s = input('혼합할 소금물의 퍼센트 농도와 양을 한 칸씩 띄어써서 입력하고(최대 5개) 혼합할려면 Done을 입력하세요. : ')

    if s == 'Done':

        break
    
    else:

        con,gram = map(float,s.split())

        salt = (con * gram) / 100

        salt_list.append((salt,gram))

        count += 1

if count == 5:

    input('최대 개수만큼 입력했으므로 Done을 입력하면 소금물을 혼합합니다.')

mix_salt = 0
mix_gram = 0

for salt,gram in salt_list:

    mix_salt += salt
    mix_gram += gram
  

mix_con = round((mix_salt/mix_gram)*100,2)
round_mix_gram = round(mix_gram,2)

print(f"농도:{mix_con}, 소금물 양:{round_mix_gram}")








