#مساحت
import math
from typing import Callable

def get_func(ls: list[str]) -> list[Callable]:
    ls_result = []
    for shape in ls:
        shape = shape.lower()
        if shape == 'square':
            square_func = lambda a : a * a
            ls_result.append(square_func)
            
        elif shape == 'circle':
            circle_func = lambda r : (r * r ) * math.pi
            ls_result.append(circle_func)
            
        elif shape == 'rectangle':
            rectangle_func = lambda l,w : l * w
            ls_result.append(rectangle_func)
            
        elif shape == 'triangle':
            triangle_func = lambda b, h : (1 / 2) * b * h
            ls_result.append(triangle_func)
    return ls_result
    
    
shape_list = ['square', 'circle', 'rectangle', 'triangle']
area_functions = get_func(shape_list)

print(f"Area of square with side 1: {area_functions[0](1)}")
print(f"Area of circle with radius 2: {area_functions[1](2)}")
print(f"Area of rectangle with length 2, width 4: {area_functions[2](2, 4)}")
print(f"Area of triangle with base 5, height 4: {area_functions[3](4, 5)}") 