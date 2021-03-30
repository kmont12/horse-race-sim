import threading
import random
import time
from threading import Thread

# from .racer import Racer
from .combo_racer import ComboRacer


class Race(Thread):

    def __init__(self, race_length, num_of_racers):
        super().__init__()
        self.race_length = race_length
        self.num_of_racers = num_of_racers
        self.racers = [ComboRacer(f"{i}", 5) for i in range(num_of_racers)]
        self.leader = None
        self.leader_position = 0
        self.is_finished = False
        self.lock = threading.Lock()
        self.final_placing = []

    def is_running(self):
        with self.lock:
            if not self.is_finished:
                return True
            return False

    def print_results(self):
        with self.lock:
            if not self.is_finished:
                if self.leader is None and len(self.final_placing) == 0:
                    print(f'No definitive leader at this time. The furthest racers are {self.leader_position} meters along')
                elif len(self.final_placing) > 0:
                    print("Some Racers already finished")
                    for index, racer in enumerate(self.final_placing):
                        print(f'Place {index + 1}: {racer.name}')
                else:
                    print(f"Racer {self.leader.name} is in the lead at {self.leader_position} meters")
                for racer in self.racers:
                    print(f"{'*' * int(racer.get_position())}{racer.name}{'-' * (self.race_length - int(racer.get_position()) - len(racer.name))}")
            else:
                print('Race Complete: Final Standings are')
                for index, racer in enumerate(self.final_placing):
                    print(f'Place {index + 1}: {racer.name}')
                    print(racer.get_stats())

    def run(self):
        while not self.is_finished:
            with self.lock:
                racers_copy = self.racers.copy()
                while racers_copy:
                    racer = random.choice(racers_copy)
                    if racer.get_position() < self.race_length:
                        position = racer.move(self.race_length)
                        if position >= self.race_length:
                            self.final_placing.append(racer)
                            if len(self.final_placing) == len(self.racers):
                                self.is_finished = True
                        if position == self.leader_position and self.leader is not None and self.leader != racer:
                            self.leader = None
                        if position > self.leader_position:
                            self.leader = racer
                            self.leader_position = position
                    racers_copy.remove(racer)
                    # else:
                    #     print(f'racer {racer_id} not moving')
            time.sleep(1)
