from abc import ABCMeta, abstractmethod

##########################################################################
#This is the Observble class that is responsible for adding in observers,
#removing observers, and updating observers
##########################################################################
class Observable(object):
    
    ###################################################################
    #Constructor for obervable class. Creates a list to hold Observers
    ###################################################################
    def __init__(self):
        self.observers = []

    ###################################################################
    #Method that adds observers to the list
    ###################################################################
    def register(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    ###################################################################
    #Method that removes observers from the list
    ###################################################################
    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    ###################################################################
    #Method that removes all observers from the list
    ###################################################################
    def unregister_all(self):
        if self.observers:
            del self.observers[:]
    
    ###################################################################
    #When the observers state changes it calls this method to notify
    #the observer by calling the observers update method.
    ###################################################################
    def update_observers(self, something):
        for observer in self.observers:
            observer.update(something)

##########################################################################
#Abstrack Observer class. updated method is then called by the observable
#class.
##########################################################################
class Observer(object):
    __metaclass__ = ABCMeta
 
    @abstractmethod
    def update(self, something):
        pass
