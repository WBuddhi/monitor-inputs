class MonitorKeyStrokes:

    def __init__(self):
        self.total = 0

    def update(self):
        self.total += 1

    def total_keystrokes(self):
        return(self.total)
