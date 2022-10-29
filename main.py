import json
from datetime import datetime
from elevator import Elevator
import sys

def init():
    # starting function, reads basic json information
    file = open('test.json')
    data = json.load(file)
    floors = data['floors']
    elevators = []
    for _ in range(data['elevators']):
        elevators.append(Elevator())
    return elevators, floors, data

def timediff():
    start = datetime.now()
    start_t = start.strftime("%H:%M:%S")
    hours = int(start_t.split(':')[0])
    minutes = int(start_t.split(':')[1])
    seconds = int(start_t.split(':')[2])
    if (seconds + 40) >= 60:
        minutes += 1
        seconds = 40 - (60 - seconds)
    else:
        seconds += 40

    if (minutes + 16) >= 60:
        hours += 1
        minutes = 16 - (60 - minutes)

    return [hours, minutes, seconds]

def not_done(end):
    current = datetime.now()
    curr = current.strftime("%H:%M:%S")
    hours = int(curr.split(':')[0])
    minutes = int(curr.split(':')[1])
    seconds = int(curr.split(':')[2])
    if (end[0] >= hours and end[1] >= minutes and end[2] >= seconds):
        return False
    return True


def main():
    elevators, floors, data = init()
    end = timediff()
    while (not_done(end)):
        # main code loop
        print(data['events'][0]['time'])
    return 0
  

if __name__ == "__main__":
    sys.exit(main())