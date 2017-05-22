import random


class Household(object):
    #wtf
    M = 0
    #prepensial marginal to consume
    c = 0.8
    savings = 0
    salary = 0
    recievedCash = []
    paidCash = []
    def __init__(self, idNumber, initialCash, minimalWage, working):
        self.idNumber = idNumber
        self.initialCash = initialCash
        self.minimalWage = minimalWage
        self.working = working

    def getMoney(self, amount):
        self.savings += amount
        self.recievedCash.append(amount)
        print "household #%i got %i" %(self.idNumber, amount)

    def payMoney(amount):
        self.savings -= amount
        self.paidCash.append(amount)
        print "household #%i lost %i" %(self.idNumber, amount)


    def findJob(self,firms):
        #take a sample from firms list
        knownFirms = random.sample(firms, int(len(firms)*knownFirmsPercentage))
        #sort knownFirms by wage
        knownFirms.sort(key = lambda x: x.wage())
        knownFirms = list(reversed(knownFirms))
        if len(knownFirms) != 0 :
            if knownFirms[0].wage() < self.minimumWage:
                print "household #%i refused job from %i with wage: %i" %(self.idNumber, knownFirms[0].idNumber, knownFirms[0].wage())
                minimumwage = minimumwage * (1-alpha)
            else:
                print "household #%i accepted job from %i with wage: %i" %(self.idNumber, knownFirms[0].idNumber, knownFirms[0].wage())
                knownFIrms[0].workers.append(self)
                self.working = True

    def loseJob(self):
        print "household #%i lost job" % self.idNumber
        self.working = False

        

    def consume(self,firms):
        budget = savigns*self.c
        if budget > 0:
            #take a sample from firms list
            knownFirms = random.sample(firms, int(len(firms)*knownFirmsPercentage))
            #sort knownFirms by prince
            knownFirms.sort(key = lambda x: x.price())
            #function local variable denoting spent on consuptioin sesion
            spent = 0
            i = 0
            while (i < len(knownFirms)) and  (spent < budget):
                i = i+1
                availableStock = form[i].stock()
                if availableStock > 0:
                    maxConsumptionFromFirm = (budget-spent)/knownFirms[i].price()
                    if evailableStock > maxConsumptionFromFirm:
                        knownFirms[i].sell(maxConsumptionFromFirm)
                    else:
                        knownFirms[i].sell(availableStock)
            self.saving = self.savings - spent
            print "household #%i consumed %i" %(self.idNumber, spent)
                


h1 = Household(0,1,3,False)
print h1.c



