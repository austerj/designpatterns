from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        raise NotImplementedError

    def cook(self):
        self.prepare()
        print('cooking pizza')


class BasicPizza(Pizza):
    @staticmethod
    def prepare():
        print('preparing pizza with tomato and cheese')


class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def prepare(self):
        self.pizza.prepare()


class PepperoniPizza(PizzaDecorator):
    def prepare(self):
        super().prepare()
        print('adding pepperoni')


class ExtraCheesePizza(PizzaDecorator):
    def prepare(self):
        super().prepare()
        print('adding extra cheese')


if __name__ == '__main__':
    # create basic pizza
    pizza = BasicPizza()
    # add pepperoni and lots of extra cheese
    pizza = PepperoniPizza(pizza)
    pizza = ExtraCheesePizza(pizza)
    pizza = ExtraCheesePizza(pizza)
    # prepare and cook the pizza
    pizza.cook()
