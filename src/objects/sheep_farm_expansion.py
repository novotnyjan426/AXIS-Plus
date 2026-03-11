from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/sheep_farm_1.png"
CLASS_ID = "AXPA"
CLASS_NAME = "STR_OBJECT_CLASS_AGRICULTURE_EXPANSIONS"
GROUND = "GROUNDSPRITE_NORMAL"

# All sheep farm building sprites are 64x52

barn = ExpansionObject(
    id="sheep_exp_barn",
    numeric_id=105,
    name_string="STR_OBJECT_SHEEP_BARN",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 52, -31, -21],
    ground_sprite=GROUND,
    height=8,
)

farmhouse = ExpansionObject(
    id="sheep_exp_farmhouse",
    numeric_id=106,
    name_string="STR_OBJECT_SHEEP_FARMHOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 10, 64, 52, -31, -19],
    ground_sprite=GROUND,
    height=8,
)

shed = ExpansionObject(
    id="sheep_exp_shed",
    numeric_id=107,
    name_string="STR_OBJECT_SHEEP_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 10, 64, 52, -31, -21],
    ground_sprite=GROUND,
    height=6,
)

sheep_pen = ExpansionObject(
    id="sheep_exp_pen",
    numeric_id=108,
    name_string="STR_OBJECT_SHEEP_PEN",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 52, -31, -21],
    ground_sprite=GROUND,
    height=2,
)

sheep_pen_alt = ExpansionObject(
    id="sheep_exp_pen_alt",
    numeric_id=109,
    name_string="STR_OBJECT_SHEEP_PEN_ALT",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[290, 10, 64, 52, -31, -21],
    ground_sprite=GROUND,
    height=2,
)
