from abc import ABC, abstractmethod


class OrderingSystem(ABC):
    @abstractmethod
    def order_item(self, amount):
        raise NotImplementedError


class Warehouse(OrderingSystem):
    def __init__(self, stock):
        self.stock = stock

    def add_warehouse(self, warehouse):
        self.warehouses.append(warehouse)

    def order_item(self, amount):
        if self.stock < amount:
            raise ValueError(
                f'cannot order {amount}, stock is {self.stock}'
            )
        else:
            self.stock -= amount
            print(f'shipping {amount} items, remaining stock is {self.stock}')


class WarehouseProxy(OrderingSystem):
    def __init__(self):
        self.warehouses = []

    def add_warehouse(self, warehouse):
        self.warehouses.append(warehouse)

    @property
    def total_stock(self):
        return sum(warehouse.stock for warehouse in self.warehouses)

    def order_item(self, amount):
        if self.total_stock < amount:
            raise ValueError(
                f'cannot order {amount}, total stock is {self.total_stock}'
            )
        print(f'delegating order of {amount} to warehouses')
        for n, warehouse in enumerate(self.warehouses):
            order_amount = min(amount, warehouse.stock)
            print(f'warehouse {n}: ', end='')
            warehouse.order_item(order_amount)
            amount -= order_amount
            if amount == 0:
                print(f'remaining total stock is {self.total_stock}')
                break

if __name__ == '__main__':
    # create warehouses
    warehouse1 = Warehouse(5)
    warehouse2 = Warehouse(1)
    warehouse3 = Warehouse(22)
    # create proxy for warehouses
    warehouse_proxy = WarehouseProxy()
    warehouse_proxy.add_warehouse(warehouse1)
    warehouse_proxy.add_warehouse(warehouse2)
    warehouse_proxy.add_warehouse(warehouse3)
    # order some items through the proxy
    warehouse_proxy.order_item(4)
    warehouse_proxy.order_item(6)
    warehouse_proxy.order_item(53)
