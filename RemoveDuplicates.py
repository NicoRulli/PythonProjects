class solution: 
    def func(a,b):
        listA = []
        listB = []
        
        for i in range(1,a):
            if a % i == 0:
                listA.append(i)

        for x in range(1,b):
            if b % x == 0:
                listB.append(x)
        
        test = listA + listB
        d = {}

        for i in test: 
            if i not in d: 
                d[i] = 1
            else: 
                d[i] += 1
        max = 0
        for i,v in d.items():
            if v > 1: 
                max = i
        
        return max
                
    print(func(70,15))