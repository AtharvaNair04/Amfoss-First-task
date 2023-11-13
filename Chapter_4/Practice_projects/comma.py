def comma(items):
    if not items:
        print("Empty list")
    elif len(items)==1:
        print(items[0])
    else:
        for i in range(len(items)-1):
            print(items[i]+",",end=' ')
        print("and"+items[-1])
spam=[]
while True:
    my_list=input("Enter an item (or type 'stop' to stop the code): ")
    if my_list=='stop':
        break
    spam.append(my_list)
comma(spam)
