class StackProcessor:
    def __init__(self):
        self.stack = []

    def process(self, n):
        for i in range(n):  # Push ค่าเข้า Stack
            self.stack.append(i)
        # Pop ค่าออกจาก Stack
        print(self.stack)

sp = StackProcessor()
sp.process(5)