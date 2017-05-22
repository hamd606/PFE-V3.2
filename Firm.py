import random

class Firm(object):
    wage = 1
    alpha = 1
    priceFactor = 0.1
    productionFactor = 0.1
    mu = 0
    sigma = 0.2
    to = 0.05
    stock = []
    demand = []
    freePosition = 0
    def __init__(self, workers, price, production, targetProduction, demand, liquidity, debt):
        self.workers = workers
        self.price = price
        self.production = production
        self.targetProduction = targetProduction
        self.demand = demand
        self.liquidity = random.uniform(60,120)
        self.debt = debt

    def setOwner(owner):
        self.owner = owner

    def setTargets(self):

        if stock[len(stock) - 1] > 0:
            self.targetProduction = production * (1 - uniform(0,1)*discountFactor)
            self.price = price * (1 - uniform(0,1)*discountFactor)
            
        else:
            self.targetProduction = production * (1 + uniform(0,1)*discountFactor)
            self.price = price * (1 + uniform(0,1)*discountFactor)

        if targetProduction < len(workers):
            self.fireWorker()

        else:
            self.hireWorker()

    def setWage(self):
        pass
