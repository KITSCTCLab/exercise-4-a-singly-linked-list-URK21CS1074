from typing import Optional


solution = []

class Node:
    """
    Provide necessary documentation
    """

    def __init__(self, data=None, next=None):
        """
        Provide necessary documentation
        """
        self.data = data
        self.next = next


class LinkedList:
    """
    Provide necessary documentation
    """

    def __init__(self):
        """
        Initialize the head
        """
        self.head = None

    def insert_at_end(self, data):
   
        """
        Insert node at end of the list
        :param data: integer data that will be used to create a node
        """
        # Write code here
        
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            
            monk = new_node
            monk.next = self.head
            self.head = monk

        
        
    def status(self):
        head = self.head
        while head:
            if head.data == None:
                break
            print(head.data, end="")
            head = head.next
        """
        It prints all the elements of list.
        """
        # write code here


class Solution:
    """
    Provide necessary documentation
    """

    def addTwoNumbers(self, first_list: Optional[LinkedList], second_list: Optional[LinkedList]) -> Optional[
        LinkedList]:
        """
        :param first_list: Linkedlist with non-negative integers
        :param second_list: Linkedlist with non-negative integers
        :return: returns the sum as a linked list
        """
       
        def fill_num(node, array=[]):
            while node:
                array.append(str(node.data))
                node = node.next
            return ''.join(array)
            
        
        solution = []
        
        first_num = fill_num(first_list.head,[])
        second_num = fill_num(second_list.head,[])
        result = str(eval("{}+{}".format(first_num,second_num)))
        
        for char in result[::-1]:
            solution.append(int(char))
        
        
            
        return solution
        # result_node = Node()
        # monk = result_node
        # first_run = True
        
        
        # while result_solution is not None:
            

        #     temp_node = Node(result_solution.data)
        #     temp_node.next = monk
        #     monk = temp_node
        #     result_solution = result_solution.next
        #     if result_solution:
        #         solution.append(result_solution.data)
            

       
        # linked_list = LinkedList()
