from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/fruit_plantation_1.png"
CLASS_ID = "AXPA"
CLASS_NAME = "STR_OBJECT_CLASS_AGRICULTURE_EXPANSIONS"
GROUND = "GROUNDSPRITE_NORMAL"

# All fruit plantation sprites are 64x59, offsets -31, -28

plantation_house = ExpansionObject(
    id="fruit_exp_house",
    numeric_id=70,
    name_string="STR_OBJECT_FRUIT_HOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 59, -31, -28],
    ground_sprite=GROUND,
    height=8,
)

plantation_shed = ExpansionObject(
    id="fruit_exp_shed",
    numeric_id=71,
    name_string="STR_OBJECT_FRUIT_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 10, 64, 59, -31, -28],
    ground_sprite=GROUND,
    height=4,
)
