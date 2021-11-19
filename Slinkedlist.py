#Sigle Linked List

class Node:
    def __init__(self, dataval=None):
        self.data = dataval
        self.next = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def traverse(self):
        tempValue = self.headval
        print(self.headval)
        while tempValue is not None:
            print(tempValue.data)
            print(tempValue)
            tempValue = tempValue.next

    def insertAtBeginning(self, newdata):
        newNode = Node(newdata)
        newNode.next = self.headval
        print(self.headval)
        self.headval = newNode

    def insertAtEnd(self, newdata):
        newNode = Node(newdata)
        if self.headval is None:  # If list is empty
            self.headval = newNode
            return

        tempValue = self.headval
        while tempValue.next is not None:
            tempValue = tempValue.next
        tempValue.next = newNode

    def insertAtBetween(self, valueBefore, newdata):
        newNode = Node(newdata)

        tempValue = self.headval
        while tempValue.data is not valueBefore:
            tempValue = tempValue.next

        newNode.next = tempValue.next
        tempValue.next = newNode

    def remove(self, value):
        tempValue = self.headval

        if value == tempValue.data:
            self.headval = tempValue.next
            tempValue.next = None
        else:
            while tempValue.next.data is not value:
                tempValue = tempValue.next

            tempValue.next = tempValue.next.next


slist1 = SLinkedList()
slist1.insertAtBeginning("D1")
slist1.insertAtEnd("D3")
slist1.insertAtBetween("D1","D2")
print(slist1.traverse())

print(slist1.traverse())

print(slist1.headval)
# secondNode = Node("B")
# thirdNode = Node("C")
# fourthNode = Node("D")
#
# slist.headval = firstNode
# slist.headval.next = secondNode
#
# secondNode.next = thirdNode
#
# thirdNode.next = fourthNode

# slist = SLinkedList()

# list1 = ["a", "b", "c", "d", "e"]

# prev_value = None

# for i in range(len(list1)):
#     newNode = Node(list1[i])

#     if i == 0:
#         slist.headval = newNode
#     else:
#         prev_value.next = newNode

#     prev_value = newNode


# slist.traverse()

# slist.insertAtBeginning("AA")
# slist.insertAtEnd("ZZ")

# # slist.remove("B")
# # print("After insertion")
# slist.traverse()

# # Find the value of Kth node