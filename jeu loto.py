
from numpy.random import randint
import numpy as np

y = int(input("Seed:"))
n = int(input("Entrez le nombre de tirages que vous voulez:"))

np.ramdom.seed(y)

for i in range (n)
    s= np.ramdom.choice(range(1,45),5, replace= false)
    s = list(s)
    print("Le tirage est :",s)




