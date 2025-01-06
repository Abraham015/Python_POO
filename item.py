import csv

class Item:
    ## Class attribute
    pay_rate=0.8 #The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        #Validations
        assert price >= 0, f"Price {price} is not grater than zero!"
        assert quantity>=0, f"Quantity {quantity} is not grater than zero!"
        # Assign to self object
        self.__name=name
        self.price=price
        self.quantity=quantity 
        #Actions to execute
        Item.all.append(self)

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name=value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    def __repr__(self):
        return f"Item ('{self.name}', '{self.price}', '{self.quantity}')"