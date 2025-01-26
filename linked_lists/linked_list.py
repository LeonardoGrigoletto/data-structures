from typing import Any
import copy

class Node:
    def __init__(self, value: Any):
        self.value: Any = value
        self.next: Node = None


class LinkedList:
    def __init__(self, value: Any) -> None:
        initial_node: Node = Node(value=value)
        self.head: Node = initial_node
        self.tail: Node = initial_node
        self.length = 1

    def print_list(self) -> None:
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value: Any) -> Node:
        new_node: Node = Node(value=value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return new_node
    
    def prepend(self, value: Any) -> Node:
        new_node: Node = Node(value=value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        return new_node

    def pop_first(self) -> Node:
        if self.length == 0:
            return None
        elif self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return popped_node
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            self.length -= 1
            return popped_node
    
    def pop(self) -> Node:
        if self.length == 0:
            return None
        elif self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return self.head
        else:
            pre = self.head
            temp = self.head.next
            while temp.next is not None:
                pre = temp
                temp = temp.next
            popped_node = temp
            pre.next = None
            self.tail = pre
            self.length -= 1
            return popped_node
    
    def get(self, index: int) -> Node:
        if self.length == 0:
            return None
        if index < 0 or index >= self.length:
            return None
        if index == self.length - 1: # Trying to improve performance. Big O remains the same
            return self.tail
        if index == 0:               # Trying to improve performance. Big O remains the same
            return self.head
        temp = self.head
        for _ in range(0, index):
            temp = temp.next
        return temp

    def set_value(self, index: int, value: Any) -> Node:
        temp = self.get(index=index)
        if temp is not None:
            temp.value = value
            return temp
        return None     

    def insert(self, index: int, value: Any) -> Node:
        new_node = Node(value=value)
        if index < 0 or index > self.length:
            return None
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return new_node
        if index == 0:
            return self.prepend(value=value)
        if index == self.length:
            return self.append(value=value)
        temp = self.get(index=index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return new_node

    def remove(self, index: int) -> Node:
        if index < 0 or index >= self.length:
            return None
        if self.length == 0:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index=index - 1)
        node_to_remove = prev.next
        prev.next = node_to_remove.next
        node_to_remove.next = None
        self.length -= 1
        return node_to_remove

    def reverse(self) -> None:
        current = self.head
        self.head = self.tail
        self.tail = current
        after = current.next
        before = None
        for _ in range(self.length):
            after = current.next
            current.next = before
            before = current
            current = after

    def partition_list(self, x: int):
        if self.length == 0 or self.head is None:
            return None
        dummy_node_gt = Node(0)
        dummy_node_lt = Node(0)
        last_node_gt = dummy_node_gt
        last_node_lt = dummy_node_lt
        current_node = self.head
        for _ in range(self.length):
            if current_node.value < x:
                last_node_lt.next = current_node
                last_node_lt = current_node
            else:
                last_node_gt.next = current_node
                last_node_gt = current_node
            current_node = current_node.next
        last_node_gt.next = None
        last_node_lt.next = None
        last_node_lt.next = dummy_node_gt.next
        self.head = dummy_node_lt.next
    
    def has_loop(self) -> bool:
        if self.length == 0 or self.length == 1:
            return False
        slow_pointer = self.head
        fast_pointer = self.head
        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if fast_pointer == slow_pointer:
                return True
        return False
    
    def find_middle_node(self) -> Node:
        if self.head is None or self.tail is None:
            return None
        slow_pointer = self.head
        fast_pointer = self.head
        while fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if fast_pointer is None:
                break
        return slow_pointer

def find_kth_from_end(linked_list: LinkedList, k: int) -> Node:
    slow_pointer = linked_list.head
    fast_pointer = linked_list.head
    for i in range(k):
        if fast_pointer is None:
            return None
        fast_pointer = fast_pointer.next
    while fast_pointer is not None:
        fast_pointer = fast_pointer.next
        slow_pointer = slow_pointer.next
    return slow_pointer


if __name__ == "__main__":
    # print("--- Appending ---")
    # linked_list = LinkedList(value=4)
    # linked_list.append(value=3)
    # linked_list.append(value=9)
    # linked_list.append(value=10)
    # linked_list.append(value=12)
    # linked_list.print_list()

    # print("--- Popping ---")
    # linked_list.pop()
    # linked_list.pop()
    # linked_list.pop()
    # linked_list.pop()
    # linked_list.pop()
    # linked_list.print_list()

    # print("--- Prepending ---")
    # linked_list = LinkedList(value=4)
    # linked_list.prepend(value=3)
    # linked_list.prepend(value=2)
    # print("Head: ", linked_list.head.value)
    # print("Tail: ", linked_list.tail.value)
    # linked_list.print_list()

    # print("--- Popping First ---")
    # linked_list = LinkedList(value=4)
    # linked_list.append(value=3)
    # linked_list.append(value=2)
    # linked_list.append(value=5)
    # linked_list.pop_first()
    # linked_list.pop_first()
    # linked_list.pop_first()
    # print("Head: ", linked_list.head.value)
    # print("Tail: ", linked_list.tail.value)
    # print("Length: ", linked_list.length)
    # linked_list.print_list()

    print("--- Getting ---")
    linked_list = LinkedList(value=1)
    linked_list.append(value=4)
    linked_list.append(value=3)
    linked_list.append(value=2)
    linked_list.append(value=5)
    linked_list.append(value=2)
    # linked_list.print_list()
    linked_list.partition_list(x=3)
    linked_list.print_list()

    # index = 3
    # print(f"Getting index {index} = {linked_list.get(index=index).value}")
    # linked_list.set_value(index=4, value=50)
    # linked_list.print_list()

    # print("--- Inserting ---")
    # linked_list.insert(index=2, value=32)
    # linked_list.print_list()
    
    # print("--- Removing ---")
    # removed_node = linked_list.remove(index=3)
    # linked_list.print_list()
    # print("Removed node = ", removed_node.value)

    # print("--- Reversing ---")
    # linked_list.print_list()
    # print("Reversed")
    # linked_list.reverse()
    # linked_list.print_list()







