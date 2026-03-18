from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/lumber_yard_1.png"
CLASS_ID = "AXSB"
CLASS_NAME = "STR_OBJECT_CLASS_BUILDING_MATERIALS"
GROUND = "GROUNDSPRITE_CONCRETE"

# Warehouse
warehouse = ExpansionObject(
    id="lumber_yard_exp_warehouse",
    numeric_id=433,
    name_string="STR_OBJECT_LUMBER_YARD_WAREHOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 10, 64, 64, -31, -40],
    ground_sprite=GROUND,
    height=8,
)

# Shed
shed = ExpansionObject(
    id="lumber_yard_exp_shed",
    numeric_id=434,
    name_string="STR_OBJECT_LUMBER_YARD_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 10, 64, 64, -31, -34],
    ground_sprite=GROUND,
    height=8,
)
