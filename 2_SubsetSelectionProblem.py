# 2. Problem Statement:
# Find all the subsets from a set of numbers whose sum is zero.

# Constraint: Subset size must be 3 to 6 only
# Set={-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4}

import random as r
Set         = set([-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4])
SetLB       = 3
SetUB       = 6
ResultList  = set()
Iterations  = 1000 

for i in range(Iterations):
    SetSize = r.randint(SetLB,SetUB)
    Chromosome = r.sample(list(Set), SetSize)
    Chromosome.sort()
    
    if sum(Chromosome) == 0:
        ResultList.add(tuple(Chromosome))


for r in ResultList:
	print (r)


print ("\nTotal Sets: ", len(ResultList))