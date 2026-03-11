from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/rubber_plantation_1.png"
CLASS_ID = "AXPA"
CLASS_NAME = "STR_OBJECT_CLASS_AGRICULTURE_EXPANSIONS"
GROUND = "GROUNDSPRITE_NORMAL"

# All rubber plantation sprites are 64x59, offsets -31, -28

warehouse = ExpansionObject(
    id="rubber_exp_warehouse",
    numeric_id=100,
    name_string="STR_OBJECT_RUBBER_WAREHOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 59, -31, -28],
    ground_sprite=GROUND,
    height=8,
)

shed = ExpansionObject(
    id="rubber_exp_shed",
    numeric_id=101,
    name_string="STR_OBJECT_RUBBER_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 10, 64, 59, -31, -28],
    ground_sprite=GROUND,
    height=6,
)
