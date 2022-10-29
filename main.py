import json
from datetime import datetime
import sys

def init():
    # starting function, reads basic json information
    file = open('test.json')
    data = json.load(file)
    floors = data['floors']
    elevators = []
    for i in range(data['elevators']):
        elevators.append(Elevator(i))

def timediff():
    start = datetime.now()
    start_t = start.strftime("%H:%M:%S")
    hours = start_t.split(':')[0]
    minutes = start_t.split(':')[1]
    seconds = start_t.split(':')[2]
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
    current = datetime.now
    curr = current.strftime("%H:%M:%S")
    hours = curr.split(':')[0]
    minutes = curr.split(':')[1]
    seconds = curr.split(':')[2]
    if (end[0] >= hours and end[1] >= minutes and end[2] >= seconds):
        return False
    return True



def main():
    init()
    end = timediff()
    while (not_done(end)):
        # main code loop
    return 0
  

if __name__ == "__main__":
    sys.exit(main())