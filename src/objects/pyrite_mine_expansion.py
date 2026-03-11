from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/pyrite_mine_1.png"
CLASS_ID = "AXPM"
CLASS_NAME = "STR_OBJECT_CLASS_MINE_EXPANSIONS"
GROUND = "GROUNDSPRITE_NORMAL"

pyrite_pile = ExpansionObject(
    id="pyrite_exp_pile",
    numeric_id=161,
    name_string="STR_OBJECT_PYRITE_PILE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 122, -31, -90],
    ground_sprite=GROUND,
    height=4,
)

pyrite_pile_small = ExpansionObject(
    id="pyrite_exp_pile_small",
    numeric_id=162,
    name_string="STR_OBJECT_PYRITE_PILE_SMALL",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[290, 10, 64, 122, -31, -90],
    ground_sprite=GROUND,
    height=3,
)
