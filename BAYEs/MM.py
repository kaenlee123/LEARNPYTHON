#!/usr/bin/env python
#coding:utf-8
"""
  Author:  kaen.lee--<lichaolfm@163.com>
  Purpose: M&M豆问题
  Created: 2017/2/9
  Version: python3.5.2
"""

import unittest
import numpy as np
import datetime as dt
start = dt.datetime.now()
prob0 = {'brown':0.3, 'yellow':0.2, 'red':0.2, 'green':0.1, 'orange':0.1, 'tan':0.1}
prob1 = {'blue':0.24, 'green':0.2, 'orange':0.16, 'yellow':0.14, 'red':0.13, 'brown':0.13}

def solution(tag, anthor, prob0, prob1):
    #tow bins from different bags
    #work out the probility of the color0 from bag0
    #situatation1: from bag0(prob0)
    priori1 = 0.5 # choice bag0
    likelihood_tag0_anthor1 = prob0[tag]*prob1[anthor]
    #situation2: from bag2
    priori2 = 0.5
    likelihood_tag1_anthor0 = prob1[tag]*prob0[anthor]
    Standardize_constants = priori1*likelihood_tag0_anthor1 + priori2*likelihood_tag1_anthor0
    return(priori1*likelihood_tag0_anthor1 / Standardize_constants)
    

if __name__ == '__main__':
    print(("the probility of the yellow from prob0:", solution('yellow', 'green', prob0, prob1)))
    end = dt.datetime.now()
    print(('costing time for result:', end-start))
    unittest.main()