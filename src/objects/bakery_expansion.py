from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/bakery_1.png"
CLASS_ID = "AXSF"
CLASS_NAME = "STR_OBJECT_CLASS_FOOD_PROCESSING"
GROUND = "GROUNDSPRITE_CONCRETE"

# Bakery expansion objects
# sprite coords from bakery.py spritesets (row 2 buildings)

oven_house = ExpansionObject(
    id="bakery_exp_oven_house",
    numeric_id=306,
    name_string="STR_OBJECT_BAKERY_OVEN_HOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 60, 64, 82, -31, -51],
    ground_sprite=GROUND,
    height=10,
)

warehouse = ExpansionObject(
    id="bakery_exp_warehouse",
    numeric_id=307,
    name_string="STR_OBJECT_BAKERY_WAREHOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 60, 64, 82, -31, -51],
    ground_sprite=GROUND,
    height=10,
)
