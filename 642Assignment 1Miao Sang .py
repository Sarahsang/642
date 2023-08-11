# Miao Sang Assignment 1
class GroupExercise:
    def __init__(self, name, trainer, maxcapacity, feeamount = 0):
        self.__Name = name
        self.__Trainer = None
        self.__MaxCapacity = maxcapacity
        self.__Participants = []
        self.__WaitList = []
        self.__Fee = feeamount
        self.__CheckIn = []
        
    def getName(self):
        return self.__Name   
    def getTrainer(self):
        return self.__Trainer
    def setTrainer(self, trainer):
        self.__Trainer = trainer
        trainer.addGroupExercise(self)
    def getMaxCapacity(self):
        return self.__MaxCapacity
    def getParticipants(self):
        return self.__Participants
    def getWaitList(self):
        return self.__WaitList
    def getFee(self):
        return self.__Fee
    def setFee(self, feeamount):
        self.__Fee = feeamount
    
    def