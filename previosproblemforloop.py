x = int(input("Enter a number: "))
state = False
for r in range(1, x):
    for p in range(1, 6):
        if r ** p == x:
            state = True
            break
    if state:
        break
if state:
    print(f"The pair for the given integer is {p} and {r}")
else:
    print(f"There is no such pair of integer {x}")
