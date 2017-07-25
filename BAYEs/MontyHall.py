#!/usr/bin/env python
#coding:utf-8
"""
  Author:  kaen.lee--<lichaolfm@163.com>
  Purpose: 
  Created: 2017/2/9
  Version: python3.5.2
"""

import unittest

class montyHall:
    #----------------------------------------------------------------------
    def __init__(self, choice, montyopen):
        """"""
        self.choice = choice
        self.montyopen = montyopen
        self.propbA = None
        self.propbB = None
        self.propbC = None
    
    #----------------------------------------------------------------------
    def __str__(self):
        """choice:the first choice
        montyopne: monty open the door"""
        if (self.choice == 'A')&(self.montyopen == 'B'):
            #situation1: car behind A
            priori1 = 1/3 
            likelihood1 = 1/2
            #situation2: car behind B
            priori2 = 1/3 
            likelihood2 = 0
            #situation3: car behind C
            priori3 = 1/3
            likelihood3 = 1
            stardardize_constance = priori1*likelihood1 + priori2*likelihood2 + priori3*likelihood3
            self.probA = priori1*likelihood1/stardardize_constance
            self.probB = priori2*likelihood2/stardardize_constance
            self.probC = priori3*likelihood3/stardardize_constance
        elif (self.choice == 'A')&(self.montyopen == 'C'):
            #situation1: car behind A
            priori1 = 1/3 
            likelihood1 = 1/2
            #situation2: car behind B
            priori2 = 1/3 
            likelihood2 = 1
            #situation3: car behind C
            priori3 = 1/3
            likelihood3 = 0
            stardardize_constance = priori1*likelihood1 + priori2*likelihood2 + priori3*likelihood3
            self.probA = priori1*likelihood1/stardardize_constance
            self.probB = priori2*likelihood2/stardardize_constance
            self.probC = priori3*likelihood3/stardardize_constance
        elif (self.choice == 'B')&(self.montyopen == 'C'):
            #situation1: car behind A
            priori1 = 1/3 
            likelihood1 = 1
            #situation2: car behind B
            priori2 = 1/3 
            likelihood2 = 1/2
            #situation3: car behind C
            priori3 = 1/3
            likelihood3 = 0
            stardardize_constance = priori1*likelihood1 + priori2*likelihood2 + priori3*likelihood3
            self.probA = priori1*likelihood1/stardardize_constance
            self.probB = priori2*likelihood2/stardardize_constance
            self.probC = priori3*likelihood3/stardardize_constance
        elif (self.choice == 'B')&(self.montyopen == 'A'):
            #situation1: car behind A
            priori1 = 1/3 
            likelihood1 = 0
            #situation2: car behind B
            priori2 = 1/3 
            likelihood2 = 1/2
            #situation3: car behind C
            priori3 = 1/3
            likelihood3 = 1
            stardardize_constance = priori1*likelihood1 + priori2*likelihood2 + priori3*likelihood3
            self.probA = priori1*likelihood1/stardardize_constance
            self.probB = priori2*likelihood2/stardardize_constance
            self.probC = priori3*likelihood3/stardardize_constance
        elif (self.choice == 'C')&(self.montyopen == 'A'):
            #situation1: car behind A
            priori1 = 1/3 
            likelihood1 = 0
            #situation2: car behind B
            priori2 = 1/3 
            likelihood2 = 1
            #situation3: car behind C
            priori3 = 1/3
            likelihood3 = 1/2
            stardardize_constance = priori1*likelihood1 + priori2*likelihood2 + priori3*likelihood3
            self.probA = priori1*likelihood1/stardardize_constance
            self.probB = priori2*likelihood2/stardardize_constance
            self.probC = priori3*likelihood3/stardardize_constance
        elif (self.choice == 'C')&(self.montyopen == 'B'):
            #situation1: car behind A
            priori1 = 1/3 
            likelihood1 = 1
            #situation2: car behind B
            priori2 = 1/3 
            likelihood2 = 0
            #situation3: car behind C
            priori3 = 1/3
            likelihood3 = 1/2
            stardardize_constance = priori1*likelihood1 + priori2*likelihood2 + priori3*likelihood3
            self.probA = priori1*likelihood1/stardardize_constance
            self.probB = priori2*likelihood2/stardardize_constance
            self.probC = priori3*likelihood3/stardardize_constance       
        return("""the probility of car behind the x
                  A: %f
                  B: %f
                  C: %f""" % (self.probA, self.probB, self.probC))

if __name__ == '__main__':
    test = montyHall('A', 'B')
    print(test)
    unittest.main()