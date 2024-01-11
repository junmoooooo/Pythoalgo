i = 1
while True:
    l, p, v = map(int, input().split())         # 입력값을 받고
    if p == 0 and l == 0 and v == 0:            # 0, 0, 0이 입력되면 반복문 종료
        break

    camping = (l * (v // p)) + min((v % p), l)  # 캠핑장을 사용할 수 있는 최대 일수
    # (휴가 일수 // 이용할수있는 연속하는 캠핑장일수 ) * 캠핑장을 최대로 사용할수 있는 일수
    # + 휴가일수 % 이용할수있는 연속하는 캠핑장일수 의 나머지와 캠핑장을 최대로 사용할수 있는 일수 중에 작은값
    print('Case {}:'.format(i), camping)
    i += 1