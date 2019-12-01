input_test = [12, 14, 1969, 100756]

modules = []
with open('input_Day_1', "r") as file:
    for x in file:
        modules.append(int(x))

# Part1
def define_fuel(mass):
    fuel = mass//3 - 2
    return fuel


def fuel_for_the_fuel_god(mass, fuel_sum):
    fuel_mass = define_fuel(mass)
    if fuel_mass < 0:
        return fuel_sum
    else:
        fuel_sum += fuel_mass
        return fuel_for_the_fuel_god(fuel_mass, fuel_sum)

print("# Part 1")
# Test Part 1
sum_test = 0
for module in input_test:
    sum_test += define_fuel(module)
print("Test sum " + str(sum_test))

# Part 1
sum_input = 0
for module in modules:
    sum_input += define_fuel(module)
print("Modules sum " + str(sum_input))

print("# Part 2")
# Test Part 2
for i, mass in enumerate(input_test):
    print(str(i) + "°) Test ", fuel_for_the_fuel_god(mass, 0))

# Part 2
fuel_sum_test = 0
for mass in modules:
    fuel_sum_test += fuel_for_the_fuel_god(mass, 0)
print(fuel_sum_test)