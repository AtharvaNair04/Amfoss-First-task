def collatz(num):
    if num%2==0:
        res=num//2
    else:
        res=(3*num)+1
    print(res)
    return res
a=int(input("enter you number:"))
while a!=1:
    a=collatz(a)
