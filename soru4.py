#Fibonacci dizisinin ilk 30 sayısını ekrana bastırma

def fibo(n):
    if n < 2:
        return False
    else:
        return fibo(n-1) + fibo(n-2)

for i in range(0,30,1): 
    print(fibo(i),end=" ")
