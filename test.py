# 39
def print_numbers(a):
    b = []
    for i in range(0,a+1):
        if i % 2 != 0:
            b.append(i)
    return b
        
x = int(input("양수 입력: "))
result = print_numbers(x)
print(*result)


# 40
def print_number(i):
    if i % 3 == 0:
        return i
    else:
        return None
    

a = int(input("숫자 입력: "))
result = print_number(a)
print(result)


# 41
def print_numbers(*args):
    return max(args), min(args)

b = map(int,input("숫자 입력: ").split())
result = print_numbers(*b)
print(result)


# 42 (39번 문제와 동일)
def print_numbers(i):
    b = []
    for u in range(0,i+1):
        if u % 2 != 0:
            b.append(u)
    return b
        
x = int(input("양수 입력: "))
result = print_numbers(x)
print(*result)

# 43
def print_number(i):
    u = 1
    while i > 0:
        u *= i
        i-=1
    return u
        
    
n = int(input("정수입력: "))
result = print_number(n)
print(result)


# 44
def print_numbers(a,b):
    if (2<= a <=9) and (2<= b <=9):
        c = min(a,b)
        d = max(a,b)

        u = 0
        for x in range(c,d+1):
            for y in range(c,d+1):
                if x*y >= 30:
                    u += x*y
    else:
        u = "잘못입력하였습니다."
    return u
                
i,j = map(int,input("숫자입력: ").split())
result = print_numbers(i,j)
print(result)


# 45
def print_numbers(*b):
    return sum(b)

a = [1,2,3,4,5]
result = print_numbers(*a)
print(result)