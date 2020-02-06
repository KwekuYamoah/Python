from random import random



def simNtoss(n):
    heads=0
    for i in range(n):
        if random() < 0.5:
            heads= heads + 1
    print("There were {0} head, meaning a proportion of {1:0.2%}".format(heads,heads/n))
    
    


   
    
   
