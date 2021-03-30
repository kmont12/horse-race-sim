from .racer import Racer
import random


class ComboRacer(Racer):

    def __init__(self, name, stride_length):
        super().__init__(name, stride_length)
        self.miss_chance = .1
        self.half_chance = .05
        self.non_crit = .99

    def move(self, max_position):
        sim = random.random()
        if sim >= self.miss_chance:
            increment = sim/.75 * self.stride_length
            if sim < self.miss_chance + self.half_chance:
                self.half_chance = min(self.half_chance*1.1, .2)
                self.non_crit *= .99
                increment = increment/2
                self.half_count += 1
            elif sim > self.non_crit:
                self.non_crit = max(self.non_crit*.9, .65)
                self.miss_chance = min(self.miss_chance*1.4, .4)
                increment = increment * 3
                self.triple_count += 1
            else:
                self.half_chance = max(.05, self.half_chance * .98)
                self.miss_chance = max(.1, self.miss_chance * .98)
            self.position = min(self.position + increment, max_position)
        else:
            self.miss_chance = min(self.miss_chance*1.1, .20)
            self.non_crit *= .99
            self.miss_count += 1
        return self.position
