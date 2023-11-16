def collatz(num):
    if num%2==0:
        res=num//2
    else:
        res=(3*num)+1
    print(res)
    return res
a=input("Give a number: ")
while True:
    try:
        while a!=1:
            a=collatz(int(a))
    except ValueError:
        print("Enter positive integer")
