from math import ceil

def solution(fees, records):
    answer = []
    parking = {}
    for i in range(len(records)):
        time, num, record = records[i].split()
        hour, minute = map(int, time.split(':'))
        if num in parking:
            parking[num].append(hour*60 + minute)
        else:
            parking[num] = [hour*60 + minute]
    cars = sorted(parking.items())
    for car in cars:
        cost = fees[1]
        diff = 0
        while car[1]:
            if len(car[1]) >= 2:
                car_in = car[1].pop(0)
                car_out = car[1].pop(0)
                diff += car_out - car_in
            else:
                diff += (23 * 60 + 59) - car[1].pop()
        if diff > fees[0]:
            cost += ceil((diff - fees[0]) / fees[2]) * fees[3]
        answer.append(cost)    
    return answer