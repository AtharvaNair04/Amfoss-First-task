import pyinputplus as pyip
bread_prices = {'wheat': 2.00, 'white': 1.00, 'sourdough': 3.00}
protein_prices = {'chicken': 2.00, 'turkey': 2.50, 'ham': 2.00, 'tofu': 2.50}
cheese_prices = {'cheddar': 1.00, 'Swiss': 1.50, 'mozzarella': 1.50}
condiment_prices = {'mayo': 0.50, 'mustard': 0.25, 'lettuce': 0.50, 'tomato': 0.50}
def calculate_cost(bread, protein, has_cheese, cheese, condiments, num_sandwiches):
    total_cost = (bread_prices[bread] + protein_prices[protein])
    if has_cheese:
        total_cost += cheese_prices[cheese]
    for condiment in condiments:
        total_cost += condiment_prices[condiment]
    return total_cost * num_sandwiches
bread_choice = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True)
protein_choice = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)
has_cheese = pyip.inputYesNo('Would you like cheese? (yes/no): ')
cheese_choice = None
if has_cheese:
    cheese_choice = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered=True)
condiments = pyip.inputYesNo('Do you want mayo? (yes/no): '),
            pyip.inputYesNo('Do you want mustard? (yes/no): '),
            pyip.inputYesNo('Do you want lettuce? (yes/no): '),
            pyip.inputYesNo('Do you want tomato? (yes/no): ')
num_sandwiches = pyip.inputInt('How many sandwiches?, min=1)
total_cost = calculate_cost(bread_choice, protein_choice, has_cheese, cheese_choice, condiments, num_sandwiches)
print(f'Total cost for {num_sandwiches} sandwiches: ${total_cost:.2f}')
