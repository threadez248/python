##searching 
##Linear search






# from typing import List


# # # def linearSearch(ListofElements, searchElement):
# # #     for i in range(len(ListofElements)):
# # #         if (ListofElements[i] == searchElement):
# # #             return ("Value present")
# # #      else:
# # #            return("Vaule not found")
        
# # # ListofElements = [99,44,55,33,88,2]
# # # searchElement = 8

# # # print(linearSearch(ListofElements, searchElement))

# # def linearSearch(ListofElements, searchElement):
# #   Found = False
# #   print("length of List", len(ListofElements))
# #   for index1 in range(len(ListofElements)):
# #      if (searchElement == ListofElements[index1]):
# #         Found = True
# #   if (Found == True):
# #     print ("Found Element")
# #   else:
# #     print ("Not found")

# # SearchElement = 11
# # linearSearch(myListA, SearchElement)

# def LinearSearch(listofelements,searchelement):
#     for i in range(len(listofelements)):
#         if (listofelements[i] == searchelement):
#             print("value present")
#             return
#     else:
#         print("value not found")
        

# listA = [3,5,6,8,4]
# listofelements = listA

# LinearSearch(listofelements, 4)

##Binary Search

from typing import List


listA = [3,5,6,8,4]
# ListA = [2,4,6,8,9]

def binarySerch(ListofElements, searchElement):
    ListofElements = sorted(ListofElements)
    print(ListofElements)
    low = 0
    mid = 0
    upper = len(ListofElements) - 1

    while(low <= upper):
        mid = ( low + upper)// 2
        if ListofElements[mid] == searchElement:
            return ("Element found", ListofElements[mid], mid)
        else:
            if ListofElements[mid] < searchElement:
                low = mid + 1
            else:
                upper = mid - 1
    return("Element not found")



print(binarySerch(listA, 5))
        







