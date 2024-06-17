#CYL Chicken requires chicken, starch, two vegetables, seasoning 
import random
def cylc():
    seasoning = seasonings()
    starch = ("sweet potato", "carrots", "winter squash", "chickpeas")
    green_vegetable = ("green beans", "broccoli", "cabbage", "snow peas", "asparagus", "bok choy", "brussels sprouts")
    color_vegetable = ("bell peppers", "summer squash", "parsnips", "beets", "mushrooms", "tomatoes")
    CYLC = ("bone-in chicken", "onion", "potato", random.choice(starch), random.choice(green_vegetable), random.choice(color_vegetable), seasoning)
    return(CYLC)

def seasonings():
    go_to = ("Go-to: salt pepper, garlic powder, onion powder, smoked paprika")
    faux_french = ("French: salt, pepper, tarragon, marjoram, sage, garlic powder, minced onion")
    kofte = ("kofte: salt, pepper, pul biber, cumin, sumac","minced onion")
    turkish = ("Turkish: salt, pepper, pul biber, parsley, garlic")
    autumn = ("Autumn: salt, pepper, onion powder, sage, nutmeg")
    faux_italian = ("Italian: salt, pepper, garlic powder, oregano, basil, thyme, parmesan powder")
    jerk = ("Jerk: salt, onion powder, garlic powder, cayenne pepper, smoked paprika, allspice, pepper, pepper flakes, cumin, nutmeg, cinnamon, brown sugar, thyme, parsley")
    seasoning = (go_to, faux_french, kofte, turkish, autumn, faux_italian, jerk, "cajun", "ranch")
    return(random.choice(seasoning))

if __name__ == "__main__":
    CYLC = cylc()
    print(CYLC)
