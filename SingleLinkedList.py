class Node:
    def __init__(self, data = None,next = None):
        """
            @params:
                >data :int --> data of the node
                >next :Node --> pointer to the next node.
            
            @Node:
                .data : contains the value of the node
                .next : conatins a copy of next node
        """
        self.data = data
        self.next = next

class SingleLinkedList:
    def __init__(self):
        """
            @params: No paramters
            Creates a empty linked list

            @SingleLinkedList:
                .head :Node : holds the information of first node  i.e., root
                .length : int : holds the number os elements in list

        """
        self.head = None
        self.length = 0
    
    def insert(self, data = None):
        """
            @params:
                >data: int --> value to be stored
            
            Inserts the node at the beginning
        """
        print(f"Inserting {data}  ==> ",end = "")
        if data is None:
            return 
        self.head = Node(data, self.head)
        self.length += 1
        print("Done.\n")
    def delete(self, data = None):
        """
            @params:
                >data: int value to be deleted
            
            Deletes the first occurance of node containing data
        """
        print(f"Deleting {data} ==> ", end = "")
        if data is None:
            return
        # Check if the list is empty
        if self.head is None:
            print(f"Not Done.\nReason :{self} is empty")
            return
        temp = self.head
        # Base case if it is first node
        if temp.data == data:
            self.head = temp.next
            temp = None
            print(f"Done.\nElement {data} is deleted.")
            self.length -= 1
            return 
        while temp:
            if temp.data == data:
                prev.next = temp.next
                temp = None
                print(f"Done.\nElement {data} is deleted.")
                self.length -= 1
                return
            prev, temp = temp, temp.next
        print(f"Not Done.\nReason: Element {data} not found.")
        temp = None
    def display(self):
        if self.head is None:
            print(f"{self} is Empty")
            return
        temp = self.head
        print(f"Elements Of {self} are:")
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print()
    def __repr__(self):
        return "Single Linked List"
    def __len__(self):
        return self.length

if __name__ == "__main__":
    my_list = SingleLinkedList() # creates a empty linked list
    #Now Perform some operations on our list
    while True:
        print("\nOperations On Single Linked List\n\n1.Insert\n2.Delete\n3.Display\n4.Length\n5.Exit\n")
        op = int(input("Enter Your Choice Bruh:"))
        if op == 1:
            ele = int(input("\nEnter Elememt to insert:"))
            my_list.insert(ele)
        elif op == 2:
            ele = int(input("\nEnter Elememt to delete:"))
            my_list.delete(ele)
        elif op == 3:
            my_list.display()
        elif op == 4:
            print(f"\n{my_list} has {my_list.__len__()} elements.")
        elif op == 5:
            print("\n\tOkay Bye!!\n\n")
            break
        else:
            print("\nSarigga Enter Cheyyi Bro\n")
    print("Have a good time.")



