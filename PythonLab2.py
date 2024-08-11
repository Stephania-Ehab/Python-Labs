# Question (1)

import math

def calculateArea(shape, x, y=1):
    if shape == 't':
        return 0.5 * x * y
    elif shape == 'r':
        return x * y
    elif shape == 's':
        return x * x
    elif shape == 'c':
        return math.pi * (x ** 2)
    else:
        return "Invalid shape"

triangle_area = calculateArea('t', 4, 5)
print(f"Area of the triangle: {triangle_area}")

rectangle_area = calculateArea('r', 4, 5)
print(f"Area of the rectangle: {rectangle_area}")

square_area = calculateArea('s', 4)
print(f"Area of the square: {square_area}")

circle_area = calculateArea('c', 4)
print(f"Area of the circle: {circle_area}")


# Question (2)

def locationLetter(sentence, letter):
    indices = []
    
    for index, char in enumerate(sentence):
        if char == letter:
            indices.append(index)
    
    return indices

sentence = "This is javaScript"
letter = "i"
location = locationLetter(sentence, letter)
print(location)


# Question (3)

def multiplicationTable(n):
    table = []

    for i in range(1, n + 1):
        sub_list = [i * j for j in range(1, i + 1)]
        table.append(sub_list)
    
    return table

number = 4
result = multiplicationTable(number)
print(result)


# Question (4) Bonus 

def namesSortedDict(names):
    name_dict = {}

    for name in names:
        first_letter = name[0]
    
        if first_letter in name_dict:
            name_dict[first_letter].append(name)
        else:
            name_dict[first_letter] = [name]

    sorted_name_dict = dict(sorted(name_dict.items()))
    
    return sorted_name_dict

# Example for Question (4) :

names = ["ahmed", "fatma", "ibrahim"]
reS= namesSortedDict(names)
print(result)