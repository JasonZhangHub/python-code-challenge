import random
import time

def waiting_game():
    wait_time = random.randint(2, 4)
    print("Your target waiting time is {wait_time} seconds".format(wait_time = wait_time))
    
    
    input("------ Press Enter To Begin -------")
    t0 = time.time()
    
    input('\n...Press Enter again after {wait_time} seconds...'.format(wait_time= wait_time))
    t1 = time.time()
    
    elapsedTime = t1 - t0
    if elapsedTime > wait_time:
        print("Elapsed time: {elapsedTime} seconds. ( {time_gap}) seconds too slow"\
              .format(elapsedTime = elapsedTime, 
                      time_gap = elapsedTime - wait_time))
    if elapsedTime == wait_time:
        print("Elapsed time: {elapsedTime} seconds. Right on target")
    if elapsedTime < wait_time:
        print("Elapsed time: {elapsedTime} seconds. ( {time_gap}) seconds too fast"\
              .format(elapsedTime = elapsedTime, 
                      time_gap = wait_time - elapsedTime))
    
    return None
    
if __name__ == '__main__':
    waiting_game()