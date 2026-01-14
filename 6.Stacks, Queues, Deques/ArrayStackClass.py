class ArrayStackclass:
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e)
        
    def top(self):
        if self.is_empty():
            raise len(self._data) == 0
        return self._data[-1]
    
    def pop(self):        
        if self.is_empty():
            raise len(self._data) == 0
        return self._data.pop()
        
    def is_balanced(self, expr):
        stacks = []
        compare = { ')': '(',
                    ']': '[', 
                    '}': '{'  }
        for character in expr:
            if character in "({[":
                stacks.append(character)
            elif character in ")}]":
                if not stacks or stacks[-1] != compare[character]:
                    return False
                stacks.pop()
        return not stacks