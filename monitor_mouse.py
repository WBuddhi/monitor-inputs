import numpy as np

class MonitorMouse:

    def __init__(self):

        self.x = 0.0
        self.y = 0.0
        self.x_sum = self.y_sum = 0
        self.start_flag = False

    def total_distance(self):
        """Calculates the euclidean."""

        return np.sqrt(self.y_sum**2 + self.x_sum**2)

    def update(self, x, y):
        """Accumulates change in x and y direction."""

        if not self.start_flag:
            self.x_old = x
            self.y_old = y
        self.x_old = self.x
        self.y_old = self.y
        self.x = x
        self.y = y
        self.x_sum += abs(self.x - self.x_old)
        self.y_sum += abs(self.y - self.y_old)
        self.start_flag = True

