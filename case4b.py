# function
def merge(list1, list2): 
      
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))] 
    return merged_list 
      
# Driver code 
list1 = [4,3,5,1,2] 
list2 = ['F', 'C', 'D', 'B', 'A']
# sorting list
list1.sort()
list2.sort() 
print(merge(list1, list2))