# collections is a inbuilt module in python
# deque is a special data structure - Double Ended Queue. It is a data structure that allows you to add and remove elements from both ends.
from collections import deque
import time

class SwipeDetector:
    def __init__(self):
        self.positions = deque(maxlen=15) # It is recoding current time and hand movement
        self.swipe_threshold = 0.18 # could not understand the concept of swipe_threshold
        self.cooldown = 0.8 # waiting period between each swipe detection
        self.last_swipte_time = 0 # this remembers when the last swipe detected

    def detect(self, x):
        # what is time.monotonic()?
        current_time = time.monotonic() # monotonic gives us a clock time that continuously increases

        self.positions.append((current_time, x))

        # atlest 5 history is required to delect a swipe
        if len(self.positions) < 5:
            return None

        # why only 0 postion. Why not other position?
        old_time, old_x = self.positions[0]
        # why only -1 postion. Why not other position?
        new_time, new_x = self.positions[-1]

        elapsed = new_time - old_time

        # what for sufficient movement history
        if elapsed < 0.25:
            return None

        # avoid detecting very slow movements
        if elapsed > 0.6:
            return None

        movement = new_x - old_x

        if current_time - self.last_swipte_time < self.cooldown:
            return None

        if movement < -self.swipe_threshold:
            self.last_swipte_time = current_time
            self.positions.clear()

            return "SWIPE LEFT"

        elif movement > self.swipe_threshold:
            self.last_swipte_time = current_time
            self.positions.clear()

            return "SWIPE RIGHT"

        print("Movement: ", round(movement, 3))

        return None
