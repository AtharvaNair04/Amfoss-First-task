def collatz(num):
    if num%2==0:
        val=num//2
    else:
        val=(3*num)+1
    print(val)
    return val
user_input=int(input("enter you number:"))
while user_input!=1:
    user_input=collatz(user_input)
