import json
import time
from datetime import datetime
from elevator import Elevator
from people import People
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

def pick_elevator(elevators, start, people_down, people_up, people_list, y):
    min_time = 10000
    curr_picked = None
    for x in elevators:
        curr_min_time = 10000
        if not x.isFull():
            if not x.queue:
                curr_min_time = 0
            elif x.currFloor <= start and x.goingUp == True and y in people_up:
                curr_min_time = x.timeToGetToFloor(start)
            elif x.currFloor >= start and x.goingUp == False and y in people_down:
                curr_min_time = x.timeToGetToFloor(start)

            if curr_min_time < min_time:
                min_time = curr_min_time
                curr_picked = x
            
    if curr_picked is not None:
        people_list.remove(y)
        if y in people_up:
            people_up.remove(y)
        else:
            people_down.remove(y)
        x.queue.append(y)
    return


def move_elevator(elevator, done):
    while not done:
        while elevator.queue:
            picked = None
            min_dist = 100000
            for person in elevator.queue:
                if person.pickedUp == False:
                    if abs(person.startFloor-elevator.currFloor) < min_dist:
                        picked = person.startFloor
                else:
                    if abs(person.endFloor-elevator.currFloor) < min_dist:
                        picked = person.endFloor
            # we have picked our destination
            transition = elevator.timeToGetToFloor(picked)
            if elevator.goingUp:
                print("Elevator moving up")
            else:
                print("Elevator moving down")
            time.sleep(transition)
            elevator.changeFloor(picked)
            time.sleep(10)
            for person in elevator.queue:
                if person.pickedUp == False and elevator.currFloor == person.startFloor:
                    person.pickedUp = True
                    print("Someone just entered the elevator")
                    elevator.numOfPeople += 1
                if person.delivered == False and elevator.currFloor == person.endFloor:
                    person.delivered = True
                    print("Someone just exited the elevator")
                    elevator.numOfPeople -= 1
                if person.delivered == True:
                    elevator.queue.remove(person)
                    total = person.Total()
                    print("I travelled from floor " + person.startFloor + "to " + person.endFloor + "in " + total + " seconds.")


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
        people_up = []
        people_down = []
        for x in events:
            sec = secondspast(start)
            while (sec < x[0]):
                pass
            # event is coming in
            startTime = datetime.now
            person = People(x[1], x[2], startTime)
            people_list.append(person)
            # grouping into people who want to go up and people who want to go down
            if people_list[len(people_list) - 1].direction == 1:
                people_up[len(people_list) - 1].append(person)
            else:
                people_down.append(person)
            
            for y in people_list:
                pick_elevator(elevators, y.floorStart, people_down, people_up, people_list, y)
    # do a while for everyone who is not picked up
    while people_list:
        pick_elevator(elevators, y.floorStart, people_down, people_up, people_list, y)
    done = True
    for thread in threads:
        thread.join()
    return 0
  

main()