n = int(input("Enter a number: "))
ans = 1
k = 0
while n != 0:
    ans = ans * n
    n = n - 1
    k = k + 1
print(str(k) + "! = " + str(ans))
