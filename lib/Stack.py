class Stack:
    def __init__(self, items=None, limit=100):
        self.items = items if items is not None else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    # def search(self, target):
    #     return target in self.items
    def search(self, target):
        if target not in self.items:
            return -1  # Target element is not in the stack, return -1 or any appropriate value
        else:
        # Find the index of the target element starting from the top of the stack (last element)
            index = len(self.items) - self.items[::-1].index(target) - 1
            return len(self.items) - 1 - index
        
        #If the target element is in the stack, we use list slicing to find the index of the target element starting from the top of the stack (the last element). 
        # The self.items[::-1].index(target) part returns the index of the target element when we reverse the order of items in the stack. 
        # We then subtract this index from the length of the stack minus 1 to calculate how far the target element is from the last element.

