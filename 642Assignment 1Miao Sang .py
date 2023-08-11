# Miao Sang Assignment 1
# create group exercise class
class GroupExercise:
    def __init__(self, name, max_capacity, fee_amount=0):
        self.__name = name
        self.__trainer = None
        self.__max_capacity = max_capacity
        self.__participants = []
        self.__wait_list = []
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
    
    def get_wait_list(self):
        return self.__wait_list
    
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
            self.__wait_list.append(member)
    
    #remove member        
    def remove_member(self, member):
        if member in self.__participants:
            self.__participants.remove(member)
            member.remove_group_exercise(self)
        elif member in self.__wait_list:
            self.__wait_list.remove(member)
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
    
    #mark attendance
    def mark_attendance(self, member):
        if member in self.__participants:
            if member in self.__checked_in:
                print("Member already checked in")
            else:
                self.__checked_in.append(member)
        else:
            print("Member not enrolled in this group exercise")
    
    #attendance rate
    def attendance_rate(self):
        return len(self.__checked_in) / len(self.__participants)

    def __str__(self):
        return f"GroupExercise(Name: {self.__name}, Trainer: {self.__trainer.get_name() if self.__trainer else 'None'}, Capacity: {self.__max_capacity})"

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
    #book group exercise
    def book_group_exercise(self, group_exercise):
        if group_exercise in self.__enrolled_group_exercise:
            print("You are already enrolled in this group exercise")
        else:
            group_exercise.enroll(self)
    
    #cancel group exercise
    def cancel_group_exercise(self, group_exercise):
        if group_exercise in self.__enrolled_group_exercise:
            group_exercise.remove_member(self)
        else:
            print("You are not enrolled in this group exercise")
            
    #display booked group exercise
    def booked_group_exercise(self):
        for group_exercise in self.__enrolled_group_exercise:
            print(group_exercise.get_name())
            
    def __str__(self):
        return f"Member(Name: {self.__full_name}, Membership No: {self.__id_number})"
    
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
    #display assigned group exercise
    def assigned_group_exercises(self):
        for group_exercise in self.__assigned_group_exercises:
            print(group_exercise.get_name())
            
    #add group exercise
    def add_group_exercise(self, group_exercise):
        if group_exercise in self.__assigned_group_exercises:
            print("This group exercise is already assigned to this trainer")
        else:
            self.__assigned_group_exercises.append(group_exercise)
            
    def __str__(self):
        return f"Trainer(Name: {self.__full_name}, Specialisation: {self.__specialisation})"
    
    
#create test data for group exercise

groupexercise1 = GroupExercise("Yoga", 10, 10)
groupexercise2 = GroupExercise("Zumba", 20, 20)

print(groupexercise1)
print(groupexercise2)

#create test data for members
member1 = Member("Miao Sang", 1)
member2 = Member("Oliver Green", 2)
member3 = Member("John Smith", 3)
member4 = Member("Jane Doe", 4)
member5 = Member("Mary Jane", 5)

print(member1)

#create test data for trainers
trainer1 = Trainer("John Armstrong", "Yoga")
trainer2 = Trainer("peter Parker", "Zumba")

print(trainer1)