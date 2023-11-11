def collatz(num):
    if num%2==0:
        val=num//2
    else:
        val=(3*num)+1
    print(val)
    return val
user_input = input("Give me a number: ")
while True:
    try:
        while user_input != 1:
            user_input = collatz(int(user_input))
    except ValueError:
        print("You must enter positive integer")
