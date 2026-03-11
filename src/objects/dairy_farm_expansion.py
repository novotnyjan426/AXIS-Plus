from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/dairy_farm_1.png"
CLASS_ID = "AXPA"
CLASS_NAME = "STR_OBJECT_CLASS_AGRICULTURE_EXPANSIONS"
GROUND = "GROUNDSPRITE_NORMAL"

# All dairy farm sprites are 64x52, offsets -31, -21

barn = ExpansionObject(
    id="dairy_exp_barn",
    numeric_id=110,
    name_string="STR_OBJECT_DAIRY_BARN",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 52, -31, -21],
    ground_sprite=GROUND,
    height=8,
)

barn_silo = ExpansionObject(
    id="dairy_exp_barn_silo",
    numeric_id=111,
    name_string="STR_OBJECT_DAIRY_BARN_SILO",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 10, 64, 52, -31, -21],
    ground_sprite=GROUND,
    height=10,
)

large_barn = ExpansionObject(
    id="dairy_exp_large_barn",
    numeric_id=112,
    name_string="STR_OBJECT_DAIRY_LARGE_BARN",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 10, 64, 52, -31, -21],
    ground_sprite=GROUND,
    height=8,
)

farmhouse = ExpansionObject(
    id="dairy_exp_farmhouse",
    numeric_id=113,
    name_string="STR_OBJECT_DAIRY_FARMHOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 52, -31, -21],
    ground_sprite=GROUND,
    height=8,
)

cattle_pen = ExpansionObject(
    id="dairy_exp_pen",
    numeric_id=114,
    name_string="STR_OBJECT_DAIRY_PEN",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[290, 10, 64, 52, -31, -21],
    ground_sprite=GROUND,
    height=2,
)

cattle_pen_alt = ExpansionObject(
    id="dairy_exp_pen_alt",
    numeric_id=115,
    name_string="STR_OBJECT_DAIRY_PEN_ALT",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[360, 10, 64, 52, -31, -21],
    ground_sprite=GROUND,
    height=2,
)
