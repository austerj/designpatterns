from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, colleague, event):
        raise NotImplementedError

    def add_colleague(self, colleague):
        colleague.mediator = self
        return colleague


class Colleague(ABC):
    def __init__(self, mediator=None):
        self.mediator = mediator

    @abstractmethod
    def notify(self, event):
        raise NotImplementedError


class HouseMediator(Mediator):
    def __init__(self, motion_detector, thermostat, coffee_maker, phone):
        self.home = True
        self.motion_detector = self.add_colleague(motion_detector)
        self.thermostat = self.add_colleague(thermostat)
        self.coffee_maker = self.add_colleague(coffee_maker)
        self.phone = self.add_colleague(phone)

    def notify(self, colleague, event):
        if colleague == self.motion_detector:
            if event == 'entry' and not self.home:
                self.home = True
                self.thermostat.increase()
            elif event == 'exit' and self.home:
                self.home = False
                self.thermostat.reduce()
        elif colleague == self.thermostat:
            pass
        elif colleague == self.coffee_maker:
            pass
        elif colleague == self.phone:
            if event == 'alarm' and self.home:
                self.coffee_maker.brew_coffee()
        else:
            raise ValueError('unknown colleague')


class HouseColleague(Colleague):
    def notify(self, event):
        self.mediator.notify(self, event)


class MotionDetector(HouseColleague):
    def enter(self):
        print('house entry detected')
        self.notify('entry')

    def exit(self):
        print('house exit detected')
        self.notify('exit')


class Thermostat(HouseColleague):
    def increase(self):
        print('increasing house temperature')
        self.notify('increase')

    def reduce(self):
        print('reducing house temperature')
        self.notify('reduce')


class CoffeeMaker(HouseColleague):
    def brew_coffee(self):
        print('brewing coffee')
        self.notify('coffee')


class Phone(HouseColleague):
    def alarm(self):
        print('phone alarm goes beep-beep-beep')
        self.notify('alarm')


if __name__ == '__main__':
    # create colleagues
    motion_detector = MotionDetector()
    thermostat = Thermostat()
    coffee_maker = CoffeeMaker()
    phone = Phone()
    # create mediator
    mediator = HouseMediator(motion_detector, thermostat, coffee_maker, phone)
    # phone alarm and home -> brew coffee
    phone.alarm()
    # leave house -> reduce temperature
    motion_detector.exit()
    # phone alarm and not home -> do nothing
    phone.alarm()
    # come home -> increase temperature
    motion_detector.enter()
