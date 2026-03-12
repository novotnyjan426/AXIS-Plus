from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/coffee_estate_1.png"
CLASS_ID = "AXPA"
CLASS_NAME = "STR_OBJECT_CLASS_AGRICULTURE_EXPANSIONS"
GROUND = "GROUNDSPRITE_NORMAL"

house = ExpansionObject(
    id="coffee_estate_exp_house",
    numeric_id=138,
    name_string="STR_OBJECT_COFFEE_HOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 59, -31, -28],
    ground_sprite=GROUND,
    height=8,
)

shed = ExpansionObject(
    id="coffee_estate_exp_shed",
    numeric_id=139,
    name_string="STR_OBJECT_COFFEE_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 10, 64, 59, -31, -28],
    ground_sprite=GROUND,
    height=6,
)
