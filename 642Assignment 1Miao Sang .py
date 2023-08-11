# Miao Sang Assignment 1
# create group exercise class
class GroupExercise:
    def __init__(self, name, max_capacity, fee_amount=0):
        self.__name = name
        self.__trainer = None
        self.__max_capacity = max_capacity
        self.__participants = []
        self.__waitlist = []
        self.__fee_amount = fee_amount
        self.__checked_in = []
    
    # Getter and setter methods
    
    def get_name(self):
        return self.__name
    
    def get_trainer(self):
        return self.__trainer
    
    def set_trainer(self, trainer):
        self.__trainer = trainer
        trainer.add_group_exercise(self)
    
    def get_max_capacity(self):
        return self.__max_capacity
    
    def get_participants(self):
        return self.__participants
    
    def get_waitlist(self):
        return self.__waitlist
    
    def get_fee_amount(self):
        return self.__fee_amount
    
    def set_fee_amount(self, fee_amount):
        self.__fee_amount = fee_amount
    
    def get_checked_in(self):
        return self.__checked_in
    
    # Methods for GroupExercise
    #enroll member
    def enroll(self, member):
        if len(self.__participants) < self.__max_capacity:
            self.__participants.append(member)
            member.add_group_exercise(self)
        else:
            self.__waitlist.append(member)
    
    #remove member        
    def remove_member(self, member):
        if member in self.__participants:
            self.__participants.remove(member)
            member.remove_group_exercise(self)
        elif member in self.__waitlist:
            self.__waitlist.remove(member)
        else:
            print("Member not found")
    
    #display members enrolled
    def enrolled_members(self):
        for member in self.__participants:
            print(member.get_full_name())
            
    #assign trainer
    def assign_trainer(self, trainer):
        self.__trainer = trainer
        trainer.add_group_exercise(self)
        
    #number of participants
    def count_participants(self):
        return len(self.__participants)
    
    #available slots
    def available_slots(self):
        return self.__max_capacity - len(self.__participants)
    
    #payments received
    def payments_received(self):
        return self.__fee_amount * len(self.__participants)
    
    #attendance
    def attendance(self):
        return len(self.__checked_in)

# create member class

class Member:
    def __init__(self, full_name, id_number):
        self.__full_name = full_name
        self.__id_number = id_number
        self.__enrolled_group_exercise = []
        
    # Getter and setter methods
    
    def get_full_name(self):
        return self.__full_name
    def get_id_number(self):
        return self.__id_number
    def get_enrolled_group_exercise(self):
        return self.__enrolled_group_exercise
    
    # methods for Member
    
    
    
#create trainer class
class Trainer:
    def __init__(self, full_name, specialisation):
        self.__full_name = full_name
        self.__specialisation = specialisation
        self.__assigned_group_exercises = []
        
    # Getter and setter methods
    def get_full_name(self):
        return self.__full_name
    def get_specialisation(self):
        return self.__specialisation
    def get_assigned_group_exercises(self):
        return self.__assigned_group_exercises

    # methods for Trainer
    