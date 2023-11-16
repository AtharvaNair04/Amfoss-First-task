import random
import time
def multi_quiz():
    num_Q=10
    num_T=3
    limit=8
    def stop_quiz():
        stop=input("Stop the quiz?(yes/no):").lower()
        return stop=='yes'
    for q_no in range(1,num_Q+1):
        if stop_quiz():
            print("Quiz stopped.")
            break
        n1=random.randint(0,9)
        n2=random.randint(0,9)
        correct=n1*n2
        print(f"Question{q_no}:{n1}x{n2}=?")
        start=time.time()
        for try_num in range(1,num_T+1):
            answer=input("Your answer:")
            if time.time()-start>limit:
                print("Time is up! Next Question.")
                break
            try:
                answer=int(answer)
            except ValueError:
                print("Please enter a valid number.")
                continue
            if answer==correct:
                print("Correct!")
                time.sleep(1)
                break
            else:
                print(f"Incorrect!{n1}x{n2}={correct}.You have {num_T-try_num} tries left.")
        print()
multi_quiz()
