def is_odd(number):
 if number%2 == 1: #2로 나누었을 때 1이면 홀수이다.
    return True
 else:
    return False

print(is_odd(3))
# True
print(is_odd(4))
# False


def avg_numbers(*args):
 result = 0
 for i in args:
    result += i
 return result/len(args)

print(avg_numbers(1, 2))
# 1.5
print(avg_numbers(1,2,3,4,5))
# 3.0

def fib(n):
    if n == 0 : return 0          # n이 0일 때는 0을 반환
    if n == 1 : return 1          # n이 1일 때는 1을 반환
    return fib(n-2) + fib(n-1)    # n이 2 이상일 때는 그 이전의 두 값을 더하여 반환

for i in range(10):
    print(fib(i))