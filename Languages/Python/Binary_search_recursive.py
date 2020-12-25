import random
from math import floor

my_long_list = random.sample(range(1000000), 1000000)
def binary_search(l, value):
    l.sort()
    cl = l

    def recursive(cl):
        
        index =  cl[floor(len(cl) / 2)]
        if value > l[index]:
            
            cl = cl[floor(len(cl) /2): len(cl)]
            recursive(cl)
            print("Value higher than")

        if value < l[index]:
            
            cl = cl[0:floor(len(cl) / 2)]
            recursive(cl)
            print("Value lower than")

        if value == l[index]:
            answer = l[index]
            print("Founded: ", answer)

        if value > l[len(l) - 1] or value < l[0]:
            print("value not in the list")
        
    
    recursive(cl)

binary_search(my_long_list, 33333)
binary_search(my_long_list, 555555)
binary_search(my_long_list, 1)
binary_search(my_long_list, 999999)
binary_search(my_long_list, 500000)