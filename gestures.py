# unable to understand collections and deque. Is it an inbuild module or downloaded module. What does it do?
# what is deque?
from collections import deque
import time

class SwipeDetector:
    def __init__(self):
        # why are we creating all these properties and what do they do?
        # unable to understand the high level overview
        self.positions = deque(maxlen=15)
        self.swipe_threshold = 0.18 # could not understand the concept of swipe_threshold
        self.cooldown = 0.8 # could not understand the concept of cooldown
        self.last_swipte_time = 0

    def detect(self, x):
        # what is time.monotonic()?
        current_time = time.monotonic()

        # stored normalized X coooordinate and timestamp
        # what is x?
        self.positions.append((current_time, x))

        # why less than 5 only
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

        # cooldown prevents repeated detection
        # could not understand the logic
        if current_time - self.last_swipte_time < self.cooldown:
            return None

        # could not understand this function at all
        if movement < -self.swipe_threshold:
            self.last_swipte_time = current_time
            self.positions.clear()

            return "SWIPE LEFT"

        # could not understand this function at all
        elif movement > self.swipe_threshold:
            self.last_swipte_time = current_time
            self.positions.clear()

            return "SWIPE RIGHT"

        print("Movement: ", round(movement, 3))

        return None
