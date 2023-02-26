# Here I am going to practice if statement along with modulo statements.
Num = int(input("Enter your number :"))
x = Num % 2
y = Num % 4
if x == 0:
    print("Even")
else:
    print("Odd")

if y == 0:
    print("Wow this number is a multiple of 4")
else:
    print("Oof this number sucks!!!")
