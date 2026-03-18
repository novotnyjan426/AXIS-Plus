from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/farm_supply_yard_1.png"
CLASS_ID = "AXSX"
CLASS_NAME = "STR_OBJECT_CLASS_OTHER_INDUSTRY"
GROUND = "GROUNDSPRITE_CONCRETE"

# Shed
shed = ExpansionObject(
    id="farm_supply_yard_exp_shed",
    numeric_id=455,
    name_string="STR_OBJECT_FARM_SUPPLY_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 64, -31, -32],
    ground_sprite=GROUND,
    height=8,
)

# Warehouse
warehouse = ExpansionObject(
    id="farm_supply_yard_exp_warehouse",
    numeric_id=456,
    name_string="STR_OBJECT_FARM_SUPPLY_WAREHOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 10, 64, 64, -31, -32],
    ground_sprite=GROUND,
    height=8,
)
