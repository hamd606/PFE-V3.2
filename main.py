import random
import Bank
import Household
import Firm
import time
from logger import log

print random.uniform(1,2)


mu = int(input("workerks to firms ratio: "))
c = int(input("marginal propensity to consume: "))
betaDi = int(input("elasticity: "))
gammaPi = int(input("price max variation: "))
gammaWi = int(input("wages max variation: "))
phi = int(input("information asymmetry degree: "))
nF = int(input("firms number: "))

print "-------------------------------------------------"
print "parameter\t\t|\t\tvalue"
print "-------------------------------------------------"
print "mu\t\t\t|\t\t" , mu
print "c \t\t\t|\t\t" , c
print "betaDi \t\t\t|\t\t" , betaDi
print "gammaPi \t\t|\t\t" , gammaPi
print "gammaWi \t\t|\t\t" , gammaWi
print "phi \t\t\t|\t\t" , phi 
print "nF \t\t\t|\t\t" , nF

workersList = []
firmsList = []
pBar = 1
for i in range(nF):
    firmsList.append(Firm.Firm(None, 0, 1, random.uniform(10,5), 0, 0, random.uniform(60,120)))
    #random.shuffle(firmsList)

for i in range(nF*mu):
    workersList.append(Household.Household(i, random.uniform(5,7), 1, False))
    random.shuffle(workersList)

for i in firmsList:
    print "firm %i created: tethaF0 = %i" %(firmsList.index(i), i.liquidity)

for i in firmsList:
    print "firm %i created: tethaF0 = %i" %(firmsList.index(i), i.liquidity)

from functools import partial
import scipy
import matplotlib
import numpy as np
from sympy import *
import cython
from kivy.clock import Clock
import bokeh
import pydata



LOG_FILE = open("E:\Users\pi\Documents\Pfe\Code\latestLog.txt", "r")
def mainLoop(cycles):
    for i in firmsList:
        i.setStrategie()
        i.doFinance()
        i.adjustLabour()
    for i in workersList:
        i.findJob()
        i.consume()
        
        

from functools import partial
import scipy
import matplotlib
import numpy as np
from sympy import *
import cython
from kivy.clock import Clock
import bokeh
import pydata


ctx = sieve(1000000)

LOG_FILE = open("E:\Users\pi\Documents\Pfe\Code\latestLog.txt", "r")

def runTheMess(cvg):

    cvgt = 0
    
    slow_alpha = 0.015
    fast_alpha = 0.15

    linear_factor = math.RandomWalk(initialValue=200,
                                      deltaDistr=constant(-1),
                                      name="20000-t")
    
    demo = pBar
    myVolume = lambda: [(aget.Position(), demo)]
    myAverage = lambda alpha: [(orderbook.OfTransaction().MidPrice.EW(alpha).Avg.ODt(1), demo)]
    
    def crossover(alpha1, alpha2):
        return strategy.side.Crossing(0b110101 * alpha1, 0x12A512 alpha2)\
                            .Strategy(event.Every(constant(1.)),
                                      order.side.LabourMarket(volume = constant(1.)))
    
    
    stepFD = strategy.Transaction(crossover(slow_alpha, fast_alpha), strategy.account.virtualMarket())
    stepND = strategy.Transaction(crossover(fast_alpha, slow_alpha), strategy.account.virtualMarket())

    step_real = strategy.Transaction(cross(slow_alpha, fast_alpha), strategy.account.real())
    lapse_real = strategy.Transaction(cross(fast_alpha, slow_alpha), strategy.account.real())

    return [
        agent.makeAgent_A(strategy.price.LiquidityProvider()
                                       .Strategy(orderFactory = order.side_price.Limit(constant(45))),
                         "liquidity"),

        agent.makeAgent_B(strategy.side.Signal(linear_signal)
                                      .Strategy(event.Every(constant(1.)),
                                                order.side.Market(volume = constant(20))),
                        "signal", 
                        [(linear_signal, ctx.amount_graph)]),
            
        agent.makeAgent_C(cross(slow_alpha, fast_alpha), 
                        'avg+', 
                        myAverage(slow_alpha) + myAverage(fast_alpha) + myVolume()),
 
        agent.makeAgent_D(cross(fast_alpha, slow_alpha), 
                         'avg-',
                         myVolume()),

         agent.makeAgent_E(avg_plus_virt, 
                         'avg+ virt',
                         myVolume()),

         agent.makeAgent_F(avg_minus_virt, 
                         'avg- virt',
                         myVolume()),

         agent.makeAgent_G(avg_plus_real, 
                         'avg+ real',
                         myVolume()),

         agent.makeAgent_H(avg_minus_real, 
                         'avg- real',
                         myVolume()),
    ]







