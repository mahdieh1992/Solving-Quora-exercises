#بزرگانه
def capitalize(names: list[str]) -> list[str]: 
    names = [name.title() for name in names]
    return names

names = ['ali', 'REYHANEH', 'aMIR', 'AMIR abbas', 'Fatemeh Zahra']
print(capitalize(names))
