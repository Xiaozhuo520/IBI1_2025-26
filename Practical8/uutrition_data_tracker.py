class FoodItem:
    def __init__(self, name, calories, protein, carbohydrate, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrate = carbohydrate
        self.fat = fat

def nutrition_anlysis(foods):
    totals = {'calories':0, 'protein':0, 
              'carbohydrate':0, 'fat':0}
    for food in foods:
        totals['calories'] += food.calories
        totals['protein'] += food.protein
        totals['carbohydrate'] += food.carbohydrate
        totals['fat'] += food.fat
    for nutrition in totals:
        print(f'Total {nutrition} is {totals[nutrition]}')
    if totals['calories'] > 2500 or totals['fat'] > 90:
        print('Warning: Your diet is unhealthy')

#example
apple = FoodItem("apple", 60, 0.3, 15, 0.5)
egg = FoodItem("egg", 143, 12.6, 0.7, 9.5)
rice = FoodItem("rice", 130, 2.7, 28, 0.3)
fried_chicken = FoodItem("fried_chiken", 800, 40, 20, 50)
        
daily_food_list = [apple, egg, rice, fried_chicken,
                   fried_chicken,fried_chicken]
nutrition_anlysis(daily_food_list)

daily_food_list = [apple, egg, rice, fried_chicken]
nutrition_anlysis(daily_food_list)