from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/herding_coop_1.png"
CLASS_ID = "AXPA"
CLASS_NAME = "STR_OBJECT_CLASS_AGRICULTURE_EXPANSIONS"
GROUND = "GROUNDSPRITE_NORMAL"

hut = ExpansionObject(
    id="herding_exp_hut",
    numeric_id=135,
    name_string="STR_OBJECT_HERDING_HUT",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 52, -31, -21],
    ground_sprite=GROUND,
    height=8,
)

hut_small = ExpansionObject(
    id="herding_exp_hut_small",
    numeric_id=136,
    name_string="STR_OBJECT_HERDING_HUT_SMALL",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[360, 10, 64, 52, -31, -21],
    ground_sprite=GROUND,
    height=6,
)
