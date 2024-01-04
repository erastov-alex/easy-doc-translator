class Counter():
    def __init__(self, count=0) -> None:
        self.count = count
    
    def add(self, n=1):
        self.count += n

    def reset(self):
        self.count = 0

    def set_value(self, value):
        self.count = value
        