def insertion_sort(nlist):
    for i in range(1, len(nlist)):
        currentvalue=nlist[i]
        position=i

        while i>0 and nlist[position-1]>currentvalue:
            nlist[position]=nlist[position-1]
            position=position-1

        nlist[position]=currentvalue
        
nlist = [14,46,43,27,57,41,45,21,70]
insertion_sort(nlist)
print(nlist)
