#!python3

from time import perf_counter
from numpy import random

def timeit(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end= perf_counter()
        print(f"{func.__name__} fucntion took {end-start:.4f} seconds")
        return result
    return wrapper

class list_node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LList():
    def __init__(self, array=None):
        head = list_node(array[0])
        self.head = head
        prev = self.head
        for i in range(1, len(array)):
            current = list_node(array[i])
            prev.next = current
            prev = current

    def insert(self, index, value):
        new_node = list_node(value)
        prev = None
        current = self.head
        for i in range(index):
            prev = current
            current = current.next
        prev.next = new_node
        new_node.next = current

    def __str__(self):
        result = ""
        current = self.head
        while current.next:
            result += str(current.value) + "->"
            current = current.next
        result += str(current.value)
        return result

@timeit
def using_list(array, index, value):
    array.insert(index, value)

@timeit
def using_linked(linked_list, index, value):
    # print(array.head.value)
    linked_list.insert(index, value)
    # print(array)

def main():
    array1 = list(random.randint(0, 100, 1_000_000))
    array2 = array1.copy()
    array2 = LList(array2)
    # print(type(array2))
    index = len(array1)//2
    value = 5
    using_list(array1, index, value)
    using_linked(array2, index, value)

if __name__ == "__main__":
    main()
