import random
from CYL_chicken import cylc
def weekly_dinners():
    casserole, mexican, level_2, instant_pot, weekend, grill = dinner_categories()
    bowl = food_in_a_bowl()
    french = bonnefemme()
    CYLChicken = cylc()
    lunch = cold_lunch()
    dinner = hot_lunch()
    Monday = (f"Monday:\n\t Lunch: {lunch}\n\t Dinner: {dinner} \n")
    lunch = cold_lunch()
    Tuesday = (f"Tuesday:\n\t Lunch: {lunch}\n\t Dinner: {mexican} \n")
    lunch = hot_lunch()
    Wednesday = (f"Wednesday:\n\t Lunch: {lunch}\n\t Dinner: {CYLChicken} \n")
    lunch = cold_lunch()
    Thursday = (f"Thursday:\n\t Lunch: {lunch}\n\t Dinner: {level_2} \n")
    lunch = cold_lunch()
    Friday = (f"Friday:\n\t Lunch: {lunch}\n\t Dinner: pizza \n")
    lunch = hot_lunch()
    Saturday = (f"Saturday:\n\t Lunch: {lunch}\n\t Dinner: {weekend} \n")
    lunch = cold_lunch()
    Sunday = (f"Sunday:\n\t Lunch: {lunch}\n\t Dinner: {grill} \n")
    print(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)


def dinner_categories():
    casserole = ("enchiladas", "baked spaghetti", "chicken broccoli bake", "lasagna", "hash")
    casserole = random.choice(casserole)
    mexican = ("tacos", "burritos", "fajitas", "mexican rice bowls")
    mexican =  random.choice(mexican)
    level_2 = (f"Bonne Femme Chicken:{bonnefemme()}","hash", "crepes", "stromboli", "pita", "taco salad", "risotto", "curry")
    level_2 = random.choice(level_2)
    instant_pot = ("pork pot roast", "beef pot roast", "beef stroganoff", "split pea soup", "goulash", "chili")
    instant_pot = random.choice(instant_pot)
    weekend = ("quiche", "french toast", "bacon and eggs", "chicken nuggets", "fish")
    weekend = random.choice(weekend)
    grill = ("burgers", "brats", "chicken thighs", "boneless chicken", "whole chicken", "kebab", "kofte")
    grill = random.choice(grill)
    return (casserole, mexican, level_2, instant_pot, weekend, grill)

def cold_lunch():
    cd_lunch = ("pasta salad", "sandwiches", "wraps", "charcuterie", "chicken salad", "couscous")
    return cd_lunch

def hot_lunch():
    ht_lunch = ("ramen", "pasta", "grilled cheese", "popovers", "dutch baby", "chips and dip", "mac and cheese", "nuggets and fries", "fish sticks")
    return ht_lunch

def bonnefemme():
    meat = ("chicken", "pork chops")
    vegetables = ("onion", 
                 "broccoli", 
                 "peas", 
                 "carrots", 
                 "corn", 
                 "brussels sprouts", 
                 "cabbage", 
                 "parsnips", 
                 "beets", 
                 "leeks", 
                 "spinach",
                 "peppers",
                 "asparagus",
                 )
    sauce = ("cream sauce",
            "mustard sauce",
            "mushroom sauce",
            "gravy sauce",
            "pepper sauce",
            )
    meal = (random.choice(meat), random.choice(vegetables), random.choice(sauce))
    return meal


def food_in_a_bowl():
    toppings = bowl_toppings()
    meat = ("chicken", 
            "ground pork", 
            "ground beef", 
            "meatballs", 
            "kofte", 
            "egg", 
            "pork", 
            "steak")
    vegetable = ("broccoli", 
                 "peppers", 
                 "green beans", 
                 "corn", 
                 "peas", 
                 "carrots", 
                 "asparagus")
    bowl = ("rice", random.choice(meat), random.choice(vegetable), toppings)
    return bowl

def bowl_toppings():
    mediterranean = ("parsley, lemon slices, feta, tzatziki")
    italian = ("basil, tomatoes, olive oil, parmesan")
    faux_asian = ("sesame seeds, scallions, soy sauce, ginger, sesame oil")
    faux_thai = ("crushed peanuts, coconut curry sauce, scallions")
    mid_med = ("cacik, sesame seeds, feta, pepper paste, mint")
    mexish = ("cilantro, tomatoes, avocado, lime widges, salsa, cheese")
    murican = ("cheddar, sour cream, scallions, bacon bits")
    toppings = (mediterranean, italian, faux_asian, faux_thai, mid_med, mexish, murican)
    toppings = random.choice(toppings)
    return toppings

#CYL Chicken requires chicken, starch, two vegetables, seasoning 
# import random
# def cylc():
#     seasoning = seasonings()
#     starch = ("sweet potato", "carrots", "winter squash", "chickpeas")
#     green_vegetable = ("green beans", "broccoli", "cabbage", "snow peas", "asparagus", "bok choy", "brussels sprouts")
#     color_vegetable = ("bell peppers", "summer squash", "parsnips", "beets", "mushrooms", "tomatoes")
#     CYLC = ("bone-in chicken", "onion", "potato", random.choice(starch), random.choice(green_vegetable), random.choice(color_vegetable), seasoning)
#     return(CYLC)

# def seasonings():
#     go_to = ("salt", "pepper", "garlic powder", "onion powder", "smoked paprika")
#     faux_french = ("salt", "pepper", "tarragon", "marjoram", "sage", "garlic powder", "minced onion")
#     kofte = ("salt", "pepper", "pul biber", "cumin", "sumac","minced onion")
#     turkish = ("salt", "pepper", "pul biber", "parsley", "garlic")
#     autumn = ("salt", "pepper", "onion powder", "sage", "nutmeg")
#     faux_italian = ("salt", "pepper", "garlic powder", "oregano", "basil", "thyme", "parmesan powder")
#     jerk = ("salt", "onion powder", "garlic powder", "cayenne pepper", "smoked paprika", "allspice", "pepper", "pepper flakes", "cumin", "nutmeg", "cinnamon", "brown sugar", "thyme", "parsley")
#     seasoning = (go_to, faux_french, kofte, turkish, autumn, faux_italian, jerk, "cajun", "ranch")
#     return(random.choice(seasoning))

weekly_dinners()
