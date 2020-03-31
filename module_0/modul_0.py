import random
count = 1
num_m = random.randint(1, 100)
num_answ = random.randint(1, 100)
while num_answ != num_m:
    centr = (num_answ + num_m)//2
    if centr == num_m:
        count +=1
        break
    elif centr>num_m:
        num_answ = centr -1
        count += 1
    elif centr<num_m:
        num_answ = centr + 1
        count += 1
        
print('Код угадан за {} раз'. format(count))
