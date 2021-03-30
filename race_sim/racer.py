import random


class Racer:

    def __init__(self, name, stride_length):
        self.name = name
        self.position = 0
        self.stride_length = stride_length
        self.miss_count = 0
        self.half_count = 0
        self.triple_count = 0

    def move(self, max_position) -> int:
        sim = random.random()
        if sim >= .1:
            increment = sim/.75 * self.stride_length
            if sim < .15:
                increment = increment/2
                self.half_count += 1
            elif sim > .99:
                increment = increment * 3
                self.triple_count += 1

            self.position = min(self.position + increment, max_position)
        else:
            self.miss_count += 1
        return self.position

    def get_stats(self):
        return f"Stuck: {self.miss_count} Stumbled: {self.half_count} Galloped: {self.triple_count}"

    def get_position(self) -> int:
        return self.position
