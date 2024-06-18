#quick sort
#if i found smaller element than pivot then increase j by 1 and swap it by i
#if i found bigger element then pivot i will do nothing and increment i
def divide(l,low,high):
    p=l[high]
    pi=high
    j=low-1
    for i in range(low,high):
        if l[i]<=p:
            j+=1
            l[i],l[j]=l[j],l[i]
    j+=1
    l[j],l[pi]=l[pi],l[j]
    pi=j
    return pi
def Quick_Sort(l,low,high):
    if low<high:
        pi=divide(l,low,high)
        Quick_Sort(l,low,pi-1)
        Quick_Sort(l,pi+1,high)
    return

if __name__=="__main__":
    l=list(map(int,input("enter the elements to be sorted").split()))
    Quick_Sort(l,0,len(l)-1)
    print("sorted array",l)    