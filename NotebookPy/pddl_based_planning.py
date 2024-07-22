


print('--------------------- Define constants for all tasks ---------------------')
#@title Define constants for all tasks {display-mode: "form"}

# define constants for objects in dataset
dish, = constants("dish", types=["utensil"])
cleaning_bottle, = constants("cleaning_bottle ", types=["utensil"])
cooking_pot, = constants("cooking_pot ", types=["utensil"])
frying_pan, = constants("frying_pan ", types=["utensil"])
trash_can, = constants("trash_can ", types=["utensil"])
cloth_napkin, = constants("cloth_napkin ", types=["utensil"])
paper_towel, = constants("paper_towel ", types=["utensil"])
bucket, = constants("bucket ", types=["utensil"])
coffee_cup, = constants("coffee_cup ", types=["utensil"])
colander, = constants("colander ", types=["utensil"])
condiment_bottle, = constants("condiment_bottle ", types=["utensil"])
dish_bowl, = constants("dish_bowl ", types=["utensil"])
drinking_glass, = constants("drinking_glass ", types=["utensil"])
measuring_cup, = constants("measuring_cup ", types=["utensil"])
mug, = constants("mug ", types=["utensil"])
rag, = constants("rag ", types=["utensil"])
wine_glass, = constants("wine_glass ", types=["utensil"])
chef_knife, = constants("chef_knife ", types=["utensil"])
condiment_shaker, = constants("condiment_shaker ", types=["utensil"])
cutlery_fork, = constants("cutlery_fork ", types=["utensil"])
cutlery_knife, = constants("cutlery_knife ", types=["utensil"])
cutting_board, = constants("cutting_board ", types=["utensil"])
dish_rack, = constants("dish_rack ", types=["utensil"])
oven_tray, = constants("oven_tray ", types=["utensil"])
mat, = constants("mat ", types=["utensil"])
wooden_spoon, = constants("wooden_spoon ", types=["utensil"])
sponge, = constants("sponge ", types=["utensil"])
coffee_filter, = constants("coffee_filter ", types=["utensil"])
wooden_chopstick, = constants("wooden_chopstick ", types=["utensil"])

beer, = constants("beer", types=["beverage"])
milk, = constants("milk", types=["beverage"])
watermelon_juice, = constants("watermelon_juice", types=["beverage"])
alcohol, = constants("alcohol", types=["beverage"])
coffee, = constants("coffee", types=["beverage"])
orange_juice, = constants("orange_juice", types=["beverage"])
tea, = constants("tea", types=["beverage"])
wine, = constants("wine", types=["beverage"])

bookshelf, = constants("bookshelf ", types=["furniture"])
closet, = constants("closet ", types=["furniture"])
cpu_table, = constants("cpu_table ", types=["furniture"])
cupboard, = constants("cupboard ", types=["furniture"])
desk, = constants("desk ", types=["furniture"])
kitchen_cabinet, = constants("kitchen_cabinet ", types=["furniture"])
nightstand, = constants("nightstand ", types=["furniture"])
wooden_chair, = constants("wooden_chair ", types=["furniture"])
piano_bench, = constants("piano_bench ", types=["furniture"])
table_cloth, = constants("table_cloth ", types=["furniture"])
coffee_table, = constants("coffee_table ", types=["furniture"])
couch, = constants("couch ", types=["furniture"])
dining_table, = constants("dining_table ", types=["furniture"])
kitchen_table, = constants("kitchen_table ", types=["furniture"])
kitchen_counter, = constants("kitchen_counter ", types=["furniture"])
pantry, = constants("pantry ", types=["furniture"])

bread, = constants("bread ", types=["food"])
cake, = constants("cake ", types=["food"])
ice_cream, = constants("ice_cream ", types=["food"])
noodles, = constants("noodles ", types=["food"])
oatmeal, = constants("oatmeal ", types=["food"])
peanut_butter, = constants("peanut_butter ", types=["food"])
rice, = constants("rice ", types=["food"])
salt, = constants("salt ", types=["food"])
snack, = constants("snack ", types=["food"])
sugar, = constants("sugar ", types=["food"])
oil, = constants("oil ", types=["food"])
pasta, = constants("pasta ", types=["food"])
chips, = constants("chips ", types=["food"])
sauce, = constants("sauce ", types=["food"])
steak, = constants("steak ", types=["food"])

blender, = constants("blender ", types=["appliance"])
dishwasher, = constants("dishwasher ", types=["appliance"])
freezer, = constants("freezer ", types=["appliance"])
microwave, = constants("microwave ", types=["appliance"])
refrigerator, = constants("refrigerator ", types=["appliance"])
oven, = constants("oven ", types=["appliance"])
stove, = constants("stove ", types=["appliance"])
washing_machine, = constants("washing_machine ", types=["appliance"])
kettle, = constants("kettle ", types=["appliance"])
vacuum_cleaner, = constants("vacuum_cleaner ", types=["appliance"])
toaster, = constants("toaster ", types=["appliance"])
air_fryer, = constants("air_fryer ", types=["appliance"])
dehumidifier, = constants("dehumidifier ", types=["appliance"])
water_boiler, = constants("water_boiler ", types=["appliance"])
ice_cream_maker, = constants("ice_cream_maker ", types=["appliance"])
juicer, = constants("juicer ", types=["appliance"])
water_filter, = constants("water_filter ", types=["appliance"])
coffee_maker, = constants("coffee_maker ", types=["appliance"])

loca, loca1, loca2, = variables("loca loca1 loca2 ", types=["location"])
appl, = variables("appl ", types=["appliance"])
appliance_at = Predicate("appliance_at", appl, loca)
kitchen, dining, basement, = constants("kitchen dining basement ", types=["location"])





