from person import Person,Consts,math

class Worker(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name,age)
        self.job = "worker"

    def get_price(self) -> int:
        price = math.floor(Consts.BASE_PRICE["worker"] * (Consts.MIN_AGE / self.age))
        return int(price)
    
    def calc_life_cost(self) -> int:
        costs = math.floor(Consts.BASE_COST["worker"] * (self.age / Consts.MIN_AGE))
        return int(costs)
    
    def calc_income(self) -> int:
        income = math.floor(Consts.BASE_INCOME['worker']['mine'] * (Consts.MIN_AGE / self.age))
        return int(income)