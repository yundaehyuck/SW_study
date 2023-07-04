
side_list = list(map(int,input('삼각형의 세 변을 한 칸씩 띄어쓰면서 입력하세요 : ').split()))

#오름차순 정렬

side_list.sort()

#일반삼각형인지 판단

if side_list[-1] < (side_list[0] + side_list[1]):

    if (side_list[2] == side_list[1]) and (side_list[1] == side_list[0]):

        print("정삼각형")
    
    elif (side_list[2] == side_list[1]) or (side_list[1] == side_list[0]) or (side_list[0] == side_list[2]):

        print("이등변삼각형")

    elif (side_list[-1])**2 == ((side_list[0])**2 + (side_list[1])**2):

        print("직각삼각형")
    
    else:

        print("삼각형")

else:

    print("삼각형 아님")
