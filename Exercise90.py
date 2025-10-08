#میوه‌خوری
def good_fruits(fruits: tuple[dict]) -> dict[str,int]:
    fruits_special = {}
    for d_fruit in fruits:
            if d_fruit['shape'] == 'sphere' and (300 <= d_fruit['mass'] <= 600) and (100 <= d_fruit['volume'] <= 500):
                fruits_special[d_fruit['name']] = fruits_special.get(d_fruit['name'],0) + 1
    return fruits_special

print(
good_fruits((
    {'name':'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
    {'name':'mango', 'shape': 'square', 'mass': 150, 'volume': 120}, 
    {'name':'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
    {'name':'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250})))