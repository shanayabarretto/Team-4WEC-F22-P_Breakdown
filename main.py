import json
from datetime import datetime
from elevator import Elevator
import sys
import threading

def init():
    # starting function, reads basic json information
    file = open('test.json')
    data = json.load(file)
    floors = data['floors']
    elevators = []
    for _ in range(data['elevators']):
        elevators.append(Elevator())
    events = []
    for event in data['events']:
        list = []
        list.append(event['time'])
        list.append(event['start'])
        list.append(event['end'])
        events.append(list)

    return elevators, floors, events

def timediff(start):
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
    else:
        minutes += 16

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

def secondspast(start):
    current = datetime.now()
    curr = current.strftime("%H:%M:%S")
    start_t = start.strftime("%H:%M:%S")
    s_hours = int(start_t.split(':')[0])
    s_minutes = int(start_t.split(':')[1])
    s_seconds = int(start_t.split(':')[2])
    hours = int(curr.split(':')[0])
    minutes = int(curr.split(':')[1])
    seconds = int(curr.split(':')[2])
    before = (s_hours*3600) + (s_minutes*60) + s_seconds
    after  = (hours*3600) + (minutes*60) + seconds
    return after-before

def pick_elevator(elevators, start, end, people_list, y):
    # TODO: deal with it being at the top
    min_time = 10000
    curr_picked = None
    for x in elevators:
        curr_min_time = 10000
        # calculate time for elevator to reach
        # 1. who gets p1
        # make sure one gets picked at the end
        if not x.isFull():
            if not x.queue:
                curr_min_time = 0
            elif x.currFloor <= start and x.goingUp == True:
                curr_min_time
            elif x.currFloor >= start and x.goingUp == False:
                curr_min_time

            if curr_min_time < min_time:
                min_time = curr_min_time
                curr_picked = x
            
            # check floor
            # right direction- end of queue
            # calculate itme
    if curr_picked is not None:
        people_list.remove(y)
        # add it to the queue
    return


def move_elevator(elevator, done):
    while not done:
        while elevator.queue:
            print("hi")


def main():
    elevators, floors, events = init()
    start = datetime.now()
    end = timediff(start)
    threads = []
    done = False
    for elevator in elevators:
        e = threading.Thread(target=move_elevator, args=[elevator, done])
        e.start()
        threads.append(e)

    while (not_done(end)):
        # main code loop
        people_list = []
        for x in events:
            sec = secondspast(start)
            while (sec < x[0]):
                pass
            # event is coming in
            people_list.append(People())
            people_list[len(people_list) - 1].floorStart = x[1]
            people_list[len(people_list) - 1].floorEnd = x[2]
            for y in people_list:
                pick_elevator(elevators, y.floorStart, y.floorEnd, people_list, y)

    done = True
    for thread in threads:
        thread.join()
    return 0
  

if __name__ == "__main__":
    sys.exit(main())