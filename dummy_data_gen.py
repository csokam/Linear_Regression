import numpy as np
from numpy.random import randint

f=open('data.csv', 'w')
f.write('Study_time(min),Score\n')

for i in range(1,50):
    time=np.random.randint(30,501)
    score=int(round(time/randint(5,10)+randint(1,25),0))
    f.write(str(time)+','+str(score)+'\n')

f.close()