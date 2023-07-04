orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

order_list = orders.split(',')

order_dict = {}

ice = 0

for coffee in order_list:

    if '아이스' in coffee:

        ice += 1

    order_dict[coffee] = order_dict.get(coffee,0) + 1

print(ice) #아이스 음료 주문 수
print(order_dict) #메뉴별 주문 수
