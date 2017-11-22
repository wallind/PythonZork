from abc import ABCMeta, abstractmethod

#This is the observerable class

class Observable(object):
 
    def __init__(self):
        self.observers = []
 
    def register(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)
 
    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
 
    def unregister_all(self):
        if self.observers:
            del self.observers[:]
 
    def update_observers(self, something, something2):
        for observer in self.observers:
            observer.update(something, something2)


class Observer(object):
    __metaclass__ = ABCMeta
 
    @abstractmethod
    def update(self, something):
        pass
