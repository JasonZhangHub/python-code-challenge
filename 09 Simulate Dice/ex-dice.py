import random

def roll_dice(*sides, simu_count = 1000000):
    
    result_all = []    
    for n in range(simu_count):
        result= 0
        for i in sides:
            result+=random.randint(1,i)
            
        result_all.append(result)
    
    #calculate the probability, count the numbers of appearance
    count = {}
    for i in result_all:
        if i in count.keys():
            count[i]+=1.0/len(result_all)
        else:
            count[i]=1.0/len(result_all)
            
    #sort a dictionary
    s = {k : '{:.3%}'.format(count[k]) for k in sorted(count)}
    print('\nOUTCOME\tPROBABILITY')
    return s


roll_dice(4,6,6)