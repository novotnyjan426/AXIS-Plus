from objects.base_object import ExpansionObject

SPRITE_FILE_1 = "src/graphics/industries/arable_farm_1.png"
SPRITE_FILE_2 = "src/graphics/industries/arable_farm_2.png"
CLASS_ID = "AXPA"
CLASS_NAME = "STR_OBJECT_CLASS_AGRICULTURE_EXPANSIONS"
GROUND = "GROUNDSPRITE_NORMAL"

# All arable farm sprites are 64x59, offsets -31, -28

# --- Variant 1 (arable_farm_1.png) ---

barn = ExpansionObject(
    id="arable_exp_barn",
    numeric_id=60,
    name_string="STR_OBJECT_ARABLE_BARN",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE_1,
    sprite_coords=[10, 10, 64, 59, -31, -28],
    ground_sprite=GROUND,
    height=8,
)

farm_cart = ExpansionObject(
    id="arable_exp_farm_cart",
    numeric_id=61,
    name_string="STR_OBJECT_ARABLE_FARM_CART",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE_1,
    sprite_coords=[80, 10, 64, 59, -31, -28],
    ground_sprite=GROUND,
    height=2,
)

farmhouse = ExpansionObject(
    id="arable_exp_farmhouse",
    numeric_id=62,
    name_string="STR_OBJECT_ARABLE_FARMHOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE_1,
    sprite_coords=[150, 10, 64, 59, -31, -28],
    ground_sprite=GROUND,
    height=8,
)

granary = ExpansionObject(
    id="arable_exp_granary",
    numeric_id=63,
    name_string="STR_OBJECT_ARABLE_GRANARY",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE_1,
    sprite_coords=[220, 10, 64, 59, -31, -28],
    ground_sprite=GROUND,
    height=8,
)

grain_silo = ExpansionObject(
    id="arable_exp_grain_silo",
    numeric_id=64,
    name_string="STR_OBJECT_ARABLE_GRAIN_SILO",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE_1,
    sprite_coords=[290, 10, 64, 59, -31, -28],
    ground_sprite=GROUND,
    height=12,
)

# --- Variant 2 (arable_farm_2.png) ---

barn_alt = ExpansionObject(
    id="arable_exp_barn_alt",
    numeric_id=65,
    name_string="STR_OBJECT_ARABLE_BARN_ALT",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE_2,
    sprite_coords=[10, 10, 64, 59, -31, -28],
    ground_sprite=GROUND,
    height=8,
)

farm_cart_alt = ExpansionObject(
    id="arable_exp_farm_cart_alt",
    numeric_id=66,
    name_string="STR_OBJECT_ARABLE_FARM_CART_ALT",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE_2,
    sprite_coords=[80, 10, 64, 59, -31, -28],
    ground_sprite=GROUND,
    height=2,
)

farmhouse_alt = ExpansionObject(
    id="arable_exp_farmhouse_alt",
    numeric_id=67,
    name_string="STR_OBJECT_ARABLE_FARMHOUSE_ALT",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE_2,
    sprite_coords=[150, 10, 64, 59, -31, -28],
    ground_sprite=GROUND,
    height=8,
)

granary_alt = ExpansionObject(
    id="arable_exp_granary_alt",
    numeric_id=68,
    name_string="STR_OBJECT_ARABLE_GRANARY_ALT",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE_2,
    sprite_coords=[220, 10, 64, 59, -31, -28],
    ground_sprite=GROUND,
    height=8,
)

grain_silo_alt = ExpansionObject(
    id="arable_exp_grain_silo_alt",
    numeric_id=69,
    name_string="STR_OBJECT_ARABLE_GRAIN_SILO_ALT",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE_2,
    sprite_coords=[290, 10, 64, 59, -31, -28],
    ground_sprite=GROUND,
    height=12,
)
