tab = []
i = 0
j= 0
sup = 0

n=len(tab)
if i in range (1, n-1):
	s = tab[i]
	j = i - 1
while j >= 0 and tab[j] > s:
	tab[j + 1] = tab[j]
	j = j - 1

tab[j + 1] = sup
