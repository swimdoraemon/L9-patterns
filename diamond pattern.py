
n = int(input("enter the number of rows: "))
a = 1
for i in range(n):
    for j in range(i+1):
        print(a, end="")
        a = a+1
    print()

