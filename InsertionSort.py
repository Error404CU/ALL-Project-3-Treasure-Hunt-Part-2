List1 = [8,7,1,0,4,2,4,10]

def insertion_sort(List1):
    #starts at 1 so it can compare an element to the left of it (0)
    for index in range(1,len(List1)):
        Cvalue = List1[index]
        # -1, the element in the list left to the index
        j = index - 1
        while j >= 0:                       # J needs to stay in positive numbers for the sake of this list
            #whatever number is j
            if Cvalue < List1[j]:
                #is to the right of j
                List1[j+1] = List1[j]   #Number in slot J becomes the number in j + 1 (Cvalue)
                List1[j] = Cvalue       #Number in slot J+1 becomes the number in J
                j = j - 1
                print List1
            else:
                break                       #No swapping needs to occur
insertion_sort(List1)
print List1

