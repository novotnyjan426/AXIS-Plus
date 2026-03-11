from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/ranch_1.png"
CLASS_ID = "AXPA"
CLASS_NAME = "STR_OBJECT_CLASS_AGRICULTURE_EXPANSIONS"
GROUND = "GROUNDSPRITE_NORMAL"

# All ranch sprites are 64x52

ranch_house = ExpansionObject(
    id="ranch_exp_house",
    numeric_id=120,
    name_string="STR_OBJECT_RANCH_HOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 52, -31, -21],
    ground_sprite=GROUND,
    height=8,
)

ranch_house_alt = ExpansionObject(
    id="ranch_exp_house_alt",
    numeric_id=121,
    name_string="STR_OBJECT_RANCH_HOUSE_ALT",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 10, 64, 52, -31, -19],
    ground_sprite=GROUND,
    height=8,
)

cottage = ExpansionObject(
    id="ranch_exp_cottage",
    numeric_id=122,
    name_string="STR_OBJECT_RANCH_COTTAGE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 10, 64, 52, -31, -21],
    ground_sprite=GROUND,
    height=6,
)

hay_bales = ExpansionObject(
    id="ranch_exp_hay",
    numeric_id=123,
    name_string="STR_OBJECT_RANCH_HAY",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 52, -31, -21],
    ground_sprite=GROUND,
    height=4,
)

hay_bales_alt = ExpansionObject(
    id="ranch_exp_hay_alt",
    numeric_id=124,
    name_string="STR_OBJECT_RANCH_HAY_ALT",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[290, 10, 64, 52, -31, -21],
    ground_sprite=GROUND,
    height=4,
)
