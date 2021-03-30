from .race import Race
import time

if __name__ == "__main__":
    race = Race(100, 16)
    race.start()
    time.sleep(1)
    while race.is_running():
        race.print_results()
        time.sleep(1)
    race.print_results()
