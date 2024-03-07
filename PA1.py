# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 13:34:57 2024

@author: LCHarris
"""

import random 
import time
from tabulate import tabulate

def one_dimension(moves):
    count = 0
    x = 0
    for i in range(moves):
        direction = random.choice(["Left","Right"])
        if direction == "Left":
            x -= 1
        elif direction == "Right":
            x += 1
        if x == 0:
            count += 1
            break
    return count


def two_dimensions(moves):
    count = 0
    x = 0
    y = 0
    for i in range(moves):
        direction = random.choice(["Left","Right","Up","Down"])
        if direction == "Left":
            x -= 1
        elif direction == "Right":
            x += 1
        elif direction == "Up":
            y += 1
        elif direction == "Down":
            y -= 1
        if x == 0 and y == 0:
            count += 1
            break
    return count


def three_dimensions(moves):
    count = 0
    x = 0
    y = 0
    z = 0
    for i in range(moves):
        direction = random.choice(["Left","Right","Up","Down","Forward","Backward"])
        if direction == "Left":
            x -= 1
        elif direction == "Right":
            x += 1
        elif direction == "Up":
            y += 1
        elif direction == "Down":
            y -= 1
        elif direction == "Forward":
            z += 1
        elif direction == "Backward":
            z -= 1
        if x == 0 and y == 0 and z == 0:
            count += 1
            break
    return count



def main():
    
    more_vals = [20,200,2000,20000,200000,2000000]
    results1 = []
    results2 = []
    results3 = []
    timeresults3 = []
    
    for moves in more_vals:
        final_count1 = 0
        for i in range(100):
            final_count1 += one_dimension(moves)
        results1.append(final_count1)

    for moves in more_vals:
        final_count2 = 0
        for i in range(100):
            final_count2 += two_dimensions(moves)
        results2.append(final_count2)
    
    start_time = time.time()
    for moves in more_vals:
        final_count3 = 0
        for i in range(100):
            final_count3 += three_dimensions(moves)
        results3.append(final_count3)
        end_time = time.time()
        elapsed_time = end_time - start_time
        timeresults3.append(elapsed_time)
    
    data1 = [
        ["1D",results1[0],results1[1],results1[2],results1[3],results1[4],results1[5]],
        ["2D",results2[0],results2[1],results2[2],results2[3],results2[4],results2[5]],
        ["3D",results3[0],results3[1],results3[2],results3[3],results3[4],results3[5]]]
    
    print("Percentages of time particle returned to origin:")
    header = ["Number of Steps:", "20", "200", "2000", "20000", "200000", "2000000"]
    table1 = tabulate(data1, header, tablefmt="grid")
    print(table1)

    
    data2 = [["3D",timeresults3[0],timeresults3[1],timeresults3[2],timeresults3[3],timeresults3[4],timeresults3[5]]]
    
    print("Run time (seconds):")
    table2 = tabulate(data2, header, tablefmt="grid")
    print(table2)

main()



