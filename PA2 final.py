# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 21:24:39 2024

@author: LAKwon
"""
import random
from tabulate import tabulate

#constant variables
BASIC_CUSTOMER_TIME = 45
SECONDS_PER_ITEM = 4
NEW_CUSTOMER_TIME = 30
PRINT_INFO_TIME = 50

#queue methods
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def get(self, position):
        return self.items[position]
    
#customer methods
class Customer:
    def __init__(self, max_items = 20):
        self.itemCount = random.randrange(6, max_items)
    
    def getItemCount(self):
        return self.itemCount

#Register methods
class Register:
    def __init__(self):
        #totals used for end of code
        self.totalTimeCheck = 0
        self.totalTimeWait = 0
        self.totalItemServed = 0
        self.currentCustomer = None
        self.timeRemaining = 0
        self.totalCustomer = 0
        self.totalIdleTime = 0
        
    def tick(self):
        if not(self.idle()):
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentCustomer = None
                return True
        else:
            self.totalIdleTime += 1
    
    def idle(self):
        return (self.currentCustomer == None)        
        
    def startNext(self, newCustomer) :
        self.currentCustomer = newCustomer
        self.timeRemaining = BASIC_CUSTOMER_TIME + SECONDS_PER_ITEM * self.currentCustomer
        self.totalItemServed += self.currentCustomer
        self.totalTimeCheck += self.timeRemaining
        self.totalCustomer += 1
        
    #if nobody is in register line
    def idling(self):
        self.totalTimeWait += 1
        
    def getPresentItems(self):
        return self.currentCustomer
    
    def getTotalItems(self):
        return self.totalItemServed

    def getAvgTimeWait(self):
        if self.totalCustomer == 0:
            return 0
        return (self.totalTimeWait * self.totalCustomer) / self.totalCustomer
        
    def getTotalCustomers(self):
        return self.totalCustomer

    def getTotalIdleTime(self):
        return self.totalIdleTime / 60
        
def simulation(simlength):
    line1 = Register()
    line2 = Register()
    line3 = Register()
    line4 = Register()
    express = Register()
    line1Queue = Queue()
    line2Queue = Queue()
    line3Queue = Queue()
    line4Queue = Queue()
    expressQueue = Queue()
    waitList = []
    randList = []
    
    for currentSecond in range(simlength+1):
        if currentSecond % NEW_CUSTOMER_TIME == 0 and currentSecond != 0:
            new = Customer()
            s1 = line1Queue.size()
            s2 = line2Queue.size()
            s3 = line3Queue.size()
            s4 = line4Queue.size()
            se = expressQueue.size()
            waitList.append(s1)
            waitList.append(s2)
            waitList.append(s3)
            waitList.append(s4)
            waitList.append(se)
            s = min(waitList)
            
            if express.idle() and new.getItemCount() < 10:
                express.startNext(new.getItemCount())
                expressQueue.enqueue(new.getItemCount())
            if s1 == s:
                randList.append(s1)
            if s2 == s:
                randList.append(s2)
            if s3 == s:
                randList.append(s3)
            if s4 == s:
                randList.append(s4)
            if se == s:
                randList.append(se)
                
            pick = random.choice(randList)
            
            if express.idle() and new.getItemCount() < 10:
                express.startNext(new.getItemCount())
                expressQueue.enqueue(new.getItemCount())
            elif pick == se and new.getItemCount() < 10:
                express.startNext(new.getItemCount())
                expressQueue.enqueue(new.getItemCount())
            elif pick == s1:
                line1.startNext(new.getItemCount())
                line1Queue.enqueue(new.getItemCount())
            elif pick == s2:
                line2.startNext(new.getItemCount())
                line2Queue.enqueue(new.getItemCount())
            elif pick == s3:
                line3.startNext(new.getItemCount())
                line3Queue.enqueue(new.getItemCount())
            elif pick == s4:
                line4.startNext(new.getItemCount())
                line4Queue.enqueue(new.getItemCount())
            waitList.clear()
            randList.clear()
        if line1Queue.size() > 1:
            line1.idling()
        if line2Queue.size() > 1:
            line2.idling()
        if line3Queue.size() > 1:
            line3.idling()
        if line4Queue.size() > 1:
            line4.idling()
        if expressQueue.size() > 1:
            express.idling()
        l1 = line1.tick()
        l2 = line2.tick()
        l3 = line3.tick()
        l4 = line4.tick()
        e = express.tick()
        if l1 == True:
            line1Queue.dequeue()
        if l2 == True:
            line2Queue.dequeue()
        if l3 == True:
            line3Queue.dequeue()
        if l4 == True:
            line4Queue.dequeue()
        if e == True:
            expressQueue.dequeue()
        if currentSecond % PRINT_INFO_TIME == 0:
            lene = expressQueue.size() - 1
            len1 = line1Queue.size() - 1
            len2 = line2Queue.size() - 1
            len3 = line3Queue.size() - 1
            len4 = line4Queue.size() - 1
            print("time=%i" % currentSecond , end="\n")
            print("reg#    customers")
            print("0", end = " ")
            if expressQueue.size() == 0:
                print("--", end = "")
            else:
                while lene >= 0:
                    print(expressQueue.get(lene), end = " | ")
                    lene -= 1
            print()
            print("1", end = " ")
            if line1Queue.size() == 0:
                print("--", end = "")
            else:
                while len1 >= 0:
                    print(line1Queue.get(len1), end = " | ")
                    len1 -= 1
            print()
            print("2", end = " ")
            if line2Queue.size() == 0:
                print("--", end = "")
            else:
                while len2 >= 0:
                    print(line2Queue.get(len2), end = " | ")
                    len2 -= 1
            print()
            print("3", end = " ")
            if line3Queue.size() == 0:
                print("--", end = "")
            else:
                while len3 >= 0:
                    print(line3Queue.get(len3), end = " | ")
                    len3 -= 1
            print()
            print("4", end = " ")
            if line4Queue.size() == 0:
                print("--", end = "")
            else:
                while len4 >= 0:
                    print(line4Queue.get(len4), end = " | ")
                    len4 -= 1
            print()
    header = ["Register", "Total Items", "Total Customers", "Total Idle Time (min)", 'Average Wait Time (sec)']
    data = [["express", express.getTotalItems(), express.getTotalCustomers(), express.getTotalIdleTime(), express.getAvgTimeWait()],
                   ["1", line1.getTotalItems(), line1.getTotalCustomers(), line1.getTotalIdleTime(), line2.getAvgTimeWait()],
                   ["2", line2.getTotalItems(), line2.getTotalCustomers(), line2.getTotalIdleTime(), line2.getAvgTimeWait()],
                   ["3", line3.getTotalItems(), line3.getTotalCustomers(), line3.getTotalIdleTime(), line3.getAvgTimeWait()],
                   ["4", line4.getTotalItems(), line4.getTotalCustomers(), line4.getTotalIdleTime(),line4.getAvgTimeWait()],
                    ]
    table = tabulate(data, header, tablefmt="grid")
    print(table)
    
def main():
    simtime = 7200
    simruns = 1
    for i in range(simruns):
        simulation(simtime)
    
main()