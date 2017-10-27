n=int(input())
A = []
while n>0:
    A.append(int(input()))
    n-=1

def bubblesort(A):
 for i in range(len(A)):
   for k in range(len(A)-1,i,-1):
     if (A[k]<A[k-1]):
       swap(A,k,k-1)
 print(A)

def swap(A,x,y):
   tmp = A[x]
   A[x] = A[y]
   A[y] = tmp
bubblesort(A)
