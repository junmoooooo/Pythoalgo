# def func(n):
#     if n == 3:
#         return
#
#     print(f'{n}의 세상에서')
#     func(n+1)
#     print(f'{n}의 세상에서 마무리')
#
# func(0)


a = 1

def func():
    a = 2
    print(a)
func()
print(a)


b = [1,2,3]

def func():
    b = [6,5,6]    # 이게없으면 [ 9,2,3 ]인데...
    b[0] = 9
func()

print(b)


#L   E   G   B



c = [1,2,3]
print(id(c))
def func(input_list):
    print(id(input_list))
    print(input_list)

func(c)


# set처리를 하면 아이디값이 분리된다.