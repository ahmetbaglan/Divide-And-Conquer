import random

def partition(l,p,n,e):
    if(n>=e or e - n == 1):
        return
    pivot = l[p]
    l[p], l[n] = l[n], l[p]
    i = n+1
    for j in range(n+1,e):
        if l[j]< pivot:
            l[i], l[j] = l[j], l[i]
            i+=1
    l[n], l[i-1] = l[i-1], l[n]
    return i-1


def quickSort(l,n,e):
    if n >= e:
        return
    pivot = random.choice(range(n,e))
    p = partition(l,pivot,n,e)
    if p == None:
        return
    quickSort(l,0,p)
    quickSort(l,p+1,e)

N = 0
a = range(N)
random.shuffle(a)
print a
quickSort(a,0,len(a))
# partition(a,len(a)-1,3,len(a))

print a