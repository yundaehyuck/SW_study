
def move_tower(N, start, to, via):
    if N == 1:
        print("{}번 원반을 {}번 기둥에서 {}번 기둥으로 옮깁니다.".format(N, start, to))
    else:
        move_tower(N-1, start, via, to)
        print("{}번 원반을 {}번 기둥에서 {}번 기둥으로 옮깁니다.".format(N, start, to))
        move_tower(N-1, via, to, start)

def hanoi(N):

    move_tower(N,'A','C','B')


hanoi(8)

