from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self):
        self.position = 0
        self.path = 'root'

    @abstractmethod
    def get_path(self):
        raise NotImplementedError

    def set_position(self, position):
        self.position = position

    def set_path(self, parent):
        self.path = f'{parent.path}->{self.position}'


class Branch(Component):
    def __init__(self):
        super().__init__()
        self.components = []

    def get_path(self):
        print(f'i am a branch at {self.path}')

    def add_component(self, component):
        component.set_position(len(self.components))
        component.set_path(self)
        self.components.append(component)


class Leaf(Component):
    def get_path(self):
        print(f'i am a leaf at {self.path}')


if __name__ == '__main__':
    # root branch
    root = Branch()
    root.add_component(Branch())
    root.add_component(Branch())
    # add children to subbranch 1
    root.components[0].add_component(Branch())
    root.components[0].add_component(Leaf())
    # add children to subbranch 2
    root.components[1].add_component(Leaf())
    root.components[1].add_component(Branch())
    root.components[1].add_component(Branch())
    root.components[1].add_component(Leaf())
    # get location of a branch and leaf
    root.components[0].get_path()
    root.components[1].components[3].get_path()
