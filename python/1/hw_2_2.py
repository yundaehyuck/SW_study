orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

order_list = orders.split(',')

#총 주문 수
total_order = len(order_list)

#중복 제거하고 리스트 변환

unique_list = list(set(order_list))

#내림차순 정렬

unique_list.sort(reverse=True)

print(total_order) #총 주문 수
print(unique_list) #고유 주문 리스트
