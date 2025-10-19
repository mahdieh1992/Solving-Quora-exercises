from person import Person,Consts,math

class Engineer(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name,age)
        self.job = "engineer"

    def get_price(self) -> int:
        price = math.floor(Consts.BASE_PRICE["engineer"] * math.sqrt(Consts.MIN_AGE / self.age))
        return int(price)
    
    def calc_life_cost(self) -> int:
        costs = math.floor(Consts.BASE_COST["engineer"] * math.sqrt(self.age / Consts.MIN_AGE))
        return int(costs)

    def calc_income(self) -> int:
        income = math.floor(Consts.BASE_INCOME['engineer']['mine'] * math.sqrt(Consts.MIN_AGE / self.age))
        return int(income)