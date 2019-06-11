def power(x):
    return x * x
    
def power2(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s  
     
print power(5)
print power2(5,3)