class WorkPlaceIsFull(Exception):
    def __str__(self) -> str:
        return "work place is full!"
    
class Consts:
        BASE_PRICE = {'mine': 150, 'school': 100, 'company': 90}
        BASE_PLACE_COST = 2500
        LEVEL_MUL = 50    

class WorkPlace:
    instances = []
    
    def __init__(self,name):
        self.name = name
        self.level = 1
        self.expertise = ""
        self.employees = []
        self.capacity = 1
        WorkPlace.instances.append(self)
    
    def get_price(self) -> int:
        const = Consts()
        expertise = self.expertise
        const_work_place = const.BASE_PRICE[expertise]
        return const_work_place
    
    def upgrade(self) -> None:
        self.level += 1
        self.calc_capacity()
        
    def hire(self, person) -> None:
        count_employee = len(self.employees)
        if count_employee >= self.capacity:
            raise WorkPlaceIsFull()
        self.employees.append(person)
        person.work_place = self
    
    def calc_capacity(self) -> None:
        pass
    
    def calc_costs(self) -> None:
        pass
    
    def get_expertise(self) -> str:
        return self.expertise
    
    def calc(self) -> int:
        return -(self.calc_costs())
    
    @staticmethod
    def calc_all() -> int:
        result = 0
        for work in WorkPlace.instances:
            result += work.calc()
        return result