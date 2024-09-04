class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_val):
        if (
            isinstance(name_val, str)
            and len(name_val) >= 3
            and not hasattr(self, "name")
        ):
            self._name = name_val
        else:
            raise Exception("name already exists")

    def orders(self):
        return [
            order
            for order in Order.all
            if order.coffee == self and isinstance(order.coffee, Coffee)
        ]

    def customers(self):
        return [*set([order.customer for order in self.orders()])]

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        return sum([order.price for order in self.orders()]) / self.num_orders()


class Customer:

    all = []

    @classmethod
    def most_aficionado(cls, coffee):
        cust_spend = {}
        for customer in coffee.customers():
            cust_spend[customer] = sum(
                [order.price for order in coffee.orders() if order.customer == customer]
            )
        return max(cust_spend, key=cust_spend.get)

    def __init__(self, name):
        self.name = name
        self.__class__.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name must be a string between 1 and 15 characters")

    def orders(self):
        return [
            order
            for order in Order.all
            if order.customer == self and isinstance(order, Order)
        ]

    def coffees(self):
        # returns a UNIQUE list of all the coffees a customer has ordered
        return [*set([order.coffee for order in self.orders()])]

    def create_order(self, coffee, price):
        return Order(self, coffee, price)


class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self.__class__.all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price_val):
        if (
            isinstance(price_val, float)
            and 1.0 <= price_val <= 10.0
            and not hasattr(self, "price")
        ):
            self._price = price_val
        else:
            raise Exception

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, cust_obj):
        if isinstance(cust_obj, Customer):
            self._customer = cust_obj
        else:
            raise Exception

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee_obj):
        if isinstance(coffee_obj, Coffee):
            self._coffee = coffee_obj
        else:
            raise Exception
