import random
from CYL_chicken import cylc
def weekly_dinners():
    casserole, mexican, OnePot, level_two, instant_pot, weekend, grill, cold_dinner = dinner_categories()
    bowl = food_in_a_bowl()
    CYLChicken = cylc()
    lunch = cold_lunch()
    dinner = cold_dinner
    pizza = ("pizza", "fish sticks", "nuggets", "quesadillas", "grilled cheese", "mac and cheese", "pasta", "ramen", "popovers", "quiche",{OnePot},{cold_dinner})
    pizza = random.choice(pizza)
    
    selection = False
    choice = False
    while selection == False:
        weather = input("Is this week hot or cold?").lower()
        if weather == "hot":
            t_day = cold_dinner
            h_day = grill
            choice = True
            selection = True
            break
        elif weather == "cold":
            t_day = input("Would you like a bowl or a casserole? ").lower()
            if t_day == "bowl":
                t_day = bowl
                selection = True
                break
            elif t_day == "casserole":
                t_day = casserole
                selection = True
                break
            else:
                print("Please type 'bowl' or 'casserole'.")
                continue
        else:
            print("Please type 'hot' or 'cold'.")
            continue
    
    while choice == False:
        h_day = input("How much effort should dinner be, Level One or Two? ").lower()
        if h_day == "one" or h_day == "1":
            h_day = dinner
            choice = True
            break
        elif h_day == "two" or h_day == "2":
            h_day = level_two
            choice = True
            break 
        else:
            print("Please type '1' or '2'.")
            pass
        
    Monday = (f"Monday:\n\t Lunch: {lunch}\n\t Dinner: {mexican} \n")
    lunch = hot_lunch()
    Tuesday = (f"Tuesday:\n\t Lunch: {lunch}\n\t Dinner: {t_day} \n")
    lunch = hot_lunch()
    Wednesday = (f"Wednesday:\n\t Lunch: {lunch}\n\t Dinner: {CYLChicken} \n")
    lunch = hot_lunch()
    Thursday = (f"Thursday:\n\t Lunch: {lunch}\n\t Dinner: {h_day} \n")
    lunch = cold_lunch()
    Friday = (f"Friday:\n\t Lunch: {lunch}\n\t Dinner: {OnePot} \n")
    lunch = hot_lunch()
    Saturday = (f"Saturday:\n\t Lunch: {lunch}\n\t Dinner: {weekend} \n")
    lunch = hot_lunch()
    Sunday = (f"Sunday:\n\t Lunch: {lunch}\n\t Dinner: {instant_pot} \n")
    print(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)


def dinner_categories():
    casserole = (
        "enchiladas", 
        "baked spaghetti", 
        "chicken broccoli bake", 
        "lasagna", 
        "hash",)
    casserole = random.choice(casserole)
    mexican = ("tacos", "burritos", "fajitas", "nachos")
    mexican =  random.choice(mexican)
    OnePot = (
        "stew",
        "spanakorizo, https://www.beryl.nyc/index.php/2024/03/08/spanakorizo/",
        "Milho, https://www.beryl.nyc/index.php/2024/03/08/milho/",
        "Przeni Kupus sa Kobasicama, https://www.beryl.nyc/index.php/2024/03/08/przeni-kupus-sa-kobasicama/",
    )
    OnePot = random.choice(OnePot)
    level_2 = (
        f"Bonne Femme Chicken:{bonnefemme()}",
        "hash", 
        "crepes", 
        "stromboli", 
        "pita", 
        "taco salad", 
        "risotto", 
        "curry",)
    level_two = random.choice(level_2)
    instant_pot = (
        "pork pot roast", 
        "beef pot roast", 
        "beef stroganoff", 
        "split pea soup", 
        "goulash", 
        "chili",
        "pulled pork",
        "red beans and rice",
        "cowboy beans and rice")
    instant_pot = random.choice(instant_pot)
    weekend = (
        "quiche", 
        "french toast", 
        "bacon and eggs", 
        "chicken nuggets", 
        "fish",
        "sandwiches",
        "quesadillas",)
    weekend = random.choice(weekend)
    grill = ("burgers",
             "brats",
             "chicken thighs",
             "boneless chicken",
             "whole chicken",
             "kebab",
             "kofte",)
    grill = random.choice(grill)
    cd_dinn = ("kimbap", 
               "taco salad", 
               "gazpacho", 
               "spring rolls", 
               "sandwiches", 
               "charcuterie",
               "cowboy caviar",
               "black bean, rice, corn salad",
               "cold chicken pita",
               "panzanella")
    cold_dinner = random.choice(cd_dinn)
    return (casserole, mexican, OnePot, level_two, instant_pot, weekend, grill, cold_dinner)

def cold_lunch():
    cd_lunch = ("pasta salad", "sandwiches", "wraps", "charcuterie", "chicken salad", "couscous", "quesadillas")
    lunch = random.choice(cd_lunch)
    return lunch

def hot_lunch():
    ht_lunch = ("ramen", "pasta", "grilled cheese", "popovers", "dutch baby", "chips and dip", "mac and cheese", "nuggets and fries", "fish sticks", "sweet potato", "baked potato")
    lunch = random.choice(ht_lunch)
    return lunch

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
    toppings = (mediterranean, italian, faux_asian, faux_thai, mid_med, mexish, murican, "bulgogi")
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
