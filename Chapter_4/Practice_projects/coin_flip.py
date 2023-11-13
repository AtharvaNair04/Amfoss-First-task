import random
def generate_coin_flips():
    coin_flips=[]
    for i in range(100):
        random_number=random.randint(0,1)
        if random_number==0:
            coin_flips.append('H')
        else:
            coin_flips.append('T')  
    return coin_flips
def has_streak(flips,streak_length):
    for i in range(len(flips)-streak_length+1):
        is_streak=True
        for j in range(1,streak_length):
            if flips[i+j]!=flips[i]:
                is_streak=False
                break
        if is_streak:
            return True
    return False 
numberOfStreaks=0
for experimentNumber in range(10000):
    coin_flips=generate_coin_flips()
    if has_streak(coin_flips,6):
        numberOfStreaks+=1
print('Chance of streak: %s%%'%(numberOfStreaks/100))
