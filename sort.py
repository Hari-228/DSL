def selection(arr):
    a=arr.copy()
    n=len(a)
    for i in range(0,n-1):
        for j in range(i+1,n):
          if   a[i]>a[j]:
             a[i],a[j]=a[j],a[i]
    return a
def bubble(arr):
   a=arr.copy()
   n=len(a)
   for i in range(n-2,-1,-1):
      for j in range(0,i+1):
         if a[j]>a[j+1]:
          a[j],a[j+1]=a[j+1],a[j]
   return a
n=int(input("Enter number of employees"))
sal=[]
for _ in range(n):
   sal.append(float(input("Enter salary")))
ss=bubble(sal)
print ("Salaries sorted in Ascending order:",ss)
print("Top 5 salaries:",sorted(sal,reverse=True)[:5])


