# PROBLEM 1
# MULTIPLE OF 3 OR 5

_sum = 0
for i in range(1,10):
    if (i%3 == 0) or (i%5 == 0):
        _sum += i
print(_sum)

#PROBLEM 2
# Sum of even fibonacci numbers lesser than 4 million
val = 1
prev = 0

_sum = 0
_step = 0
while(val < 4000000):
    temp = val
    val += prev
    prev = temp
    _step += 1
    if val%2 == 0:
        _sum += val
    
    print("Step : " , _step,"Val : " , val,"Sum : " , _sum)

print("Sum of Even Fibonacci Numbers less than 4 million is ",_sum)

# PROBLEM 3
# LARGEST PRIME FACTOR

num = 600851475143
div = 2
prime_factors = []
while(num != 1):
    if num%div == 0:
        if div not in prime_factors:
            prime_factors.append(div)
        num/=div
        continue
    div+=1
print(prime_factors)

# PROBLEM 4
# LARGEST PALINDROME PRODUCT

def check_palindrome(_snum):
    if len(_snum)%2 != 0:
        print("to be a palindrome number , it must have even digit")
        return 0
    else:
        n = len(_snum)
        mid = int(n/2)
        for i in range(mid):
            if _snum[i] != _snum[n-1-i]:
                return 0
        return 1

pal_nums = [i*x for i in range(100,1000) for x in range(100,1000) if check_palindrome(str(i*x))]
sorted(pal_nums)[len(pal_nums)-1]

# PROBLEM 5
# SMALLEST MULTIPLE

ans = 1
for i in range(2,21):
    ans = ans * i

print(ans)

