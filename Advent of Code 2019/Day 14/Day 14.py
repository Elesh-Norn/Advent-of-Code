from sklearn.linear_model import LinearRegression
import numpy as np
def read_input():
    formulas = {}
    key_quant = {}
    with open('input_Day_14.txt', "r") as file:
        for x in file:
            s = x.strip().split(" ")
            product = s.pop()
            formulas[product] = {}
            key_quant[product] = int(s.pop())
            s.pop()
            while s:
                chem = s.pop()
                chem = chem.replace(",", "")
                formulas[product][chem] = int(s.pop())

    return formulas, key_quant


whiteboard = read_input()

formula = whiteboard[0]
quant = whiteboard[1]
inventory = {}
inventory['ORE'] = float("inf")
for k in quant.keys():
    inventory[k] = 0

def fabricate(fuel_quantity):
    ore_count = 0
    to_fabricate = [('FUEL', fuel_quantity)]
    x = []
    y = []

    while to_fabricate:
        plan = to_fabricate[-1]
        if inventory[plan[0]] < plan[1]:
            can = True
            for element, quantity in formula[plan[0]].items():
                if inventory[element] < quantity:
                    can = False
                    to_fabricate.append((element, quantity))
            if can:
                for element, quantity in formula[plan[0]].items():
                    if element == 'ORE':
                        ore_count += quantity
                    inventory[element] -= quantity
                inventory[plan[0]] += quant[plan[0]]
                #Part 2
                if plan[0] == 'FUEL':
                    x.append(ore_count)
                    y.append(inventory['FUEL'])
                    if inventory['FUEL'] % 1000 == 0:
                        print("Calculating beep boop: " + str(int(inventory['FUEL']/1000)) + "/10")
        else:
            to_fabricate.pop()

    print("Ore used:", ore_count)
    return x, y
#Part 1 (1 Fuel)
fabricate(1)

#Part 2 (Look at 10 000 Fuel Ore Usage and predict for the trillion Ore))
x, y = fabricate(10000)
model = LinearRegression()
x = np.array(x).reshape((-1, 1))
model.fit(x, y)
print(model.predict([[1000000000000]]))
