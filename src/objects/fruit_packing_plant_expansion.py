from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/fruit_packing_plant_1.png"
CLASS_ID = "AXSF"
CLASS_NAME = "STR_OBJECT_CLASS_FOOD_PROCESSING"
GROUND = "GROUNDSPRITE_CONCRETE"

# sp1: warehouse building
warehouse = ExpansionObject(
    id="fruit_packing_exp_warehouse",
    numeric_id=315,
    name_string="STR_OBJECT_FRUIT_PACKING_WAREHOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 76, -31, -45],
    ground_sprite=GROUND,
    height=10,
)

# sp3: silo/hopper equipment (replaces duplicate sp2)
silo = ExpansionObject(
    id="fruit_packing_exp_silo",
    numeric_id=316,
    name_string="STR_OBJECT_FRUIT_PACKING_SILO",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 10, 64, 63, -31, -32],
    ground_sprite=GROUND,
    height=8,
)
