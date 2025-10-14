#مدیریت داروخانه
class Drug:
    def __init__(self,name: str,amount: int,price: int) -> None:
        self.name = name
        self.amount = amount
        self.price = price

class Pharmacy:
    def __init__(self,name: str):
        self.name = name
        self.drugs = []
        self.employees = []
        
    def add_drug(self, drug: Drug):
        self.drugs.append(drug)
        
    def add_employee(self,first_name: str,last_name: str,age: int):
        employee = {
        'first_name' : first_name,
        'last_name' : last_name,
        'age' : age
        }
        self.employees.append(employee)
    
    def total_value(self)-> int:
        values = []
        for items in self.drugs:
           values.append(items.amount * items.price) 
        return sum(values)
                
    def employees_summary(self) -> str:
        result = f"Employees:\n"
        for index,employ in enumerate(self.employees):
            result +=f"The employee number {index + 1} is {employ['first_name']} {employ['last_name']} who is {employ['age']} years old.\n"
        return result    
# ساخت چند شیء دارو
drug1 = Drug("Aspirin", 100, 25000)
drug2 = Drug("Ibuprofen", 50, 40000)
drug3 = Drug("Vitamin C", 200, 100000)

# 2. ساخت یک شیء داروخانه
my_pharmacy = Pharmacy("City Pharmacy")

print(f"Created Pharmacy: {my_pharmacy.name}")
print("-" * 20)


# افزودن داروها به داروخانه
my_pharmacy.add_drug(drug1)
my_pharmacy.add_drug(drug2)
my_pharmacy.add_drug(drug3)

print(f"Number of drugs in {my_pharmacy.name}: {len(my_pharmacy.drugs)}")
print("-" * 20)

# افزودن کارمندان به داروخانه
my_pharmacy.add_employee("Alice", "Smith", 25)
my_pharmacy.add_employee("Bob", "Johnson", 30)

# محاسبه و چاپ ارزش داروها
total_inventory_value = my_pharmacy.total_value()

print(f"Total value of drugs in {my_pharmacy.name}: {total_inventory_value}")
print("-" * 20)


# دریافت و چاپ اطلاعات کارمندان
employee_list_summary = my_pharmacy.employees_summary()

print(employee_list_summary)