from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/limestone_mine_1.png"
CLASS_ID = "AXPM"
CLASS_NAME = "STR_OBJECT_CLASS_MINE_EXPANSIONS"
GROUND = "GROUNDSPRITE_NORMAL"

limestone_pile = ExpansionObject(
    id="limestone_exp_pile",
    numeric_id=156,
    name_string="STR_OBJECT_LIMESTONE_PILE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 122, -31, -90],
    ground_sprite=GROUND,
    height=4,
)

limestone_pile_small = ExpansionObject(
    id="limestone_exp_pile_small",
    numeric_id=157,
    name_string="STR_OBJECT_LIMESTONE_PILE_SMALL",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[290, 10, 64, 122, -31, -90],
    ground_sprite=GROUND,
    height=3,
)
