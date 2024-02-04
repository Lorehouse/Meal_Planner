import random
from CYL_chicken import cylc
def weekly_dinners():
    casserole, mexican, level_2, instant_pot = dinner_categories()
    bowl = food_in_a_bowl()
    print(casserole, mexican, level_2, instant_pot)
    CYLC = cylc()
    Monday = (f"Monday: {casserole} \n")
    Tuesday = (f"Tuesday {mexican} \n")
    Wednesday = (f"Wednesday: {CYLC} \n")
    Thursday = (f"Thursday: {level_2} \n")
    Friday = ("Friday: pizza \n")
    Saturday = (f"Saturday: {bowl} \n")
    Sunday = (f"Sunday: {instant_pot} \n")
    print(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)


def dinner_categories():
    casserole = ("enchiladas", "baked spaghetti", "chicken broccoli bake", "lasagna", "hash")
    casserole = random.choice(casserole)
    mexican = ("tacos", "burritos", "fajitas", "mexican rice bowls")
    mexican =  random.choice(mexican)
    level_2 = (f"Bonne Femme Chicken:{bonnefemme()}","hash", "crepes", "stromboli", "pita", "taco salad")
    level_2 = random.choice(level_2)
    instant_pot = ("pork pot roast", "beef pot roast", "beef stroganoff", "split pea soup", "goulash", "chili")
    instant_pot = random.choice(instant_pot)
    return (casserole, mexican, level_2, instant_pot)

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
    meat = ("chicken", "ground pork", "ground beef", "meatballs", "kofte", "egg", "pork", "steak")
    vegetable = ("broccoli", "peppers", "green beans", "corn", "peas", "carrots", "asparagus")
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
