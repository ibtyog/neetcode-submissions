class MinStack:
    def __init__(self):
        self.stack = []
        self.minimal = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimal or val <= self.minimal[-1]:
            self.minimal.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minimal[-1]:
            self.minimal.pop()
        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimal[-1]
