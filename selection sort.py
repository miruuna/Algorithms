def selection_sort(nlist):
    for fillslot in range(len(nlist)-1, 0,-1):
        maxpos=0
        for i in range(1,fillslot+1):
            if nlist[i]>nlist[maxpos]:
                maxpos=i
        a=nlist[fillslot]
        nlist[fillslot]=nlist[maxpos]
        nlist[maxpos]=a
nlist = [14,46,43,27,57,41,45,21,70]
selection_sort(nlist)
print(nlist)
