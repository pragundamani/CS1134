from ArrayStack import ArrayStack


class MaxStack:
    def __init__(self):
        self.data = ArrayStack()

    def is_empty(self):
        return len(self.data) == 0

    def __len__(self):
        return len(self.data)

    def push(self, val):
        if self.is_empty():
            self.data.push((val, val))
        else:
            curr_max = max(self.data.top()[1], val)
            self.data.push((val, curr_max))

    def top(self):
        if self.is_empty():
            raise Exception("MaxStack is empty")
        return self.data.top()[0]

    def pop(self):
        if self.is_empty():
            raise Exception("MaxStack is empty")
        return self.data.pop()[0]

    def max(self):
        if self.is_empty():
            raise Exception("MaxStack is empty")
        return self.data.top()[1]
