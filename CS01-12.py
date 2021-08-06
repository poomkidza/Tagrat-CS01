Num = int(input("Enter your loop:"))
Numtotal = []
for i in range(Num):
    data=int(input("Enter your number:"))
    Numtotal += [data]
    print(Numtotal)
Numtotal.sort(reverse=False)
print(Numtotal[0])
nvm = len(Numtotal)
print(Numtotal[nvm-1])