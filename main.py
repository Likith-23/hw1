def myfunction(n):
    for i in range(0, n + 1):
        print("First Loop")
    
    j = 1
    while j <= n:
        print("Second Loop", j)
        j = j * 2
    
    for i in range(0, 100):
        print("Third Loop")
myfunction(4)