c  =  input('')
t  =  []
for x , y in zip(c, range(10,1,-1)):
    calcu = int(x) * y
    t.append(calcu) 
z  =  (sum(t) * 10) % 11    
print(z) 

c  =  input('')
t  =  []
for x , y in zip(c, range(11,1,-1)):
    calcu = int(x) * y
    t.append(calcu) 
z  =  (sum(t) * 10) % 11    
print(z) 
