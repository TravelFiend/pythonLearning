MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.0

customerChoice = input(' What would you like? (espresso/latte/cappuccino): ')
print('Please insert coins.')

enoughWater = MENU[customerChoice]['ingredients']['water'] <= resources['water']
enoughMilk = MENU[customerChoice]['ingredients']['milk'] <= resources['milk']
enoughCoffee = MENU[customerChoice]['ingredients']['coffee'] <= resources['coffee']
enoughResources = enoughWater and enoughMilk and enoughCoffee

if customerChoice == 'report':
  print(f'Water: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: ${money}')
else:
  quarters = float(input('How many quarters?: ')) * 25 / 100
  dimes = float(input('How many dimes?: ')) * 10 / 100
  nickels = float(input('How many nickels?: ')) * 5 / 100
  pennies = float(input('How many pennies?: ')) / 100

  totalPaid = quarters + dimes + nickels + pennies;

  if totalPaid >= MENU[customerChoice]['cost'] and enoughResources:
    money += MENU[customerChoice]["cost"]
    resources['water'] -= MENU[customerChoice]['ingredients']['water']
    resources['milk'] -= MENU[customerChoice]['ingredients']['milk']
    resources['coffee'] -= MENU[customerChoice]['ingredients']['coffee']
    print(f'Here is ${round(totalPaid - MENU[customerChoice]["cost"], 2)} in change.')
    print(f'Here is your {customerChoice} ☕️ Enjoy!')
  else:
    outOf = ''
    if not enoughWater:
      outOf = 'water'
    elif not enoughMilk:
      outOf = 'milk'
    elif not enoughCoffee:
      outOf = 'coffee'

    print(f'Sorry, there is not enough {outOf}.')
