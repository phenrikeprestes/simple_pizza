import sys


print('Pizza Delivery')
print('################################')
print('')
print('Cheese = 1')
print('Veggie = 2')
print('Pepperoni = 3')
print('Meat = 4')
print('Margherita = 5')
print('BBQ Chicken = 6')
print('Hawaiian = 7')
print('Buffalo = 8')
print('Supreme = 9')
print('The Works = 10')
print('About = 0')
print('')

Cheese = 1
Veggie = 2
Pepperoni = 3
Meat = 4
Margherita = 5
BBQChicken = 6
Hawaiian = 7
Buffalo = 8
Supreme = 9
TheWorks = 10


choose = int(input('Digite o Número de sua pizza  '))


if choose == 1:
    print('Your pizza is Cheese')
elif choose == 2:
    print('Your pizza is Veggie')
elif choose == 3:
    print('Your pizza is Pepperoni')
elif choose == 4:
    print('Your pizza is Meat')
elif choose == 5:
    print('Your pizza is Margherita')
elif choose == 6:
    print('Your pizza is BBQ Chicken')
elif choose == 7:
    print('Your pizza is Hawaiian')
elif choose == 8:
    print('Your pizza is Buffalo')
elif choose == 9:
    print('Your pizza is Supreme')
elif choose == 10:
    print('Your pizza is The Works')
else:
    print('Invalid option. Try placing your order again')
    sys.exit()

print('#################################')
print('')

print('Press 1 for yes or 2 for no')
plus = int(input('Do you want any extra?  '))

if plus == 1:
    print('Extra Cheese = 1, Extra Meat = 2, Extra Vegetable = 3')

else:
    print('OK')

extraCheese = 1
extraMeat = 2
extraVegetable = 3

extra = int(input('Type the extra  '))

if extra == 1:
    print('Extra Cheese Add')
elif extra == 2:
    print('Extra Meat Add')
else:
    print('Extra Vegetable')

print('Your pizza  is read. Bon Apettit!!')
