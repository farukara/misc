#!python3
# coding: utf-8
# Compares deque and list performance to find the longest palindrome

from time import perf_counter
from typing import List

def timed(function):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        value = function(*args, **kwargs)
        finish = perf_counter()
        print(f"\n\"{function.__name__}\" function took {finish - start:.6f} seconds")
        return value
    return wrapper

class Deq_with_list():
    "deq class using list"
    def __init__(self, text):
        self.content = list(text.lower())
    def size(self):
        return(len(self.content))
    def remove_front(self):
        return self.content.pop()
    def remove_rear(self):
        return self.content.pop(0)

class deq_node():
    "initilizes linked-list-like type node object to use in deque class"
    def __init__(self, item):
        self.value = item
        self.prev = None
        self. next = None
        
        

class Deq_with_object():
    "deq class using object"
    def __init__(self, text):
        self.content = text.lower()
        self.rear = deq_node(self.content[0])
        self.front = deq_node(self.content[-1])
        current_parent = self.rear
        for letter in self.content[1:-1]:
            current_node = deq_node(letter)
            current_node.prev = current_parent
            current_parent.next = current_node
            current_parent = current_node
        current_node.next = self.front
        self.front.prev = current_node
    def size(self):
        return len(self.content)
    def remove_front(self):
        current_node = self.front
        self.front = self.front.prev
        return current_node.value
    def remove_rear(self):
        current_node = self.rear
        self.rear = self.rear.next
        return current_node.value

@timed
def using_list (text):
    "accepts text as a string and returns bool"
    text = text.lower()
    for i in range(len(text)//2):
        if text[i] != text[-(i+1)]:
            return False
        return True
@timed
def using_deque(text):
    "accepts text as a deque object and applies deque methods on list to return a bool"
    for i in range(text.size()//2):
        if text.remove_front() != text.remove_rear():
            return False
    return True

if __name__ == "__main__":
    with open("longest_palindrome_text.txt", "r") as file:
        text = file.read()
    new_text = ""
    for letter in text:
        if letter.isalnum():
            new_text += letter
    deqlist = Deq_with_list(new_text)
    deqobject = Deq_with_object(new_text)
    print("using list: ", using_list(new_text))
    print("using deque based on list" , using_deque(deqlist))
    print("using deque based on custom object" , using_deque(deqobject))
