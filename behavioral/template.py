from abc import ABC, abstractmethod


class PastaDish(ABC):
    def make_dish(self):
        self.boil_water()
        self.cook_pasta()
        self.drain_pasta()
        self.add_pasta()
        self.add_sauce()
        self.add_protein()
        self.add_garnish()

    @staticmethod
    def boil_water():
        print('boiling water')

    @staticmethod
    def cook_pasta():
        print('cooking pasta')

    @staticmethod
    def drain_pasta():
        print('draining pasta')

    @abstractmethod
    def add_pasta():
        raise NotImplementedError

    @abstractmethod
    def add_sauce():
        raise NotImplementedError

    @abstractmethod
    def add_protein():
        raise NotImplementedError

    @abstractmethod
    def add_garnish():
        raise NotImplementedError


class SpaghettiMeatballs(PastaDish):
    @staticmethod
    def add_pasta():
        print('adding spaghetti')

    @staticmethod
    def add_sauce():
        print('adding tomato sauce')

    @staticmethod
    def add_protein():
        print('adding meatballs')

    @staticmethod
    def add_garnish():
        print('adding parmesan')


class PenneAlfredo(PastaDish):
    @staticmethod
    def add_pasta():
        print('adding penne')

    @staticmethod
    def add_sauce():
        print('adding alfredo sauce')

    @staticmethod
    def add_protein():
        print('adding chicken')

    @staticmethod
    def add_garnish():
        print('adding parsley')


if __name__ == '__main__':
    # make pasta dishes
    SpaghettiMeatballs().make_dish()
    PenneAlfredo().make_dish()
