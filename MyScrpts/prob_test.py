import random as r
x = ['A','B',"C",'D','E']
prob = [15, 35, 20, 10, 20 ]
win = 0

def test():
    pr = r.random()*100
    probsum = 0
    for i in range(len(prob)):
        probsum += prob[i]
        if(pr <= probsum):
            #print('{} <= {}'.format(pr, probsum))
            return i
        #else:
            #print('{} > {}'.format(pr, probsum))

for i in range(100):
    t1 = x[test()]
    t2 = x[test()]
    print(t1+t2)
    #if (t1 == 'A' and t2 == 'E') or (t1 == 'E' and t2 == 'A'):
    #FOR 3 SYMBOLS USE 'A' in t1+t2+t3 and 'B' in t1+t2+t3 and 'C' in t1+t2+t3
    if(t1+t2 == 'AE' or t1+t2 == 'EA'):
        print('t1 is {}, t2 is {}'.format(t1, t2))
        win+=1
print (win/100)








