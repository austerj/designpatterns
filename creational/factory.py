from abc import ABC, abstractmethod


class Restaurant(ABC):
    @classmethod
    def cook_item(cls, item_from_menu):
        item = cls.create_item(item_from_menu)
        item.cook()
        return item

    @abstractmethod
    def create_item(item_from_menu):
        raise NotImplementedError


class Pizza(ABC):
    def cook(self):
        self.prepare()
        print('putting pizza in the oven')
        print('pizza is done!')

    @abstractmethod
    def prepare(self):
        raise NotImplementedError


class MargheritaPizza(Pizza):
    @staticmethod
    def prepare():
        print('preparing margherita pizza')


class PepperoniPizza(Pizza):
    @staticmethod
    def prepare():
        print('preparing pepperoni pizza')


class PizzaRestaurant(Restaurant):
    def create_item(item_from_menu):
        if item_from_menu == 'margherita':
            return MargheritaPizza()
        elif item_from_menu == 'pepperoni':
            return PepperoniPizza()
        else:
            return None


if __name__ == '__main__':
    # create a pizza restaurant
    restaurant = PizzaRestaurant()
    # cook a margherita pizza
    restaurant.cook_item('margherita')
    # cook a pepperoni pizza
    restaurant.cook_item('margherita')
