#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 21:08:27 2021

@author: zachary
"""


import random

# def validate_input(value_type, prompt, error_message, invalid_type_message, lower = None, upper = None):
#     val = input(prompt)
#     if type(val) is value_type:
#         if lower and upper and lower <= val and val <= upper:
#             return value_type(val)
#         elif lower and upper:
#             print(error_message)
#         else:
#             return value_type(val)
#     else:
#         print(invalid_type_message)

def getpopdens():
    invalid = True
    while invalid == True:
        popdens_ = input('What is your desired population density (in [0,1])? ')
        try:
            popdens = float(popdens_)
            if 0 <= popdens and popdens <= 1:
                invalid = False
            else:
                print('Population density must be in [0,1]')
        except:
            print('Population density must be value in [0,1]')
    return popdens


def getsize():
    invalid = True
    while invalid == True:
        size_ = input('How large would you like to make your grid? ')
        try:
            size = int(size_)
            invalid = False
        except ValueError:
            print('Grid size much be positive integer' )
            invalid = True
    return size

def getdischance():
    invalid = True
    while invalid == True:
        dischance_ = input('What is your desired disease chance (in [0,1])? ')
        try:
            dischance = float(dischance_)
            if 0 <= dischance and dischance <= 1:
                invalid = False
            else:
                print('Disease chance must be in [0,1]')
        except:
            print('Disease chance must be value in [0,1]')
    return dischance

def getbirthchance():
    invalid = True
    while invalid == True:
        birthchance_ = input('What is your desired birth chance (in [0,1])? ')
        try:
            birthchance = float(birthchance_)
            if 0 <= birthchance and birthchance <= 1:
                invalid = False
            else:
                print('Birth chance must be in [0,1]')
        except:
            print('Birth chance must be value in [0,1]')
    return birthchance

def getspreadchance():
    invalid = True
    while invalid == True:
        spreadchance_ = input('What is your desired spread chance (in [0,1])? ')
        try:
            spreadchance = float(spreadchance_)
            if 0 <= spreadchance and spreadchance <= 1:
                invalid = False
            else:
                print('Spread chance must be in [0,1]')
        except:
            print('Spread chance must be value in [0,1]')
    return spreadchance

def getdisdur():
    invalid = True
    while invalid == True:
        disdur_ = input('What is your desired disease duration (integer in [1,10])? ')
        try:
            disdur = int(disdur_)
            if 1 <= disdur and disdur <= 10:
                invalid = False
            else:
                print('Disease duration must be in [1,10]')
        except:
            print('Disease duration must be integer in [1,10]')
    return disdur

def getmortrate():
    invalid = True
    while invalid == True:
        mortrate_ = input('What is your desired mortality rate (in [0,1])? ')
        try:
            mortrate = float(mortrate_)
            if 0 <= mortrate and mortrate <= 1:
                invalid = False
            else:
                print('Mortality rate must be in [0,1]')
        except:
            print('Mortality rate must be value in [0,1]')
    return mortrate

def getdays():
    invalid = True
    while invalid == True:
        days_ = input('How many days would you like to simulate (positive integer)')
        try:
            days = int(days_)
            invalid = False
        except:
            print('Days must be positive integer')
    return days

def getneighbors(tuple):
    neighbors = []
    for i in range(-1,2):
        for j in range(-1,2):
            neighbors.append((tuple[0] + i,tuple[1] + j))
    del neighbors[neighbors.index(tuple)]
    return neighbors

def update(states,birthchance,spreadchance,disdur,mortrate,size):
    for cell in states:
        if states[cell] == 'X':
            continue
        _neighbors_ = getneighbors(cell)
        neighbors = []
        for n in _neighbors_:
            if n[0] >= 0 and n[0] < size and n[1] >= 0 and n[1] < size:
                neighbors.append(n)
        if states[cell] == '.':
            for n in neighbors:
                if states[n] == 0:
                    occ = random.random()
                    if occ < birthchance:
                        states[cell] = 0
                        break
        elif states[cell] == 0:
            for n in neighbors:
                if type(states[n]) is int and states[n] >= 1:
                    inf = random.random()
                    if inf < spreadchance:
                        states[cell] += 1
                        break
        elif states[cell] >= 1 and states[cell] < disdur:
            states[cell] += 1
        else:
            kill = random.random()
            if kill < mortrate:
                states[cell] = 'X'
            else:
                states[cell] = 0
    return states

def make_grid(states,size):
    for j in range(size):
        rowj = ''
        for i in range(size):
            rowj += str(states[(i,j)]) + ' '
        print(rowj)
    print('')

def zombie_sim(size,popdens,dischance,birthchance,spreadchance,disdur,mortrate,days):
    states = {}
    for i in range(size):
        for j in range(size):
            occ = random.random()
            if occ < popdens:
                states[i,j] = 0
            else:
                states[i,j] = '.'
    for k in states:
        if states[k] == 0:
            dis = random.random()
            if dis < popdens:
                states[k] += 1
    for i in range(days):
        make_grid(states,size)
        values = set(states.values())
        nums = {i for i in range(disdur + 1)}
        nums2 = nums.difference({0})
        if values.difference(nums) == values:
            print('No more living specimens')
            break
        elif values.difference(nums2) == values:
            print('Virus eradicated!')
            break
        update(states,birthchance,spreadchance,disdur,mortrate,size)

def sim():
    popdens = getpopdens()
    size = getsize()
    dischance = getdischance()
    birthchance = getbirthchance()
    spreadchance = getspreadchance()
    disdur = getdisdur()
    mortrate = getmortrate()
    days = getdays()
    zombie_sim(size,popdens,dischance,birthchance,spreadchance,disdur,mortrate,days)


if __name__ == '__main__':
    zombie_sim(20, 0.15, 0.1, 0.1, 0.1, 3, 0.5, 500)