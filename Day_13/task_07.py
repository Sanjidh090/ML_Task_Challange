with open('buf.txt','w') as f:
    import time 
    start = time.time()
    [f.write(str(i)+'\n') for i in range(10**6)]
    print(time.time()-start)
