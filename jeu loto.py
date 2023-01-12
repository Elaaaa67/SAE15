from numpy.random import randint
import numpy as np

tab= [0, 0, 0, 0, 0]
#y = int(input("Seed:"))


np.random.seed(0)




#tri cocktail
def cocktailSort(a):
    swapped = True
    n = len(a)
    start = 0
    end = n-1
    while (swapped==True):

        swapped = False

        for i in range(start,end):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        if (swapped == False):
            break

        swapped = False

            # move the end point back by one, because
            # item at the end is in its rightful spot
        end = end - 1

            # from right to left, doing the same
            # comparison as in the previous stage
        for i in range(end - 1, start - 1, -1):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

            # increase the starting point, because
            # the last stage would have moved the next
            # smallest number to its rightful spot.
            start = start + 1
    return a
        # Driver code to test above



if __name__ == '__main__':
    x = int(input("Entrez le nombre de tirages que vous voulez:"))
    for i in range(x):
        a = np.random.choice(range(1, 45), 5, replace=False)
        a = list(a)
        print("Le tirage est :", a)
        print("Tirage triée:",cocktailSort(a))
