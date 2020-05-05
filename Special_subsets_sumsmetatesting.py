# Special subset sums: meta-testing

# for element in B
# assert element not in C

# 
#

def sum_set(A):
    n = len(A)
    summ = 0
    
    for i in range(n):
        summ += A[i]
        
def special_set(B, C):
    for element_B in B:
        for element_C in C:
            if element_B == element_C:
                ValueError
        
    if (sum_set(B) != sum_set(C) and (len(B) < len(C) or (len(B) > len(C) and sum_set(B) > sum_set(C)))):
        # assuming they're considerring only the B C permutation
        print(len())
    

    
    