from abc import ABC, abstractmethod


class VendingMachineState(ABC):
    @abstractmethod
    def insert_dollar():
        raise NotImplementedError

    @abstractmethod
    def eject_money():
        raise NotImplementedError

    @abstractmethod
    def dispense():
        raise NotImplementedError


class HasDollarState(VendingMachineState):
    @staticmethod
    def insert_dollar(vending_machine):
        print('machine already has a dollar')

    @staticmethod
    def eject_money(vending_machine):
        print('returning dollar from machine')
        vending_machine.state = vending_machine.idle_state

    @staticmethod
    def dispense(vending_machine):
        vending_machine.stock -= 1
        print('dispensing item')
        if vending_machine.stock > 0:
            vending_machine.state = vending_machine.idle_state
        else:
            vending_machine.state = vending_machine.out_of_stock_state


class IdleState(VendingMachineState):
    @staticmethod
    def insert_dollar(vending_machine):
        print('inserted dollar in machine')
        vending_machine.state = vending_machine.has_dollar_state

    @staticmethod
    def eject_money(vending_machine):
        print('machine has no dollar to eject')

    @staticmethod
    def dispense(vending_machine):
        print('insert dollar before trying to dispense item')


class OutOfStockState(VendingMachineState):
    @staticmethod
    def insert_dollar(vending_machine):
        print('machine is out of stock, returning dollar from machine')

    @staticmethod
    def eject_money(vending_machine):
        print('machine has no dollar to eject')

    @staticmethod
    def dispense(vending_machine):
        print('insert dollar before trying to dispense item')


class VendingMachine:
    has_dollar_state = HasDollarState()
    idle_state = IdleState()
    out_of_stock_state = OutOfStockState()

    def __init__(self, stock):
        self.stock = int(stock)
        if stock > 0:
            self.state = self.idle_state
        else:
            self.stock = 0
            self.state = self.out_of_stock_state

    def insert_dollar(self):
        self.state.insert_dollar(self)

    def eject_money(self):
        self.state.eject_money(self)

    def dispense(self):
        self.state.dispense(self)


if __name__ == '__main__':
    # create vending machine with 2 items in stock
    vending_machine = VendingMachine(2)
    # dispense items
    vending_machine.dispense()
    vending_machine.insert_dollar()
    vending_machine.dispense()
    vending_machine.eject_money()
    vending_machine.insert_dollar()
    vending_machine.dispense()
    vending_machine.insert_dollar()
