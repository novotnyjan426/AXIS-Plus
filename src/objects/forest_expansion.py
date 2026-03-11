from objects.base_object import ExpansionObject

CLASS_ID = "AXPA"
CLASS_NAME = "STR_OBJECT_CLASS_AGRICULTURE_EXPANSIONS"
GROUND = "GROUNDSPRITE_NORMAL"

# All forest sprites are 64x78, offsets -31, -45
# 3 variants from forest_1/2/3.png

logging_crane = ExpansionObject(
    id="forest_exp_crane",
    numeric_id=145,
    name_string="STR_OBJECT_FOREST_CRANE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file="src/graphics/industries/forest_1.png",
    sprite_coords=[10, 10, 64, 78, -31, -45],
    ground_sprite=GROUND,
    height=10,
)

logging_crane_alt = ExpansionObject(
    id="forest_exp_crane_alt",
    numeric_id=146,
    name_string="STR_OBJECT_FOREST_CRANE_ALT",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file="src/graphics/industries/forest_2.png",
    sprite_coords=[10, 10, 64, 78, -31, -45],
    ground_sprite=GROUND,
    height=10,
)

equipment = ExpansionObject(
    id="forest_exp_equipment",
    numeric_id=147,
    name_string="STR_OBJECT_FOREST_EQUIPMENT",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file="src/graphics/industries/forest_1.png",
    sprite_coords=[80, 10, 64, 78, -31, -45],
    ground_sprite=GROUND,
    height=4,
)

log_pile = ExpansionObject(
    id="forest_exp_logs",
    numeric_id=148,
    name_string="STR_OBJECT_FOREST_LOGS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file="src/graphics/industries/forest_1.png",
    sprite_coords=[150, 10, 64, 78, -31, -45],
    ground_sprite=GROUND,
    height=4,
)

log_pile_alt = ExpansionObject(
    id="forest_exp_logs_alt",
    numeric_id=149,
    name_string="STR_OBJECT_FOREST_LOGS_ALT",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file="src/graphics/industries/forest_3.png",
    sprite_coords=[150, 10, 64, 78, -31, -45],
    ground_sprite=GROUND,
    height=4,
)
