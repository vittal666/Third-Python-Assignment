num = int(input("Enter a number to generate Fibonacci series : ")) 

def recur_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))

if num <= 0:  
   print("Please enter a number which is greater than 0")  
else:  
   print("\nFibonacci sequence : ")  
   for i in range(num):  
       print(recur_fibo(i))
